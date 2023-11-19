import os

from celery import shared_task


@shared_task
def send_reminder_message():
    url = 'https://api.telegram.org/bot'
    token = os.getenv('TELEGRAM_BOT_TOKEN')


