from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.accounts.models import User


class Food(models.Model):
    """Food model for tracking nutritional information"""
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, blank=True)
    calories_per_100g = models.PositiveIntegerField()
    protein_per_100g = models.DecimalField(max_digits=5, decimal_places=2)
    carbs_per_100g = models.DecimalField(max_digits=5, decimal_places=2)
    fat_per_100g = models.DecimalField(max_digits=5, decimal_places=2)
    fiber_per_100g = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sugar_per_100g = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sodium_per_100g = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['name', 'brand']

    def __str__(self):
        return f"{self.brand} - {self.name}" if self.brand else self.name


class Meal(models.Model):
    """Meal model for tracking daily meals"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
    name = models.CharField(max_length=100)
    meal_type = models.CharField(
        max_length=20,
        choices=[
            ('breakfast', 'Breakfast'),
            ('lunch', 'Lunch'),
            ('dinner', 'Dinner'),
            ('snack', 'Snack'),
        ]
    )
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', 'meal_type']

    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.date})"


class MealFood(models.Model):
    """Junction model for foods in meals"""
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='foods')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity_grams = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField(blank=True)

    @property
    def calories(self):
        return (self.food.calories_per_100g * self.quantity_grams) / 100

    @property
    def protein(self):
        return (self.food.protein_per_100g * self.quantity_grams) / 100

    @property
    def carbs(self):
        return (self.food.carbs_per_100g * self.quantity_grams) / 100

    @property
    def fat(self):
        return (self.food.fat_per_100g * self.quantity_grams) / 100

    def __str__(self):
        return f"{self.meal.name} - {self.food.name} ({self.quantity_grams}g)"


class NutritionGoal(models.Model):
    """Nutrition goals for users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nutrition_goals')
    daily_calories = models.PositiveIntegerField()
    daily_protein = models.DecimalField(max_digits=5, decimal_places=2)
    daily_carbs = models.DecimalField(max_digits=5, decimal_places=2)
    daily_fat = models.DecimalField(max_digits=5, decimal_places=2)
    daily_fiber = models.DecimalField(max_digits=5, decimal_places=2, default=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Nutrition Goals"
