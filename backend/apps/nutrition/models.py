from decimal import Decimal

from apps.accounts.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Nutrition(models.Model):
    """
    Modelo para registro nutricional
    """

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="nutrition_entries"
    )
    date = models.DateField()
    name = models.CharField(max_length=200, help_text="Nombre del alimento")
    calories = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    # Usar DecimalField para precisión en macronutrientes
    protein_g = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
        help_text="Proteína en gramos",
    )
    carbs_g = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
        help_text="Carbohidratos en gramos",
    )
    fat_g = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
        help_text="Grasa en gramos",
    )

    # Campos adicionales útiles
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]
        indexes = [
            models.Index(fields=["user", "-date"]),
            models.Index(fields=["date"]),
        ]
        verbose_name = "Nutrition Entry"
        verbose_name_plural = "Nutrition Entries"

    def __str__(self):
        return f"{self.name} - {self.date} ({self.user.username})"

    @property
    def total_macros(self):
        """Calcula total de macronutrientes"""
        return {
            "protein": float(self.protein_g),
            "carbs": float(self.carbs_g),
            "fat": float(self.fat_g),
            "total_grams": float(self.protein_g + self.carbs_g + self.fat_g),
        }
