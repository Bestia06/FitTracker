"""
Django management command to migrate legacy data
"""
from django.core.management.base import BaseCommand
from django.db import connection
from django.contrib.auth.hashers import make_password
from apps.accounts.models import User
from apps.habits.models import Habit
from apps.nutrition.models import Meal
from apps.workouts.models import Workout
from datetime import datetime


class Command(BaseCommand):
    help = 'Migrate legacy data to Django models'

    def handle(self, *args, **options):
        self.stdout.write('Starting data migration...')
        
        # Mapping dictionaries
        user_mapping = {}
        habit_mapping = {}
        
        # Migrate Users
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, username, email, password_hash, date_joined FROM User")
            legacy_users = cursor.fetchall()
            
            for user_data in legacy_users:
                user_id, username, email, password_hash, date_joined = user_data
                
                # Check if user already exists
                if User.objects.filter(email=email).exists():
                    user = User.objects.get(email=email)
                    self.stdout.write(f'User {email} already exists, skipping...')
                else:
                    # Create Django user
                    user = User.objects.create(
                        username=username,
                        email=email,
                        password=make_password(password_hash),
                        date_joined=date_joined or datetime.now(),
                        fitness_level='beginner'
                    )
                    self.stdout.write(f'Created user: {email}')
                
                user_mapping[user_id] = user.id
        
        # Migrate Habits
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, user_id, title, kind, target_value, color_hex, created_at FROM Habit")
            legacy_habits = cursor.fetchall()
            
            for habit_data in legacy_habits:
                habit_id, user_id, title, kind, target_value, color_hex, created_at = habit_data
                
                if user_id in user_mapping:
                    # Check if habit already exists
                    existing_habit = Habit.objects.filter(
                        user_id=user_mapping[user_id],
                        name=title
                    ).first()
                    
                    if existing_habit:
                        self.stdout.write(f'Habit {title} already exists, skipping...')
                        habit_mapping[habit_id] = existing_habit.id
                    else:
                        habit = Habit.objects.create(
                            user_id=user_mapping[user_id],
                            name=title,
                            description=f"Habit migrated from legacy: {title}",
                            category=kind.lower() if kind else 'general',
                            frequency='daily',
                            target_count=int(target_value) if target_value else 1,
                            is_active=True,
                            created_at=created_at or datetime.now()
                        )
                        self.stdout.write(f'Created habit: {title}')
                        habit_mapping[habit_id] = habit.id
        
        # Migrate Nutrition Entries
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, user_id, date, name, calories, protein_g, carbs_g, fat_g FROM NutritionEntry")
            legacy_nutrition = cursor.fetchall()
            
            for nutrition_data in legacy_nutrition:
                nutrition_id, user_id, date, name, calories, protein_g, carbs_g, fat_g = nutrition_data
                
                if user_id in user_mapping:
                    # Check if meal already exists
                    existing_meal = Meal.objects.filter(
                        user_id=user_mapping[user_id],
                        name=name,
                        date=date
                    ).first()
                    
                    if existing_meal:
                        self.stdout.write(f'Meal {name} on {date} already exists, skipping...')
                    else:
                        meal = Meal.objects.create(
                            user_id=user_mapping[user_id],
                            name=name,
                            meal_type='other',
                            date=date,
                            notes=f"Migrated from legacy: {name} - Calories: {calories}, Protein: {protein_g}g, Carbs: {carbs_g}g, Fat: {fat_g}g"
                        )
                        self.stdout.write(f'Created meal: {name} on {date}')
        
        # Migrate Workouts
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, habit_id, date, duration_minutes, notes, created_at, duration_min FROM Workout")
            legacy_workouts = cursor.fetchall()
            
            for workout_data in legacy_workouts:
                workout_id, habit_id, date, duration_minutes, notes, created_at, duration_min = workout_data
                
                if habit_id in habit_mapping:
                    # Get user_id from habit
                    habit = Habit.objects.get(id=habit_mapping[habit_id])
                    user_id = habit.user_id
                    
                    # Check if workout already exists
                    existing_workout = Workout.objects.filter(
                        user_id=user_id,
                        name=f"Workout from {date}",
                        date=date
                    ).first()
                    
                    if existing_workout:
                        self.stdout.write(f'Workout on {date} already exists, skipping...')
                    else:
                        # Convert duration to timedelta
                        from datetime import timedelta
                        duration = timedelta(minutes=duration_minutes or duration_min or 30)
                        
                        workout = Workout.objects.create(
                            user_id=user_id,
                            name=f"Workout from {date}",
                            description=notes or f"Workout migrated from legacy",
                            date=date,
                            duration=duration,
                            calories_burned=None,
                            notes=notes or "",
                            created_at=created_at or datetime.now()
                        )
                        self.stdout.write(f'Created workout on {date}')
        
        self.stdout.write(
            self.style.SUCCESS('Data migration completed successfully!')
        )
