from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.accounts.models import User


class Workout(models.Model):
    """Workout model for tracking exercise sessions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    duration = models.DurationField(help_text="Workout duration in minutes")
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.date})"


class Exercise(models.Model):
    """Exercise model for individual exercises"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('strength', 'Strength Training'),
            ('cardio', 'Cardio'),
            ('flexibility', 'Flexibility'),
            ('balance', 'Balance'),
            ('sports', 'Sports'),
        ]
    )
    muscle_groups = models.JSONField(default=list, blank=True)
    equipment_needed = models.JSONField(default=list, blank=True)
    instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    """Junction model for exercises in workouts"""
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(default=1)
    reps = models.PositiveIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    distance = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.workout.name} - {self.exercise.name}"
