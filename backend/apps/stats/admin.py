from django.contrib import admin

from .models import HabitProgress, NutritionStats, UserStats, WorkoutStats


@admin.register(UserStats)
class UserStatsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "total_workouts",
        "total_habits_completed",
        "current_streak",
    )
    list_filter = ("current_streak", "longest_streak")
    search_fields = ("user__username", "user__email")
    readonly_fields = ("created_at", "updated_at")


@admin.register(HabitProgress)
class HabitProgressAdmin(admin.ModelAdmin):
    list_display = ("habit", "date", "completed", "value")
    list_filter = ("completed", "date", "habit__kind")
    search_fields = ("habit__title", "notes")
    date_hierarchy = "date"
    readonly_fields = ("created_at",)


@admin.register(WorkoutStats)
class WorkoutStatsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date",
        "total_duration",
        "total_calories_burned",
        "workout_count",
    )
    list_filter = ("date", "workout_count")
    search_fields = ("user__username", "user__email")
    date_hierarchy = "date"
    readonly_fields = ("created_at",)


@admin.register(NutritionStats)
class NutritionStatsAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "total_calories", "total_protein", "meal_count")
    list_filter = ("date", "meal_count")
    search_fields = ("user__username", "user__email")
    date_hierarchy = "date"
    readonly_fields = ("created_at",)
