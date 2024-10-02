from django.db import models
from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    place = models.CharField(
        max_length=255,
        verbose_name='Место привычки',
        help_text='Укажите место, где необходимо выполнять привычку',
        blank=True,
        null=True,
    )
    time = models.DateTimeField(
        verbose_name='Время выполнения',
        help_text='Укажите время, когда необходимо выполнять привычку',
        blank=True,
        null=True,
    )
    action = models.CharField(
        max_length=255,
        verbose_name='Действие',
        help_text='Укажите действие, которое представляет собой привычка',
    )
    sign_nice_habit = models.BooleanField(
        default=False,
        verbose_name='Признак приятной привычки',
        help_text='Привычка, которую можно привязать к выполнению полезной привычки',
        blank=True,
        null=True,
    )
    related_habit = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Связанная привычка',
        help_text='Привычка, которая связана с другой привычкой, указывать для полезных привычек, но не для приятных',
    )
    periodicity = models.PositiveIntegerField(
        verbose_name='Периодичность выполнения',
        help_text='Укажите периодичность выполнения привычки в часах (не более 168 часов-не реже 1 раза в неделю)',
        blank=True,
        null=True,
    )
    reward = models.CharField(
        max_length=255,
        verbose_name='Вознаграждение',
        help_text='Укажите награду за выполнение привычки',
        blank=True,
        null=True,
    )
    time_to_complete = models.PositiveIntegerField(
        verbose_name='Время для выполнения привычки',
        help_text='Укажите время для выполнения привычки в секундах, не более 120 секунд',
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Признак публичности',
        help_text='Отметьте, если привычка доступна для других пользователей',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
