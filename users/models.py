from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта',
        help_text='Укажите электронную почту',
    )
    phone = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='Номер телефона',
        help_text='Укажите номер телефона',
        blank=True,
        null=True,
    )
    tg_nickname = models.CharField(
        max_length=50,
        verbose_name='Телеграм-никнейм',
        help_text='Укажите свой Телеграм-никнейм',
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to='users/avatars',
        verbose_name='Аватарка',
        help_text='Загрузите аватарку',
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
