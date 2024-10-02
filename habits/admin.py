from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class Habit(admin.ModelAdmin):
    list_filter = ('id', 'user', 'action',)
