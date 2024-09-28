from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habit, HabitLog, HabitCategory
from habits.serializers import HabitSerializer, HabitLogSerializer, HabitCategorySerializer


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitLogCreateAPIView(CreateAPIView):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer


class HabitLogListAPIView(ListAPIView):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer


class HabitLogRetrieveAPIView(RetrieveAPIView):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer


class HabitLogUpdateAPIView(UpdateAPIView):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer


class HabitLogDestroyAPIView(DestroyAPIView):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer


class HabitCategoryCreateAPIView(CreateAPIView):
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer


class HabitCategoryListAPIView(ListAPIView):
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer


class HabitCategoryRetrieveAPIView(RetrieveAPIView):
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer


class HabitCategoryUpdateAPIView(UpdateAPIView):
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer


class HabitCategoryDestroyAPIView(DestroyAPIView):
    queryset = HabitCategory.objects.all()
    serializer_class = HabitCategorySerializer

