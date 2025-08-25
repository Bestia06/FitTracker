"""
Tests para los modelos de FitTracker
"""

from datetime import date
from decimal import Decimal

from apps.habits.models import Habit
from apps.nutrition.models import Nutrition
from apps.stats.models import HabitProgress, NutritionStats, UserStats, WorkoutStats
from apps.workouts.models import Workout
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserModelTest(TestCase):
    """Tests para el modelo User"""

    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass123",
            "first_name": "Test",
            "last_name": "User",
        }

    def test_create_user(self):
        """Test crear usuario"""
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("testpass123"))

    def test_user_str(self):
        """Test string representation del usuario"""
        user = User.objects.create_user(**self.user_data)
        expected = f"{user.username} ({user.email})"
        self.assertEqual(str(user), expected)


class HabitModelTest(TestCase):
    """Tests para el modelo Habit"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.habit_data = {
            "title": "Ejercicio diario",
            "kind": "daily",
            "target_value": 30.0,
            "color_hex": "#FF5733",
            "user": self.user,
        }

    def test_create_habit(self):
        """Test crear hábito"""
        habit = Habit.objects.create(**self.habit_data)
        self.assertEqual(habit.title, "Ejercicio diario")
        self.assertEqual(habit.kind, "daily")
        self.assertEqual(habit.target_value, 30.0)
        self.assertEqual(habit.color_hex, "#FF5733")
        self.assertEqual(habit.user, self.user)

    def test_habit_str(self):
        """Test string representation del hábito"""
        habit = Habit.objects.create(**self.habit_data)
        expected = f"{habit.title} - {habit.user.username}"
        self.assertEqual(str(habit), expected)


class NutritionModelTest(TestCase):
    """Tests para el modelo Nutrition"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.nutrition_data = {
            "name": "Manzana",
            "date": date.today(),
            "calories": 95,
            "protein_g": Decimal("0.50"),
            "carbs_g": Decimal("25.00"),
            "fat_g": Decimal("0.30"),
            "user": self.user,
        }

    def test_create_nutrition(self):
        """Test crear entrada nutricional"""
        nutrition = Nutrition.objects.create(**self.nutrition_data)
        self.assertEqual(nutrition.name, "Manzana")
        self.assertEqual(nutrition.calories, 95)
        self.assertEqual(nutrition.protein_g, Decimal("0.50"))
        self.assertEqual(nutrition.user, self.user)

    def test_total_macros_property(self):
        """Test propiedad total_macros"""
        nutrition = Nutrition.objects.create(**self.nutrition_data)
        macros = nutrition.total_macros
        self.assertEqual(macros["protein"], 0.5)
        self.assertEqual(macros["carbs"], 25.0)
        self.assertEqual(macros["fat"], 0.3)


class WorkoutModelTest(TestCase):
    """Tests para el modelo Workout"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.habit = Habit.objects.create(
            user=self.user,
            title="Ejercicio diario",
            kind="workout",
            target_value=30,
            color_hex="#FF5733",
        )
        self.workout_data = {
            "habit": self.habit,
            "date": date.today(),
            "duration_min": 60,
            "calories": 300,
            "status": "done",
        }

    def test_create_workout(self):
        """Test crear entrenamiento"""
        workout = Workout.objects.create(**self.workout_data)
        self.assertEqual(workout.habit, self.habit)
        self.assertEqual(workout.status, "done")
        self.assertEqual(workout.duration_min, 60)
        self.assertEqual(workout.calories, 300)

    def test_calories_per_minute_property(self):
        """Test propiedad calories_per_minute"""
        workout = Workout.objects.create(**self.workout_data)
        self.assertEqual(workout.calories_per_minute, 5.0)


class StatsModelTest(TestCase):
    """Tests para los modelos de estadísticas"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.habit = Habit.objects.create(
            title="Ejercicio diario",
            kind="daily",
            target_value=30.0,
            color_hex="#FF5733",
            user=self.user,
        )

    def test_user_stats(self):
        """Test crear estadísticas de usuario"""
        user_stats = UserStats.objects.create(
            user=self.user,
            total_workouts=10,
            total_habits_completed=25,
            current_streak=5,
        )
        self.assertEqual(user_stats.total_workouts, 10)
        self.assertEqual(user_stats.total_habits_completed, 25)
        self.assertEqual(user_stats.current_streak, 5)

    def test_habit_progress(self):
        """Test crear progreso de hábito"""
        progress = HabitProgress.objects.create(
            habit=self.habit, date=date.today(), completed=True, value=30.0
        )
        self.assertEqual(progress.habit, self.habit)
        self.assertTrue(progress.completed)
        self.assertEqual(progress.value, 30.0)

    def test_workout_stats(self):
        """Test crear estadísticas de entrenamiento"""
        workout_stats = WorkoutStats.objects.create(
            user=self.user,
            date=date.today(),
            total_duration=120,
            total_calories_burned=600.0,
            workout_count=2,
        )
        self.assertEqual(workout_stats.user, self.user)
        self.assertEqual(workout_stats.total_duration, 120)
        self.assertEqual(workout_stats.total_calories_burned, 600.0)
        self.assertEqual(workout_stats.workout_count, 2)

    def test_nutrition_stats(self):
        """Test crear estadísticas de nutrición"""
        nutrition_stats = NutritionStats.objects.create(
            user=self.user,
            date=date.today(),
            total_calories=2000.0,
            total_protein=150.0,
            total_carbs=200.0,
            total_fat=70.0,
            meal_count=4,
        )
        self.assertEqual(nutrition_stats.user, self.user)
        self.assertEqual(nutrition_stats.total_calories, 2000.0)
        self.assertEqual(nutrition_stats.total_protein, 150.0)
        self.assertEqual(nutrition_stats.meal_count, 4)
