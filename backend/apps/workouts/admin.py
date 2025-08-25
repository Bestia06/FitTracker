# workout/admin.py
from django.contrib import admin

from .models import Workout, Exercise


class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = [
        "habit_title", "date", "duration_min", "calories", "status"
    ]
    list_filter = ["status", "date", "created_at"]
    search_fields = ["habit__title", "notes"]
    ordering = ["-date", "-created_at"]
    date_hierarchy = "date"
    inlines = [ExerciseInline]
    
    def habit_title(self, obj):
        return obj.habit.title
    habit_title.short_description = "Habit"


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'workout', 'sets', 'reps', 'weight_kg']
    list_filter = ['workout__status']
    search_fields = ['name', 'workout__habit__title']