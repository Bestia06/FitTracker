# workout/admin.py
from django.contrib import admin
from .models import Workout, Exercise

class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'date', 'workout_type', 'calories', 'duration_minutes']
    list_filter = ['workout_type', 'date', 'created_at']
    search_fields = ['name', 'user__username']
    ordering = ['-date', '-created_at']
    date_hierarchy = 'date'
    inlines = [ExerciseInline]

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'workout', 'sets', 'reps', 'weight_kg']
    list_filter = ['workout__workout_type']
    search_fields = ['name', 'workout__name']