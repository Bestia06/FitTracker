from django.contrib import admin
from .models import Habit

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'kind', 'target_value', 'color_hex', 'created_at']
    list_filter = ['kind', 'created_at']
    search_fields = ['title', 'user__username']
    ordering = ['-created_at']