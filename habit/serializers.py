from rest_framework import serializers
from .models import Habit
from . import validators


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, value):
        validators.validate_reward_and_pleasant_habit(value.get('reward'))
        validators.validate_last_execution_date(value.get('time_to_complete'))
        validators.validate_related_habit(value.get('pleasant_habit'))
        validators.validate_pleasant_habit(value)
        validators.validate_execution_time(value)
        return value
