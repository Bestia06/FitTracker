"""
Django management command to cleanup legacy tables
"""

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Cleanup legacy tables after migration"

    def handle(self, *args, **options):
        self.stdout.write("Starting cleanup of legacy tables...")

        with connection.cursor() as cursor:
            # Drop legacy tables
            tables_to_drop = ["User", "Habit", "NutritionEntry", "Workout"]

            for table in tables_to_drop:
                try:
                    cursor.execute(f"DROP TABLE IF EXISTS `{table}`")
                    self.stdout.write(f"Dropped table: {table}")
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f"Error dropping {table}: {e}")
                    )

        # Verify Django tables have data
        from apps.accounts.models import User
        from apps.habits.models import Habit
        from apps.nutrition.models import Meal
        from apps.workouts.models import Workout

        self.stdout.write("\nVerification:")
        self.stdout.write(f"Users: {User.objects.count()}")
        self.stdout.write(f"Habits: {Habit.objects.count()}")
        self.stdout.write(f"Meals: {Meal.objects.count()}")
        self.stdout.write(f"Workouts: {Workout.objects.count()}")

        self.stdout.write(self.style.SUCCESS("\nLegacy tables cleanup completed!"))
