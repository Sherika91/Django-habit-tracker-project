from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from habit.models import Habit
from users.models import User


class HabitCRUDTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@gmail.com',
            first_name='test',
            last_name='test',
        )
        self.user.set_password('test')
        self.user.save()

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            habit_name='test habit 1',
            habit_description='test habit description 1',
            owner=self.user,
            habit_action='test habit action 1',
            is_pleasant=True,
            period='DAILY',
            reward='test reward 1',
            time_to_complete=120,
            is_public=True,
        )

    def tearDown(self):
        self.user.delete()
        self.habit.delete()

    def test_create_habit(self):
        response = self.client.post(reverse('habit:habit-create'), data={
            'habit_name': 'test habit',
            'habit_description': 'test habit description',
            'owner': self.user.pk,
            'habit_action': 'test habit action',
            'is_pleasant': False,
            'period': 'DAILY',
            'reward': 'test reward',
            'time_to_complete': 120,
            'is_public': True,
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['habit_name'], 'test habit')
        self.assertEqual(response.data['owner'], self.user.pk)

    def test_get_habit_list(self):
        response = self.client.get(reverse('habit:habit-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'count': 1,
                             'next': None,
                             'previous': None,
                             'results': [
                                 {'id': self.habit.pk,
                                  'habit_name': 'test habit 1',
                                  'habit_description': 'test habit description 1',
                                  'habit_action': 'test habit action 1',
                                  'is_pleasant': True,
                                  'period': 'DAILY',
                                  'reward': 'test reward 1',
                                  'time_to_complete': 120,
                                  'is_public': True,
                                  'owner': self.user.pk,
                                  'pleasant_habit': []
                                  }]})

    def test_get_public_habit_list(self):
        response = self.client.get(reverse('habit:public-habit-list'))

        self.assertEqual(response.status_code, 200)
        first_dict = response.data[0]
        self.assertEqual(first_dict['is_public'], True)

    def test_get_habit_detail(self):
        response = self.client.get(reverse('habit:habit-detail', kwargs={'pk': self.habit.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {'id': self.habit.pk,
                          'habit_name': 'test habit 1',
                          'habit_description': 'test habit description 1',
                          'habit_action': 'test habit action 1',
                          'is_pleasant': True,
                          'period': 'DAILY',
                          'reward': 'test reward 1',
                          'time_to_complete': 120,
                          'is_public': True,
                          'owner': self.user.pk,
                          'pleasant_habit': []
                          })

    def test_update_habit(self):
        response = self.client.put(reverse('habit:habit-detail', kwargs={'pk': self.habit.pk}), data={
            'habit_name': 'test habit 2',
            'habit_description': 'test habit description 2',
            'owner': self.user.pk,
            'habit_action': 'test habit action 2',
            'is_pleasant': False,
            'period': 'DAILY',
            'reward': 'test reward 2',
            'time_to_complete': 120,
            'is_public': False,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['habit_name'], 'test habit 2')
        self.assertEqual(response.data['is_public'], False)

    def test_delete_habit(self):
        response = self.client.delete(reverse('habit:habit-detail', kwargs={'pk': self.habit.pk}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Habit.objects.count(), 0)
