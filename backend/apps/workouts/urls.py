"""
URLs for workouts app.
"""

from django.urls import path

from . import api_views

app_name = "workouts"

urlpatterns = [
    # Entrenamientos
    path("", api_views.WorkoutListCreateView.as_view(), name="workout_list"),
    path("<int:pk>/", api_views.WorkoutDetailView.as_view(), name="workout_detail"),
]
