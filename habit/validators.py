from rest_framework.exceptions import ValidationError


class PleasantHabitValidator:
    def __init__(self, pleasant_habit, reward):
        self.pleasant_habit = pleasant_habit
        self.reward = reward

    def __call__(self, value):
        pleasant_habit = dict(value).get(self.pleasant_habit)
        reward = dict(value).get(self.reward)

        if pleasant_habit and reward:
            raise ValidationError('You can not set reward for pleasant habit')


class TimeValidator:
    def __init__(self,field):
        self.field = field

    def __call__(self, data):
        time_to_complete = data.get(self.field)

        if time_to_complete and isinstance(time_to_complete, int) and time_to_complete > 120:
            raise ValidationError('Time to complete cannot be more than 120 seconds.')


class LinkedHabitValidator:
    def __init__(self, pleasant_habit, is_pleasant):
        self.pleasant_habit = pleasant_habit
        self.is_pleasant = is_pleasant

    def __call__(self, value):
        pleasant_habit = dict(value).get(self.pleasant_habit)
        is_pleasant = dict(value).get(self.is_pleasant)

        if pleasant_habit and not all(habit.is_pleasant for habit in pleasant_habit):
            raise ValidationError('linked habit can only include pleasant habits')


class PleasurableRewardValidator:
    def __init__(self, is_pleasant, reward, pleasant_habit):
        self.is_pleasant = is_pleasant
        self.reward = reward
        self.pleasant_habit = pleasant_habit

    def __call__(self, data):
        is_pleasant = data.get(self.is_pleasant)
        reward = data.get(self.reward)
        pleasant_habit = data.get(self.pleasant_habit)

        if is_pleasant:
            if reward or pleasant_habit:
                pass
            raise ValidationError('A pleasant habit cannot have a reward or a linked habit.')
