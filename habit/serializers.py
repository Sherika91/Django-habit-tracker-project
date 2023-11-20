from rest_framework import serializers
from .models import Habit
from . import validators


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
