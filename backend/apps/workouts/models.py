from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

from apps.habits.models import Habit


class Workout(models.Model):
    """
    Modelo para registro de entrenamientos
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('skipped', 'Skipped'),
    ]
    
    id = models.AutoField(primary_key=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField()
    duration_min = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Duración en minutos"
    )
    distancia_km = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.00'))],
        help_text="Distancia en kilómetros"
    )
    calories = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        help_text="Calorías quemadas"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Estado del entrenamiento"
    )
    notes = models.TextField(blank=True, help_text="Notas adicionales")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
        indexes = [
            models.Index(fields=['habit', '-date']),
            models.Index(fields=['date']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"{self.habit.title} - {self.date} ({self.status})"
    
    @property
    def calories_per_minute(self):
        """Calcula calorías por minuto"""
        return round(self.calories / self.duration_min, 2) if self.duration_min > 0 else 0


class Exercise(models.Model):
    """
    Modelo para ejercicios específicos dentro de un entrenamiento
    """
    id = models.AutoField(primary_key=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=200, help_text="Nombre del ejercicio")
    sets = models.PositiveIntegerField(default=1, help_text="Número de series")
    reps = models.PositiveIntegerField(null=True, blank=True, help_text="Repeticiones por serie")
    weight_kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(Decimal('0.00'))],
        help_text="Peso en kilogramos"
    )
    duration_seconds = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        help_text="Duración en segundos (para ejercicios de tiempo)"
    )
    rest_seconds = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        help_text="Tiempo de descanso en segundos"
    )
    notes = models.TextField(blank=True, help_text="Notas adicionales")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['workout']),
            models.Index(fields=['name']),
        ]
    
    def __str__(self):
        return f"{self.name} - {self.workout.habit.title}"
    
    @property
    def total_duration(self):
        """Calcula duración total incluyendo descanso"""
        if self.duration_seconds:
            return self.duration_seconds
        if self.rest_seconds:
            return self.rest_seconds
        return 0