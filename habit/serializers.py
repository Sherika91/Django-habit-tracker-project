from rest_framework import serializers
from .models import Habit
from . import validators


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [validators.PleasantHabitValidator('pleasant_habit', 'reward'),
                      validators.TimeValidator('time_to_complete'),
                      validators.LinkedHabitValidator('pleasant_habit', 'is_pleasant'),
                      validators.PleasurableRewardValidator('is_pleasant', 'reward', 'pleasant_habit')]
