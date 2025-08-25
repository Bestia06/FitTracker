"""
URLs for habits app.
"""
from django.urls import path
from . import api_views

app_name = 'habits'

urlpatterns = [
    # Hábitos
    path('', api_views.HabitListCreateView.as_view(), name='habit_list'),
    path(
        '<int:pk>/',
        api_views.HabitDetailView.as_view(),
        name='habit_detail'
    ),
    # Marcar hábitos como completados
    path(
        '<int:pk>/complete/',
        api_views.mark_habit_completed,
        name='habit_complete'
    ),
    path(
        '<int:pk>/incomplete/',
        api_views.mark_habit_incomplete,
        name='habit_incomplete'
    ),
    path(
        '<int:pk>/progress/',
        api_views.get_habit_progress,
        name='habit_progress'
    ),
]
