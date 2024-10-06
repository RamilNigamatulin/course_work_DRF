from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from habits.tasks import notify_habit_created, notify_habit_update


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        """ Вызываем задачи Celery для отправки уведомления."""
        habit = serializer.save()
        notify_habit_update.delay(habit.id)


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Открываем доступ только к своим привычкам."""
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Привязываем текущего пользователя к создаваемой привычке и вызываем задачи Celery для отправки уведомления.
        """
        habit = serializer.save(user=self.request.user)
        notify_habit_created.delay(habit.id)


class PublicHabitListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
