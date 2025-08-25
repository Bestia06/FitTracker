#!/usr/bin/env python
"""
Script para insertar datos de prueba en FitTracker
Ejecutar: python manage.py shell < seed_data.py
"""

import os
import sys
from datetime import date, timedelta
from decimal import Decimal

import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.accounts.models import User
from apps.habits.models import Habit
from apps.nutrition.models import Nutrition
from apps.stats.models import HabitProgress, NutritionStats, UserStats, WorkoutStats
from apps.workouts.models import Exercise, Workout
from django.contrib.auth import get_user_model

User = get_user_model()


def create_test_data():
    """Crear datos de prueba completos"""
    print("🌱 Iniciando inserción de datos de prueba...")

    # 1. Crear usuarios adicionales
    print("\n👥 Creando usuarios...")
    users = []

    # Usuario existente o crear uno nuevo
    try:
        user1 = User.objects.get(username="josep")
        print(f"✅ Usuario existente: {user1.username}")
    except User.DoesNotExist:
        user1 = User.objects.create_user(
            username="josep", email="josep@example.com", password="josep123"
        )
        print(f"✅ Usuario creado: {user1.username}")

    # Crear usuarios adicionales
    test_users = [
        {"username": "maria", "email": "maria@example.com", "password": "maria123"},
        {"username": "carlos", "email": "carlos@example.com", "password": "carlos123"},
        {"username": "ana", "email": "ana@example.com", "password": "ana123"},
        {"username": "pedro", "email": "pedro@example.com", "password": "pedro123"},
    ]

    for user_data in test_users:
        user, created = User.objects.get_or_create(
            username=user_data["username"],
            defaults={
                "email": user_data["email"],
            },
        )
        if created:
            user.set_password(user_data["password"])
            user.save()
            print(f"✅ Usuario creado: {user.username}")
        else:
            print(f"✅ Usuario existente: {user.username}")
        users.append(user)

    users.insert(0, user1)  # Agregar josep al inicio

    # 2. Crear hábitos
    print("\n🎯 Creando hábitos...")
    habits = []

    habit_data = [
        {
            "title": "Ejercicio diario",
            "kind": "workout",
            "target_value": 30.0,
            "color_hex": "#FF5733",
            "description": "Hacer ejercicio todos los días",
        },
        {
            "title": "Beber agua",
            "kind": "daily",
            "target_value": 8.0,
            "color_hex": "#33A8FF",
            "description": "Beber 8 vasos de agua al día",
        },
        {
            "title": "Meditar",
            "kind": "daily",
            "target_value": 15.0,
            "color_hex": "#33FF57",
            "description": "Meditar 15 minutos al día",
        },
        {
            "title": "Leer",
            "kind": "daily",
            "target_value": 30.0,
            "color_hex": "#F3FF33",
            "description": "Leer 30 minutos al día",
        },
        {
            "title": "Dormir bien",
            "kind": "daily",
            "target_value": 8.0,
            "color_hex": "#9B33FF",
            "description": "Dormir 8 horas al día",
        },
    ]

    for i, habit_info in enumerate(habit_data):
        for user in users[:3]:  # Solo para los primeros 3 usuarios
            habit = Habit.objects.create(
                user=user,
                title=f"{habit_info['title']} - {user.username}",
                kind=habit_info["kind"],
                target_value=habit_info["target_value"],
                color_hex=habit_info["color_hex"],
            )
            habits.append(habit)
            print(f"✅ Hábito creado: {habit.title}")

    # 3. Crear entradas nutricionales
    print("\n🍎 Creando entradas nutricionales...")

    nutrition_data = [
        {
            "name": "Manzana",
            "calories": 95,
            "protein_g": Decimal("0.50"),
            "carbs_g": Decimal("25.00"),
            "fat_g": Decimal("0.30"),
        },
        {
            "name": "Pollo a la plancha",
            "calories": 165,
            "protein_g": Decimal("31.00"),
            "carbs_g": Decimal("0.00"),
            "fat_g": Decimal("3.60"),
        },
        {
            "name": "Arroz integral",
            "calories": 216,
            "protein_g": Decimal("4.50"),
            "carbs_g": Decimal("45.00"),
            "fat_g": Decimal("1.80"),
        },
        {
            "name": "Ensalada de espinacas",
            "calories": 23,
            "protein_g": Decimal("2.90"),
            "carbs_g": Decimal("3.60"),
            "fat_g": Decimal("0.40"),
        },
        {
            "name": "Yogur griego",
            "calories": 59,
            "protein_g": Decimal("10.00"),
            "carbs_g": Decimal("3.60"),
            "fat_g": Decimal("0.40"),
        },
    ]

    for i, nutrition_info in enumerate(nutrition_data):
        for user in users[:3]:  # Solo para los primeros 3 usuarios
            nutrition = Nutrition.objects.create(
                user=user,
                name=nutrition_info["name"],
                date=date.today() - timedelta(days=i),
                calories=nutrition_info["calories"],
                protein_g=nutrition_info["protein_g"],
                carbs_g=nutrition_info["carbs_g"],
                fat_g=nutrition_info["fat_g"],
            )
            print(f"✅ Nutrición creada: {nutrition.name} para {user.username}")

    # 4. Crear entrenamientos
    print("\n🏋️ Creando entrenamientos...")

    workout_data = [
        {
            "duration_min": 45,
            "calories": 300,
            "status": "done",
            "notes": "Entrenamiento de cardio",
        },
        {
            "duration_min": 60,
            "calories": 400,
            "status": "done",
            "notes": "Entrenamiento de fuerza",
        },
        {
            "duration_min": 30,
            "calories": 200,
            "status": "done",
            "notes": "Yoga y estiramientos",
        },
        {
            "duration_min": 90,
            "calories": 600,
            "status": "done",
            "notes": "Entrenamiento completo",
        },
        {
            "duration_min": 20,
            "calories": 150,
            "status": "pending",
            "notes": "Entrenamiento pendiente",
        },
    ]

    for i, workout_info in enumerate(workout_data):
        for habit in habits[:3]:  # Solo para los primeros 3 hábitos
            workout = Workout.objects.create(
                habit=habit,
                date=date.today() - timedelta(days=i),
                duration_min=workout_info["duration_min"],
                calories=workout_info["calories"],
                status=workout_info["status"],
                notes=workout_info["notes"],
            )
            print(
                f"✅ Entrenamiento creado: {workout.notes} para {habit.user.username}"
            )

    # 5. Crear ejercicios
    print("\n💪 Creando ejercicios...")

    exercise_data = [
        {"name": "Push-ups", "sets": 3, "reps": 15, "notes": "Flexiones de pecho"},
        {"name": "Squats", "sets": 4, "reps": 20, "notes": "Sentadillas"},
        {
            "name": "Plank",
            "sets": 3,
            "duration_seconds": 60,
            "notes": "Plancha abdominal",
        },
        {"name": "Pull-ups", "sets": 3, "reps": 8, "notes": "Dominadas"},
        {"name": "Burpees", "sets": 3, "reps": 10, "notes": "Burpees completos"},
    ]

    for workout in Workout.objects.all()[:5]:  # Solo para los primeros 5 entrenamientos
        for exercise_info in exercise_data[:3]:  # Solo 3 ejercicios por entrenamiento
            exercise = Exercise.objects.create(
                workout=workout,
                name=exercise_info["name"],
                sets=exercise_info["sets"],
                reps=exercise_info.get("reps"),
                duration_seconds=exercise_info.get("duration_seconds"),
                notes=exercise_info["notes"],
            )
            print(f"✅ Ejercicio creado: {exercise.name} en {workout.habit.title}")

    # 6. Crear estadísticas
    print("\n📊 Creando estadísticas...")

    for user in users[:3]:
        # Estadísticas de usuario
        user_stats, created = UserStats.objects.get_or_create(
            user=user,
            defaults={
                "total_workouts": 5,
                "total_habits_completed": 12,
                "current_streak": 3,
                "total_calories_burned": 1500,
                "total_calories_consumed": 2000,
            },
        )
        if created:
            print(f"✅ Estadísticas de usuario creadas para {user.username}")

        # Progreso de hábitos
        for habit in Habit.objects.filter(user=user)[:3]:
            for i in range(7):  # Últimos 7 días
                progress, created = HabitProgress.objects.get_or_create(
                    habit=habit,
                    date=date.today() - timedelta(days=i),
                    defaults={
                        "completed": i % 2 == 0,  # Alternar completado
                        "value": habit.target_value if i % 2 == 0 else 0,
                    },
                )
            print(f"✅ Progreso de hábito creado para {habit.title}")

        # Estadísticas de entrenamiento
        workout_stats, created = WorkoutStats.objects.get_or_create(
            user=user,
            date=date.today(),
            defaults={
                "total_duration": 180,
                "total_calories_burned": 450,
                "workout_count": 3,
            },
        )
        if created:
            print(f"✅ Estadísticas de entrenamiento creadas para {user.username}")

        # Estadísticas de nutrición
        nutrition_stats, created = NutritionStats.objects.get_or_create(
            user=user,
            date=date.today(),
            defaults={
                "total_calories": 1800,
                "total_protein": 120,
                "total_carbs": 200,
                "total_fat": 60,
                "meal_count": 4,
            },
        )
        if created:
            print(f"✅ Estadísticas de nutrición creadas para {user.username}")

    print("\n🎉 ¡Datos de prueba insertados exitosamente!")
    print("\n📋 Resumen de datos creados:")
    print(f"   👥 Usuarios: {User.objects.count()}")
    print(f"   🎯 Hábitos: {Habit.objects.count()}")
    print(f"   🍎 Nutrición: {Nutrition.objects.count()}")
    print(f"   🏋️ Entrenamientos: {Workout.objects.count()}")
    print(f"   💪 Ejercicios: {Exercise.objects.count()}")
    print(f"   📊 Estadísticas de usuario: {UserStats.objects.count()}")
    print(f"   📈 Progreso de hábitos: {HabitProgress.objects.count()}")
    print(f"   🏃 Estadísticas de entrenamiento: {WorkoutStats.objects.count()}")
    print(f"   🍽️ Estadísticas de nutrición: {NutritionStats.objects.count()}")


if __name__ == "__main__":
    create_test_data()
