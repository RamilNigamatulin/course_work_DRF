from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.serializers import HabitSerializer
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from habits.service import send_telegram_message


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)

    def periodic_task(self, habit):
        PeriodicTask.objects.filter(name=f'habit_reminder{habit.id}').delete()

        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=habit.time.minute,
            hour=habit.time.hour,
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
        )

        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'habit_reminder{habit.id}',
            task='habit.tasks.habit_reminder',
        )
        send_telegram_message.delay(user.tg_chat_id, message)


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемой привычке."""
        serializer.save(user=self.request.user)

    def periodic_task(self, habit):

        # PeriodicTask.objects.filter(name=f'habit_reminder{habit.id}').delete()

        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=habit.time.minute,
            hour=habit.time.hour,
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
        )

        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'habit_reminder{habit.id}',
            task='habit.tasks.habit_reminder',
        )
        send_telegram_message.delay(user.tg_chat_id, message)


class PublicHabitListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
