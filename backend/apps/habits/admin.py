from django.contrib import admin
from .models import Habit, HabitLog, HabitStreak


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'category', 'frequency', 'target_count', 'is_active')
    list_filter = ('category', 'frequency', 'is_active', 'user')
    search_fields = ('name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(HabitLog)
class HabitLogAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date', 'completed_count')
    list_filter = ('date', 'habit__category')
    search_fields = ('habit__name', 'habit__user__username')
    date_hierarchy = 'date'
    readonly_fields = ('created_at',)


@admin.register(HabitStreak)
class HabitStreakAdmin(admin.ModelAdmin):
    list_display = ('habit', 'current_streak', 'longest_streak', 'last_completed_date')
    list_filter = ('habit__category',)
    search_fields = ('habit__name', 'habit__user__username')
    readonly_fields = ('updated_at',)
