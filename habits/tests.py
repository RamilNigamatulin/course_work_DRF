from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from habits.models import Habit
from django.urls import reverse


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.habit_published = Habit.objects.create(action='Опубликованная привычка', periodicity=7, user=self.user,
                                                    is_published=True)
        self.habit_unpublished = Habit.objects.create(
            action='Неопубликованная привычка', periodicity=7, user=self.user, is_published=False)
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habits_create", )
        data = {
            "action": "Тест_привычка_1",
            "periodicity": 7,
        }
        response = self.client.post(url, data, )
        # print(response.content)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertTrue(
            Habit.objects.all().exists()
        )
        self.assertEqual(
            Habit.objects.all().count(), 3
        )

    def test_habit_retrieve(self):
        """ Тестирование на получение деталей привычки."""
        url = reverse("habits:habits_retrieve", args=(self.habit_published.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("action"), self.habit_published.action
        )

    def test_habit_update(self):
        """Тестирование обновление привычки."""
        url = reverse("habits:habits_update", args=(self.habit_published.pk,))
        data = {
            "action": "Тест_привычка_1",
            "periodicity": 7,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("action"), "Тест_привычка_1"
        )

    def test_habit_delete(self):
        """ Тестирование удаление привычки."""
        url = reverse("habits:habits_delete", args=(self.habit_published.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 1
        )

    def test_habit_list(self):
        """Тестирование получения списка всех привычек."""
        url = reverse("habits:habits_list", )
        response = self.client.get(url)
        data = response.json()
        result = {'count': 2,
                  'next': None,
                  'previous': None,
                  'results': [
                      {
                          'id': self.habit_published.pk,
                          'place': None,
                          'time': None,
                          'action': self.habit_published.action,
                          'sign_nice_habit': False,
                          'periodicity': self.habit_published.periodicity,
                          'reward': None,
                          'time_to_complete': None,
                          'is_published': True,
                          'user': self.user.pk,
                          'related_habit': None
                      },
                      {
                          'id': self.habit_unpublished.pk,
                          'place': None,
                          'time': None,
                          'action': self.habit_unpublished.action,
                          'sign_nice_habit': False,
                          'periodicity': self.habit_unpublished.periodicity,
                          'reward': None,
                          'time_to_complete': None,
                          'is_published': False,
                          'user': self.user.pk,
                          'related_habit': None
                      }
                  ]
                  }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_public_habits_list(self):
        """Тестирование получения списка опубликованных привычек."""
        url = reverse("habits:public_habits_list", )
        response = self.client.get(url)
        data = response.json()
        result = {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.habit_published.pk,
                        'place': None,
                        'time': None,
                        'action': self.habit_published.action,
                        'sign_nice_habit': False,
                        'periodicity': self.habit_published.periodicity,
                        'reward': None,
                        'time_to_complete': None,
                        'is_published': True,
                        'user': self.user.pk,
                        'related_habit': None
                    }
                ]
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
