from django.urls import path
from habits.models import Habit, HabitLog, HabitCategory
from habits.views import (HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView, HabitListAPIView,
                          HabitRetrieveAPIView)
from habits.apps import HabitsConfig


app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habits_list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits_retrieve'),
    path('habits/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habits_update'),
    path('habits/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habits_delete'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habits_create'),
]
