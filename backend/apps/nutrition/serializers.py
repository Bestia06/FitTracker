# nutrition/serializers.py
from rest_framework import serializers

from .models import Nutrition


class NutritionSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Nutrition"""

    user = serializers.StringRelatedField(read_only=True)
    total_macros = serializers.ReadOnlyField()

    class Meta:
        model = Nutrition
        fields = [
            "id",
            "user",
            "date",
            "name",
            "calories",
            "protein_g",
            "carbs_g",
            "fat_g",
            "total_macros",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
