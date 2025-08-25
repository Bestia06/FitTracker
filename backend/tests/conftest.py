"""
Configuración de pytest para FitTracker
"""

import pytest
from apps.habits.models import Habit
from apps.nutrition.models import Nutrition
from apps.stats.models import UserStats
from apps.workouts.models import Workout
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def api_client():
    """Fixture para cliente de API"""
    return APIClient()


@pytest.fixture
def user():
    """Fixture para crear un usuario de prueba"""
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpass123",
        first_name="Test",
        last_name="User",
    )


@pytest.fixture
def authenticated_client(api_client, user):
    """Fixture para cliente autenticado"""
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def habit(user):
    """Fixture para crear un hábito de prueba"""
    return Habit.objects.create(
        title="Ejercicio diario",
        kind="daily",
        target_value=30.0,
        color_hex="#FF5733",
        user=user,
    )


@pytest.fixture
def nutrition_entry(user):
    """Fixture para crear una entrada nutricional de prueba"""
    from datetime import date
    from decimal import Decimal

    return Nutrition.objects.create(
        name="Manzana",
        date=date.today(),
        calories=95,
        protein_g=Decimal("0.50"),
        carbs_g=Decimal("25.00"),
        fat_g=Decimal("0.30"),
        user=user,
    )


@pytest.fixture
def workout(user):
    """Fixture para crear un entrenamiento de prueba"""
    from datetime import date

    return Workout.objects.create(
        name="Entrenamiento de fuerza",
        date=date.today(),
        workout_type="strength",
        calories=300,
        duration_minutes=60,
        user=user,
    )


@pytest.fixture
def user_stats(user):
    """Fixture para crear estadísticas de usuario de prueba"""
    return UserStats.objects.create(
        user=user, total_workouts=10, total_habits_completed=25, current_streak=5
    )


@pytest.fixture
def sample_users():
    """Fixture para crear múltiples usuarios de prueba"""
    users = []
    for i in range(3):
        user = User.objects.create_user(
            username=f"user{i}", email=f"user{i}@example.com", password="testpass123"
        )
        users.append(user)
    return users


@pytest.fixture
def sample_habits(user):
    """Fixture para crear múltiples hábitos de prueba"""
    habits = []
    habit_data = [
        {"title": "Ejercicio diario", "kind": "daily", "target_value": 30.0},
        {"title": "Beber agua", "kind": "daily", "target_value": 8.0},
        {"title": "Leer", "kind": "daily", "target_value": 30.0},
    ]

    for data in habit_data:
        habit = Habit.objects.create(**data, color_hex="#FF5733", user=user)
        habits.append(habit)
    return habits
