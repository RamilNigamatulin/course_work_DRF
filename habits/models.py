from django.db import models
from users.models import User


class HabitCategory(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название категории',
        help_text='Укажите название категории привычек',
    )
    description = models.TextField(
        verbose_name='Описание категории',
        help_text='Укажите описание категории привычек',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Категория привычек'
        verbose_name_plural = 'Категории привычек'


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    place = models.CharField(
        max_length=255,
        verbose_name='Место привычки',
        help_text='Укажите место, где необходимо выполнять привычку',
    )
    time = models.DateTimeField(
        verbose_name='Время выполнения',
        help_text='Укажите время, когда необходимо выполнять привычку',
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
        help_text='Укажите периодичность выполнения привычки в днях',
        default=1,
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
        help_text='Укажите время для выполнения привычки в минутах',
        default=180,
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name='Признак публичности',
        help_text='Отметьте, если привычка доступна для других пользователей',
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        HabitCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория привычки',
        help_text='Укажите категорию привычки',
    )

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'


class HabitLog(models.Model):
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name='logs',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='habit_logs'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата выполнения',
    )
    completed = models.BooleanField(
        default=False,
        verbose_name='Статус выполнения',
        help_text='Отметьте, если привычка выполнена',
    )

    class Meta:
        verbose_name = 'Лог выполнения привычки'
        verbose_name_plural = 'Логи выполнения привычек'
