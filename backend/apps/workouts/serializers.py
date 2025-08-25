# workout/serializers.py
from rest_framework import serializers
from .models import Workout, Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Exercise"""
    class Meta:
        model = Exercise
        fields = [
            'id', 'name', 'sets', 'reps', 'weight_kg', 
            'duration_seconds', 'rest_seconds', 'notes'
        ]

class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Workout"""
    user = serializers.StringRelatedField(read_only=True)
    exercises = ExerciseSerializer(many=True, read_only=True)
    calories_per_minute = serializers.ReadOnlyField()
    
    class Meta:
        model = Workout
        fields = [
            'id', 'user', 'date', 'name', 'workout_type', 'calories', 
            'duration_minutes', 'notes', 'exercises', 'calories_per_minute',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class WorkoutCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear workout con ejercicios"""
    exercises = ExerciseSerializer(many=True, required=False)
    
    class Meta:
        model = Workout
        fields = [
            'date', 'name', 'workout_type', 'calories', 
            'duration_minutes', 'notes', 'exercises'
        ]
    
    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises', [])
        validated_data['user'] = self.context['request'].user
        workout = Workout.objects.create(**validated_data)
        
        for exercise_data in exercises_data:
            Exercise.objects.create(workout=workout, **exercise_data)
        
        return workout