from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Serializer para hábitos"""
    
    class Meta:
        model = Habit
        fields = [
            'id', 'title', 'kind', 'target_value', 'color_hex',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

