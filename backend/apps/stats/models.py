from django.db import models
from apps.accounts.models import User
from apps.habits.models import Habit


class UserStats(models.Model):
    """
    Estadísticas generales del usuario
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='stats'
    )
    total_workouts = models.IntegerField(default=0)
    total_habits_completed = models.IntegerField(default=0)
    total_calories_consumed = models.FloatField(default=0.0)
    total_calories_burned = models.FloatField(default=0.0)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_activity_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Estadística de Usuario"
        verbose_name_plural = "Estadísticas de Usuario"

    def __str__(self):
        return f"Stats de {self.user.username}"


class HabitProgress(models.Model):
    """
    Progreso de hábitos específicos
    """
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, related_name='progress'
    )
    date = models.DateField()
    completed = models.BooleanField(default=False)
    value = models.FloatField(default=0.0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['habit', 'date']
        ordering = ['-date']
        verbose_name = "Progreso de Hábito"
        verbose_name_plural = "Progresos de Hábitos"

    def __str__(self):
        return f"{self.habit.title} - {self.date}"


class WorkoutStats(models.Model):
    """
    Estadísticas específicas de entrenamientos
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='workout_stats'
    )
    date = models.DateField()
    total_duration = models.IntegerField(default=0)  # en minutos
    total_calories_burned = models.FloatField(default=0.0)
    workout_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'date']
        ordering = ['-date']
        verbose_name = "Estadística de Entrenamiento"
        verbose_name_plural = "Estadísticas de Entrenamientos"

    def __str__(self):
        return f"Workout Stats - {self.user.username} - {self.date}"


class NutritionStats(models.Model):
    """
    Estadísticas específicas de nutrición
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='nutrition_stats'
    )
    date = models.DateField()
    total_calories = models.FloatField(default=0.0)
    total_protein = models.FloatField(default=0.0)
    total_carbs = models.FloatField(default=0.0)
    total_fat = models.FloatField(default=0.0)
    total_fiber = models.FloatField(default=0.0)
    meal_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'date']
        ordering = ['-date']
        verbose_name = "Estadística de Nutrición"
        verbose_name_plural = "Estadísticas de Nutrición"

    def __str__(self):
        return f"Nutrition Stats - {self.user.username} - {self.date}"
