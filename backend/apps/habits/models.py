from django.db import models
from django.core.validators import RegexValidator

from apps.accounts.models import User


class Habit(models.Model):
    """
    Modelo para hábitos de usuario
    """
    HABIT_KINDS = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('counter', 'Counter'),
        ('timer', 'Timer'),
    ]
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='habits'
    )
    title = models.CharField(max_length=200)
    kind = models.CharField(max_length=20, choices=HABIT_KINDS)
    target_value = models.FloatField(help_text="Valor objetivo del hábito")
    
    # Validador para color hexadecimal
    color_validator = RegexValidator(
        regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
        message='Color debe ser formato hex válido (#FFFFFF o #FFF)'
    )
    color_hex = models.CharField(max_length=7, validators=[color_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"