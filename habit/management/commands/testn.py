from django.core.management import BaseCommand

from habit.services import MyBot
from habit.tasks import send_reminder_message


class Command(BaseCommand):
    def handle(self, *args, **options):
        my_bot = MyBot()
        my_bot.sent_reminder_message('Hello from Django!')
