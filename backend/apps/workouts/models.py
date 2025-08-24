from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

from apps.accounts.models import User

class Workout(models.Model):
    """
    Modelo para registro de entrenamientos
    """
    WORKOUT_TYPES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength Training'),
        ('flexibility', 'Flexibility'),
        ('sports', 'Sports'),
        ('other', 'Other'),
    ]
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField()
    name = models.CharField(max_length=200, help_text="Nombre del entrenamiento")
    workout_type = models.CharField(max_length=20, choices=WORKOUT_TYPES, default='other')
    
    # Calorías quemadas
    calories = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        help_text="Calorías quemadas durante el entrenamiento"
    )
    
    # Duración del entrenamiento
    duration_minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Duración en minutos"
    )
    
    # Notas adicionales
    notes = models.TextField(blank=True, help_text="Notas adicionales del entrenamiento")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
        indexes = [
            models.Index(fields=['user', '-date']),
            models.Index(fields=['date']),
            models.Index(fields=['workout_type']),
        ]
    
    def __str__(self):
        return f"{self.name} - {self.date} ({self.user.username})"
    
    @property
    def calories_per_minute(self):
        """Calcula calorías por minuto"""
        return round(self.calories / self.duration_minutes, 2) if self.duration_minutes > 0 else 0

# Modelo adicional para ejercicios específicos dentro de un workout
class Exercise(models.Model):
    """
    Modelo para ejercicios específicos dentro de un entrenamiento
    """
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=200)
    sets = models.PositiveIntegerField(default=1)
    reps = models.PositiveIntegerField(null=True, blank=True)
    weight_kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    rest_seconds = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.name} - {self.workout.name}"