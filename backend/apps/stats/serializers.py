from rest_framework import serializers
from .models import UserStats, HabitProgress, WorkoutStats, NutritionStats


class UserStatsSerializer(serializers.ModelSerializer):
    """Serializer para estadísticas generales del usuario"""
    
    class Meta:
        model = UserStats
        fields = [
            'id', 'total_workouts', 'total_habits_completed',
            'total_calories_consumed', 'total_calories_burned',
            'current_streak', 'longest_streak', 'last_activity_date',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class HabitProgressSerializer(serializers.ModelSerializer):
    """Serializer para progreso de hábitos"""
    habit_title = serializers.CharField(source='habit.title', read_only=True)
    
    class Meta:
        model = HabitProgress
        fields = [
            'id', 'habit', 'habit_title', 'date', 'completed',
            'value', 'notes', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class WorkoutStatsSerializer(serializers.ModelSerializer):
    """Serializer para estadísticas de entrenamientos"""
    
    class Meta:
        model = WorkoutStats
        fields = [
            'id', 'date', 'total_duration', 'total_calories_burned',
            'workout_count', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class NutritionStatsSerializer(serializers.ModelSerializer):
    """Serializer para estadísticas de nutrición"""
    
    class Meta:
        model = NutritionStats
        fields = [
            'id', 'date', 'total_calories', 'total_protein',
            'total_carbs', 'total_fat', 'total_fiber',
            'meal_count', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class StatsSummarySerializer(serializers.Serializer):
    """Serializer para resumen de estadísticas"""
    total_workouts = serializers.IntegerField()
    total_habits_completed = serializers.IntegerField()
    total_calories_consumed = serializers.FloatField()
    total_calories_burned = serializers.FloatField()
    current_streak = serializers.IntegerField()
    longest_streak = serializers.IntegerField()
    weekly_progress = serializers.DictField()
    monthly_progress = serializers.DictField()
