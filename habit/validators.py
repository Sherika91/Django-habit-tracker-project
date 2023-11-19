from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_reward_and_pleasant_habit(value):
    if value and value.pleaseant_habit:
        raise ValidationError('Reward and pleasant habit cannot be set at the same time')


def validate_execution_time(value):
    if value > 120:
        raise ValidationError('Execution time cannot be more than 120 seconds')


def validate_related_habit(value):
    if value and not value.is_pleasant:
        raise ValidationError('Related habit must be pleasant habit')


def validate_pleasant_habit(value):
    if value.is_pleasant and (value.reward or value.pleasant_habit):
        raise ValidationError('Pleasant habit cannot have reward or pleasant habit')


def validate_last_execution_date(value):
    if timezone.now() - value.last_execution_date < timezone.timedelta(days=7):
        raise ValidationError('You cannot perform the habit less than once every 7 days.')
