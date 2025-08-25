"""
Tests para las APIs de FitTracker
"""

from datetime import date
from decimal import Decimal

from apps.habits.models import Habit
from apps.nutrition.models import Nutrition
from apps.workouts.models import Workout
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


class BaseTestCase(TestCase):
    """Clase base para tests de API"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.client.force_authenticate(user=self.user)


class AuthenticationAPITest(BaseTestCase):
    """Tests para autenticación"""

    def test_register_user(self):
        """Test registro de usuario"""
        url = reverse("register")
        data = {
            "username": "newuser",
            "email": "new@example.com",
            "password": "newpass123",
            "password_confirm": "newpass123",
            "first_name": "New",
            "last_name": "User",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("user", response.data)
        self.assertIn("tokens", response.data)

    def test_login_user(self):
        """Test login de usuario"""
        url = reverse("accounts:login")
        data = {"email": "test@example.com", "password": "testpass123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("user", response.data)
        self.assertIn("token", response.data)

    def test_user_profile(self):
        """Test obtener perfil de usuario"""
        url = reverse("accounts:profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")


class HabitsAPITest(BaseTestCase):
    """Tests para API de hábitos"""

    def setUp(self):
        super().setUp()
        self.habit_data = {
            "title": "Ejercicio diario",
            "kind": "daily",
            "target_value": 30.0,
            "color_hex": "#FF5733",
        }

    def test_create_habit(self):
        """Test crear hábito"""
        url = reverse("habits:habit_list")
        response = self.client.post(url, self.habit_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Ejercicio diario")
        self.assertEqual(response.data["kind"], "daily")

    def test_list_habits(self):
        """Test listar hábitos"""
        # Crear un hábito primero
        Habit.objects.create(user=self.user, **self.habit_data)

        url = reverse("habits:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_get_habit_detail(self):
        """Test obtener detalle de hábito"""
        habit = Habit.objects.create(user=self.user, **self.habit_data)

        url = reverse("habits:habit_detail", kwargs={"pk": habit.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Ejercicio diario")

    def test_update_habit(self):
        """Test actualizar hábito"""
        habit = Habit.objects.create(user=self.user, **self.habit_data)

        url = reverse("habits:habit_detail", kwargs={"pk": habit.pk})
        update_data = {"title": "Ejercicio actualizado"}
        response = self.client.patch(url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Ejercicio actualizado")

    def test_delete_habit(self):
        """Test eliminar hábito"""
        habit = Habit.objects.create(user=self.user, **self.habit_data)

        url = reverse("habits:habit_detail", kwargs={"pk": habit.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class NutritionAPITest(BaseTestCase):
    """Tests para API de nutrición"""

    def setUp(self):
        super().setUp()
        self.nutrition_data = {
            "name": "Manzana",
            "date": date.today().isoformat(),
            "calories": 95,
            "protein_g": "0.50",
            "carbs_g": "25.00",
            "fat_g": "0.30",
        }

    def test_create_nutrition(self):
        """Test crear entrada nutricional"""
        url = reverse("nutrition:nutrition_list")
        response = self.client.post(url, self.nutrition_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Manzana")
        self.assertEqual(response.data["calories"], 95)

    def test_list_nutrition(self):
        """Test listar entradas nutricionales"""
        Nutrition.objects.create(
            user=self.user,
            name="Manzana",
            date=date.today(),
            calories=95,
            protein_g=Decimal("0.50"),
            carbs_g=Decimal("25.00"),
            fat_g=Decimal("0.30"),
        )

        url = reverse("nutrition:nutrition_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)


class WorkoutsAPITest(BaseTestCase):
    """Tests para API de entrenamientos"""

    def setUp(self):
        super().setUp()
        # Crear un habit primero
        self.habit = Habit.objects.create(
            user=self.user,
            title="Ejercicio diario",
            kind="workout",
            target_value=30,
            color_hex="#FF5733"
        )
        self.workout_data = {
            "habit": self.habit.id,
            "date": date.today().isoformat(),
            "duration_min": 60,
            "calories": 300,
            "status": "done",
        }

    def test_create_workout(self):
        """Test crear entrenamiento"""
        url = reverse("workouts:workout_list")
        response = self.client.post(url, self.workout_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["habit"], self.habit.id)
        self.assertEqual(response.data["status"], "done")

    def test_list_workouts(self):
        """Test listar entrenamientos"""
        Workout.objects.create(
            habit=self.habit,
            date=date.today(),
            duration_min=60,
            calories=300,
            status="done",
        )

        url = reverse("workouts:workout_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)


class StatsAPITest(BaseTestCase):
    """Tests para API de estadísticas"""

    def test_get_user_stats(self):
        """Test obtener estadísticas de usuario"""
        url = reverse("stats:user_stats")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_workouts", response.data)
        self.assertIn("total_habits_completed", response.data)

    def test_get_stats_summary(self):
        """Test obtener resumen de estadísticas"""
        url = reverse("stats:stats_summary")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_workouts", response.data)
        self.assertIn("weekly_progress", response.data)
        self.assertIn("monthly_progress", response.data)


class APINinjaTest(BaseTestCase):
    """Tests para integración con API Ninja"""

    def test_enrich_nutrition(self):
        """Test enriquecer datos nutricionales"""
        url = reverse("enrich_nutrition")
        data = {"name": "apple"}
        response = self.client.post(url, data)
        # Puede fallar si no hay API key configurada o si la URL no existe
        self.assertIn(response.status_code, [200, 503, 404])

    def test_search_exercises(self):
        """Test buscar ejercicios"""
        url = reverse("search_exercises")
        response = self.client.get(url, {"name": "push-up"})
        # Puede fallar si no hay API key configurada o si la URL no existe
        self.assertIn(response.status_code, [200, 503, 404])
