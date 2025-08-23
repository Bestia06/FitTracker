from django.contrib import admin
from .models import Food, Meal, MealFood, NutritionGoal


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'calories_per_100g', 'protein_per_100g', 'carbs_per_100g', 'fat_per_100g')
    list_filter = ('brand',)
    search_fields = ('name', 'brand', 'barcode')
    readonly_fields = ('created_at',)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'meal_type', 'date')
    list_filter = ('meal_type', 'date', 'user')
    search_fields = ('name', 'user__username')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')


@admin.register(MealFood)
class MealFoodAdmin(admin.ModelAdmin):
    list_display = ('meal', 'food', 'quantity_grams', 'calories', 'protein', 'carbs', 'fat')
    list_filter = ('meal__meal_type', 'food__brand')
    search_fields = ('meal__name', 'food__name')


@admin.register(NutritionGoal)
class NutritionGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'daily_calories', 'daily_protein', 'daily_carbs', 'daily_fat')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
