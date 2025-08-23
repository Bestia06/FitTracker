from django.contrib import admin
from .models import Workout, Exercise, WorkoutExercise


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'date', 'duration', 'calories_burned')
    list_filter = ('date', 'user')
    search_fields = ('name', 'user__username', 'user__email')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)


@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'sets', 'reps', 'weight', 'order')
    list_filter = ('exercise__category',)
    search_fields = ('workout__name', 'exercise__name')
    ordering = ('workout', 'order')
