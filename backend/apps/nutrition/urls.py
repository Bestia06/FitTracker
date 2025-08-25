"""
URLs for nutrition app.
"""

from django.urls import path

from . import api_views

app_name = "nutrition"

urlpatterns = [
    # Entradas nutricionales
    path("", api_views.NutritionListCreateView.as_view(), name="nutrition_list"),
    path(
        "<int:pk>/",
        api_views.NutritionDetailView.as_view(),
        name="nutrition_detail",
    ),
]
