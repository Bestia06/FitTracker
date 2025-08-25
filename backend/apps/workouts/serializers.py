# workout/serializers.py
from rest_framework import serializers

from .models import Workout, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Exercise"""
    
    class Meta:
        model = Exercise
        fields = [
            'id', 'name', 'sets', 'reps', 'weight_kg', 
            'duration_seconds', 'rest_seconds', 'notes',
            'total_duration', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Workout"""

    habit_title = serializers.CharField(
        source='habit.title', read_only=True
    )
    user_username = serializers.CharField(
        source='habit.user.username', read_only=True
    )
    calories_per_minute = serializers.ReadOnlyField()
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = [
            "id",
            "habit",
            "habit_title",
            "user_username",
            "date",
            "duration_min",
            "distancia_km",
            "calories",
            "status",
            "notes",
            "calories_per_minute",
            "exercises",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        # El usuario se obtiene del habit
        return super().create(validated_data)


class WorkoutCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear workout con ejercicios"""
    exercises = ExerciseSerializer(many=True, required=False)
    
    class Meta:
        model = Workout
        fields = [
            'habit', 'date', 'duration_min', 'distancia_km',
            'calories', 'status', 'notes', 'exercises'
        ]
    
    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises', [])
        workout = Workout.objects.create(**validated_data)
        
        for exercise_data in exercises_data:
            Exercise.objects.create(workout=workout, **exercise_data)
        
        return workout