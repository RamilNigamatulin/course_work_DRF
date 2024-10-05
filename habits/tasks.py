from habits.models import Habit
from habits.service import send_telegram_message
from celery import shared_task
from users.models import User


@shared_task
def inform_habit(habit_id):
    """Направление информации о привычках в телеграм."""
    habit = Habit.objects.get(id=habit_id)
    user = User.objects.get(id=habit.user_id)
    message = (f'Привет! Напоминаем, что сегодня в {habit.time.strftime("%H:%M")} '
               f'нужно выполнить привычку "{habit.action}" в месте "{habit.place}".')

    print(user.tg_chat_id)

    send_telegram_message(user.tg_chat_id, message)
