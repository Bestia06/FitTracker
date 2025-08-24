"""
URLs for nutrition app.
"""

from django.urls import path

from . import views

urlpatterns = [
    # API Ninja endpoints
    path("api-ninja/nutrition/", views.get_nutrition_info, name="nutrition_info"),
    path("api-ninja/exercise/", views.get_exercise_info, name="exercise_info"),
    path(
        "api-ninja/exercises-by-muscle/",
        views.get_exercises_by_muscle,
        name="exercises_by_muscle",
    ),
]
