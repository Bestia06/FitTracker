from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Habit"""
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Habit
        fields = ['id', 'user', 'title', 'kind', 'target_value', 'color_hex', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

