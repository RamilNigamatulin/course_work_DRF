from celery import shared_task
from habits.models import Habit
from habits.service import send_telegram_message
from users.models import User
from datetime import datetime


@shared_task
def send_daily_habits():
    """Отправка информации о привычках ежедневно в телеграм."""
    now = datetime.now()
    day_of_week = now.weekday()  # Получаем текущий день недели (0 - понедельник, 6 - воскресенье)

    # Фильтруем привычки по дню недели и времени
    habits = Habit.objects.filter(
        time__hour=now.hour,
        time__minute=now.minute,
        periodicity__contains=[day_of_week]  # Фильтруем по текущему дню недели
    )

    for habit in habits:
        user = User.objects.get(id=habit.user_id)
        if user.tg_chat_id:
            text = (
                f'Привет! Напоминаем, что сегодня в {habit.time.strftime("%H:%M")} нужно выполнить '
                f'привычку "{habit.action}" в месте "{habit.place}".'
            )
            send_telegram_message(user.tg_chat_id, text)


@shared_task
def notify_habit_created(habit_id):
    """Отправка уведомления о создании новой привычки."""
    habit = Habit.objects.get(id=habit_id)
    user = User.objects.get(id=habit.user_id)
    if user.tg_chat_id:
        text = (
            f'Привет! Новая привычка "{habit.action}" создана для выполнения в {habit.time.strftime("%H:%M")} '
            f'в месте "{habit.place}".'
        )
        send_telegram_message(user.tg_chat_id, text)


@shared_task
def notify_habit_update(habit_id):
    """Отправка уведомления об изменении привычки."""
    habit = Habit.objects.get(id=habit_id)
    user = User.objects.get(id=habit.user_id)
    if user.tg_chat_id:
        text = (
            f'Привет! Изменена привычка "{habit.action}". Выполнение запланировано в {habit.time.strftime("%H:%M")} '
            f'в месте "{habit.place}".'
        )
        send_telegram_message(user.tg_chat_id, text)
