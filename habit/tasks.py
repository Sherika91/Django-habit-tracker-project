import os

import requests
from celery.schedules import crontab
from celery import shared_task, current_task
from django.core.mail import send_mail
from dotenv import load_dotenv

from config.celery import app
from habit.models import Habit

load_dotenv()

URL = os.getenv('TELEGRAM_BOT_URL')
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


@shared_task
def send_email_reminder(email, habit_name):
    """ Send reminder email to user """
    try:
        send_mail(
            subject='Reminder',
            message='Hello, this is a reminder message to complete your habit!' + habit_name,
            from_email=os.getenv('EMAIL_HOST_USER'),
            recipient_list=[email],
            fail_silently=False
        )
    except Exception as e:
        current_task.retry(exc=e, countdown=60)


@shared_task
def send_reminder_message(habit_name):
    """ Send reminder message to user """

    try:
        requests.post(
            url=f'{URL}{TOKEN}/sendMessage',
            data={'chat_id': 377922624,  # User Telegram ID Here
                  'text': f'Hello, this is a reminder message to complete your habit! {habit_name}'
                  }
        )
    except Exception as e:
        current_task.retry(exc=e, countdown=60)


@shared_task
def check_habit_completion():
    """ if habit is not completed and time is less than or equal to now, send reminder message """
    habits = Habit.objects.all()

    for habit in habits:
        send_email_reminder.delay(habit.owner.email, habit.habit_name)
        send_reminder_message.delay(habit.habit_name)


app.conf.beat_schedule = {
    'check_habit_completion': {
        'task': 'habit.tasks.check_habit_completion',
        'schedule': crontab(hour=15, minute=00),  # EVERY DAY AT 15:00
    },
}

app.conf.timezone = 'Europe/Moscow'
