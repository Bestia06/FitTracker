# nutrition/admin.py
from django.contrib import admin
from .models import Nutrition

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'date', 'calories', 'protein_g', 'carbs_g', 'fat_g']
    list_filter = ['date', 'created_at']
    search_fields = ['name', 'user__username']
    ordering = ['-date', '-created_at']
    date_hierarchy = 'date'