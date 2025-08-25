"""
URLs for stats app.
"""

from django.urls import path

from . import api_views

app_name = "stats"

urlpatterns = [
    # Estadísticas generales del usuario
    path("user/", api_views.UserStatsView.as_view(), name="user_stats"),
    # Progreso de hábitos
    path(
        "habits/progress/",
        api_views.HabitProgressListCreateView.as_view(),
        name="habit_progress_list",
    ),
    path(
        "habits/progress/<int:pk>/",
        api_views.HabitProgressDetailView.as_view(),
        name="habit_progress_detail",
    ),
    # Estadísticas de entrenamientos
    path(
        "workouts/",
        api_views.WorkoutStatsListCreateView.as_view(),
        name="workout_stats_list",
    ),
    path(
        "workouts/<int:pk>/",
        api_views.WorkoutStatsDetailView.as_view(),
        name="workout_stats_detail",
    ),
    # Estadísticas de nutrición
    path(
        "nutrition/",
        api_views.NutritionStatsListCreateView.as_view(),
        name="nutrition_stats_list",
    ),
    path(
        "nutrition/<int:pk>/",
        api_views.NutritionStatsDetailView.as_view(),
        name="nutrition_stats_detail",
    ),
    # Resumen de estadísticas
    path("summary/", api_views.stats_summary, name="stats_summary"),
    # Dashboard
    path("dashboard/", api_views.dashboard_view, name="dashboard"),
    # Progreso de hábitos específicos
    path("habits/<int:habit_id>/progress/", api_views.habit_progress_view, name="habit_progress_detail"),
    path("habits/<int:habit_id>/complete/", api_views.mark_habit_completed_view, name="mark_habit_completed"),
    path("habits/<int:habit_id>/incomplete/", api_views.mark_habit_incomplete_view, name="mark_habit_incomplete"),
    # Health check
    path("health/", api_views.health_check, name="health_check"),
]
