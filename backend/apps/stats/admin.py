from django.contrib import admin
from .models import BodyMeasurement, FitnessGoal, ProgressLog


@admin.register(BodyMeasurement)
class BodyMeasurementAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'weight', 'body_fat_percentage', 'muscle_mass')
    list_filter = ('date', 'user')
    search_fields = ('user__username', 'user__email')
    date_hierarchy = 'date'
    readonly_fields = ('created_at',)


@admin.register(FitnessGoal)
class FitnessGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'goal_type', 'target_value', 'current_value', 'is_completed')
    list_filter = ('goal_type', 'is_completed', 'user')
    search_fields = ('title', 'user__username')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ProgressLog)
class ProgressLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal', 'value', 'date')
    list_filter = ('date', 'goal__goal_type')
    search_fields = ('goal__title', 'user__username')
    date_hierarchy = 'date'
    readonly_fields = ('created_at',)
