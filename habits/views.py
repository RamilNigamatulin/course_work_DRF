from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.serializers import HabitSerializer


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
        return Habit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемой привычке."""
        serializer.save(user=self.request.user)


class PublicHabitListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_published=True)
    serializer_class = HabitSerializer