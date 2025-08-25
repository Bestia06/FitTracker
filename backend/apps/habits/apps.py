"""Habits app configuration module."""

from django.apps import AppConfig  # type: ignore


class HabitConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.habits"
