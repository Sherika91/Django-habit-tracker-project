import asyncio
import os

import requests
from celery import current_task
from telegram import Bot

from habit.tasks import send_reminder_message


URL = os.getenv('TELEGRAM_BOT_URL')
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


class MyBot:

    def sent_reminder_message(self, habit_name):
        """ Send reminder message to user """

        try:
            requests.post(
                url=f'{URL}{TOKEN}/sendMessage',
                data={'chat_id': 377922624,
                      'text': f'Hello, this is a reminder message to complete your habit! {habit_name}'
                      }
            )

        except TypeError:
            pass
