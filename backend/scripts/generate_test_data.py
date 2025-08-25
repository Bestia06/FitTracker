#!/usr/bin/env python
"""
Script to generate test data for FitTracker application
Generates 50 records for each model with realistic data
"""

import os
import sys
import django
from datetime import date, timedelta
from decimal import Decimal
import random

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings_dev')
django.setup()

from django.contrib.auth import get_user_model
from apps.accounts.models import User
from apps.habits.models import Habit
from apps.nutrition.models import Nutrition
from apps.workouts.models import Workout, Exercise
from apps.stats.models import UserStats, HabitProgress, WorkoutStats, NutritionStats

User = get_user_model()

# Sample data for realistic generation
FOOD_ITEMS = [
    ("Chicken Breast", 165, 31, 0, 3.6),
    ("Salmon", 208, 25, 0, 12),
    ("Brown Rice", 111, 2.6, 23, 0.9),
    ("Broccoli", 34, 2.8, 7, 0.4),
    ("Sweet Potato", 86, 1.6, 20, 0.1),
    ("Quinoa", 120, 4.4, 22, 1.9),
    ("Greek Yogurt", 59, 10, 3.6, 0.4),
    ("Almonds", 164, 6, 6, 14),
    ("Banana", 89, 1.1, 23, 0.3),
    ("Spinach", 23, 2.9, 3.6, 0.4),
    ("Eggs", 155, 13, 1.1, 11),
    ("Oatmeal", 68, 2.4, 12, 1.4),
    ("Avocado", 160, 2, 9, 15),
    ("Tuna", 144, 30, 0, 1),
    ("Blueberries", 57, 0.7, 14, 0.3),
    ("Turkey", 135, 29, 0, 1.7),
    ("Cottage Cheese", 98, 11, 3.4, 4.3),
    ("Carrots", 41, 0.9, 10, 0.2),
    ("Lentils", 116, 9, 20, 0.4),
    ("Pork Chop", 231, 26, 0, 12),
    ("Asparagus", 20, 2.2, 3.9, 0.1),
    ("Milk", 42, 3.4, 5, 1),
    ("Peanut Butter", 188, 8, 6, 16),
    ("Strawberries", 32, 0.7, 8, 0.3),
    ("Beef Steak", 271, 26, 0, 18),
    ("Cauliflower", 25, 1.9, 5, 0.3),
    ("Tofu", 76, 8, 1.9, 4.8),
    ("Oranges", 47, 0.9, 12, 0.1),
    ("Shrimp", 85, 20, 0.2, 0.5),
    ("Kale", 33, 2.9, 6, 0.6),
    ("Cheddar Cheese", 113, 7, 0.4, 9),
    ("Apples", 52, 0.3, 14, 0.2),
    ("Cod", 82, 18, 0, 0.7),
    ("Bell Peppers", 31, 1, 7, 0.3),
    ("Hummus", 166, 8, 14, 10),
    ("Grapes", 62, 0.6, 16, 0.2),
    ("Lamb", 294, 25, 0, 21),
    ("Zucchini", 17, 1.2, 3.1, 0.3),
    ("Soy Milk", 33, 3.2, 1.8, 1.9),
    ("Cashews", 157, 5, 9, 12),
    ("Pineapple", 50, 0.5, 13, 0.1),
    ("Halibut", 111, 21, 0, 2.3),
    ("Brussels Sprouts", 38, 3.4, 8, 0.3),
    ("Feta Cheese", 74, 4, 1.2, 6),
    ("Pears", 57, 0.4, 15, 0.1),
    ("Mushrooms", 22, 3.1, 3.3, 0.3),
    ("Walnuts", 185, 4, 4, 18),
    ("Kiwi", 42, 0.8, 10, 0.4),
    ("Sardines", 208, 24, 0, 12),
    ("Arugula", 25, 2.6, 3.7, 0.7),
    ("Goat Cheese", 103, 6, 0.6, 8),
    ("Peaches", 39, 0.9, 10, 0.3),
    ("Cucumber", 16, 0.7, 3.6, 0.1),
    ("Pistachios", 159, 6, 8, 13),
    ("Mango", 60, 0.8, 15, 0.4),
    ("Swordfish", 146, 23, 0, 5.7),
    ("Radishes", 16, 0.7, 3.4, 0.1),
]

HABIT_TITLES = [
    "Drink 8 glasses of water daily",
    "Exercise for 30 minutes",
    "Read 20 pages",
    "Meditate for 10 minutes",
    "Take vitamins",
    "Walk 10,000 steps",
    "Practice guitar for 15 minutes",
    "Write in journal",
    "Do 50 push-ups",
    "Eat 5 servings of vegetables",
    "Practice Spanish for 20 minutes",
    "Do 10 minutes of stretching",
    "Call a friend or family member",
    "Learn a new word",
    "Practice coding for 30 minutes",
    "Do 20 squats",
    "Listen to a podcast",
    "Practice drawing for 15 minutes",
    "Do 5 minutes of deep breathing",
    "Take a photo of something beautiful",
    "Practice piano for 20 minutes",
    "Do 30 jumping jacks",
    "Read news for 10 minutes",
    "Practice yoga for 15 minutes",
    "Do 25 sit-ups",
    "Practice cooking a new recipe",
    "Do 10 minutes of cleaning",
    "Practice photography",
    "Do 40 lunges",
    "Practice writing for 15 minutes",
    "Do 5 minutes of gratitude",
    "Practice painting for 20 minutes",
    "Do 35 burpees",
    "Practice singing for 10 minutes",
    "Do 15 minutes of gardening",
    "Practice dancing for 15 minutes",
    "Do 45 mountain climbers",
    "Practice knitting for 20 minutes",
    "Do 10 minutes of organizing",
    "Practice woodworking for 30 minutes",
    "Do 50 jumping jacks",
    "Practice calligraphy for 15 minutes",
    "Do 20 minutes of walking",
    "Practice origami for 10 minutes",
    "Do 30 push-ups",
    "Practice martial arts for 20 minutes",
    "Do 15 minutes of stretching",
    "Practice pottery for 30 minutes",
    "Do 25 burpees",
    "Practice photography for 15 minutes",
    "Do 10 minutes of meditation",
    "Practice sculpture for 20 minutes",
    "Do 40 sit-ups",
]

EXERCISE_NAMES = [
    "Push-ups", "Squats", "Lunges", "Burpees", "Plank",
    "Mountain Climbers", "Jumping Jacks", "Sit-ups", "Crunches",
    "Pull-ups", "Dips", "Wall Sit", "High Knees", "Butterfly Kicks",
    "Russian Twists", "Leg Raises", "Bicycle Crunches", "Superman",
    "Bird Dog", "Dead Bug", "Glute Bridges", "Donkey Kicks",
    "Fire Hydrants", "Clamshells", "Side Plank", "Reverse Crunches",
    "V-Ups", "Mason Twists", "Flutter Kicks", "Scissor Kicks",
    "Hollow Hold", "Arch Hold", "L-Sit", "Handstand Hold",
    "Pike Push-ups", "Diamond Push-ups", "Wide Push-ups",
    "Decline Push-ups", "Incline Push-ups", "Pistol Squats",
    "Jump Squats", "Split Squats", "Calf Raises", "Box Jumps",
    "Tuck Jumps", "Broad Jumps", "Lateral Jumps", "Single-leg Deadlifts",
    "Good Mornings", "Hip Thrusts", "Romanian Deadlifts", "Sumo Squats"
]

def create_test_users():
    """Create test users if they don't exist"""
    users_created = []
    
    # Create admin user
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@fittracker.com',
            'first_name': 'Admin',
            'last_name': 'User',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        users_created.append(admin_user)
        print(f"Created admin user: {admin_user.username}")
    
    # Create joseph user
    joseph_user, created = User.objects.get_or_create(
        username='joseph',
        defaults={
            'email': 'joseph@fittracker.com',
            'first_name': 'Joseph',
            'last_name': 'Developer',
            'is_staff': False,
            'is_superuser': False
        }
    )
    if created:
        joseph_user.set_password('joseph123')
        joseph_user.save()
        users_created.append(joseph_user)
        print(f"Created joseph user: {joseph_user.username}")
    
    return [admin_user, joseph_user]

def create_habits(users):
    """Create 50 habits distributed among users"""
    habits = []
    habit_kinds = ['daily', 'weekly', 'monthly', 'counter', 'timer']
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', 
              '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9']
    
    for i in range(50):
        user = random.choice(users)
        habit = Habit.objects.create(
            user=user,
            title=random.choice(HABIT_TITLES),
            kind=random.choice(habit_kinds),
            target_value=random.randint(1, 100),
            color_hex=random.choice(colors)
        )
        habits.append(habit)
        print(f"Created habit: {habit.title} for {habit.user.username}")
    
    return habits

def create_nutrition_entries(users):
    """Create 50 nutrition entries distributed among users"""
    nutrition_entries = []
    
    for i in range(50):
        user = random.choice(users)
        food_name, calories, protein, carbs, fat = random.choice(FOOD_ITEMS)
        
        # Generate random date within last 30 days
        random_date = date.today() - timedelta(days=random.randint(0, 30))
        
        nutrition = Nutrition.objects.create(
            user=user,
            date=random_date,
            name=food_name,
            calories=calories,
            protein_g=Decimal(str(protein)),
            carbs_g=Decimal(str(carbs)),
            fat_g=Decimal(str(fat))
        )
        nutrition_entries.append(nutrition)
        print(f"Created nutrition entry: {nutrition.name} for {nutrition.user.username}")
    
    return nutrition_entries

def create_workouts(habits):
    """Create 50 workouts distributed among habits"""
    workouts = []
    status_choices = ['pending', 'done', 'skipped']
    
    for i in range(50):
        habit = random.choice(habits)
        random_date = date.today() - timedelta(days=random.randint(0, 30))
        
        workout = Workout.objects.create(
            habit=habit,
            date=random_date,
            duration_min=random.randint(15, 120),
            distancia_km=Decimal(str(random.uniform(0, 20))),
            calories=random.randint(100, 800),
            status=random.choice(status_choices),
            notes=f"Workout session {i+1}"
        )
        workouts.append(workout)
        print(f"Created workout: {workout.habit.title} for {workout.habit.user.username}")
    
    return workouts

def create_exercises(workouts):
    """Create 50 exercises distributed among workouts"""
    exercises = []
    
    for i in range(50):
        workout = random.choice(workouts)
        
        exercise = Exercise.objects.create(
            workout=workout,
            name=random.choice(EXERCISE_NAMES),
            sets=random.randint(1, 5),
            reps=random.randint(5, 20),
            weight_kg=Decimal(str(random.uniform(0, 100))),
            duration_seconds=random.randint(30, 300),
            rest_seconds=random.randint(30, 120),
            notes=f"Exercise {i+1}"
        )
        exercises.append(exercise)
        print(f"Created exercise: {exercise.name} for workout {exercise.workout.id}")
    
    return exercises

def create_habit_progress(habits):
    """Create 50 habit progress entries"""
    progress_entries = []
    
    for i in range(50):
        habit = random.choice(habits)
        random_date = date.today() - timedelta(days=random.randint(0, 30))
        
        progress = HabitProgress.objects.create(
            habit=habit,
            date=random_date,
            completed=random.choice([True, False]),
            value=random.uniform(0, 100),
            notes=f"Progress entry {i+1}"
        )
        progress_entries.append(progress)
        print(f"Created habit progress: {progress.habit.title} for {progress.habit.user.username}")
    
    return progress_entries

def create_user_stats(users):
    """Create user stats for all users"""
    stats = []
    
    for user in users:
        stat, created = UserStats.objects.get_or_create(
            user=user,
            defaults={
                'total_workouts': random.randint(0, 100),
                'total_habits_completed': random.randint(0, 500),
                'total_calories_consumed': random.uniform(0, 50000),
                'total_calories_burned': random.uniform(0, 30000),
                'current_streak': random.randint(0, 30),
                'longest_streak': random.randint(0, 100),
                'last_activity_date': date.today() - timedelta(days=random.randint(0, 7))
            }
        )
        if created:
            stats.append(stat)
            print(f"Created user stats for: {stat.user.username}")
    
    return stats

def create_workout_stats(users):
    """Create 50 workout stats entries"""
    workout_stats = []
    
    for i in range(50):
        user = random.choice(users)
        random_date = date.today() - timedelta(days=random.randint(0, 30))
        
        stat = WorkoutStats.objects.create(
            user=user,
            date=random_date,
            total_duration=random.randint(30, 180),
            total_calories_burned=random.uniform(100, 800),
            workout_count=random.randint(1, 5)
        )
        workout_stats.append(stat)
        print(f"Created workout stats for: {stat.user.username}")
    
    return workout_stats

def create_nutrition_stats(users):
    """Create 50 nutrition stats entries"""
    nutrition_stats = []
    
    for i in range(50):
        user = random.choice(users)
        random_date = date.today() - timedelta(days=random.randint(0, 30))
        
        stat = NutritionStats.objects.create(
            user=user,
            date=random_date,
            total_calories=random.uniform(800, 2500),
            total_protein=random.uniform(50, 200),
            total_carbs=random.uniform(100, 400),
            total_fat=random.uniform(30, 100),
            total_fiber=random.uniform(10, 50),
            meal_count=random.randint(1, 6)
        )
        nutrition_stats.append(stat)
        print(f"Created nutrition stats for: {stat.user.username}")
    
    return nutrition_stats

def main():
    """Main function to generate all test data"""
    print("🚀 Starting FitTracker Test Data Generation...")
    print("=" * 50)
    
    # Create users
    print("\n👥 Creating users...")
    users = create_test_users()
    
    # Create habits
    print("\n✅ Creating habits...")
    habits = create_habits(users)
    
    # Create nutrition entries
    print("\n🍎 Creating nutrition entries...")
    nutrition_entries = create_nutrition_entries(users)
    
    # Create workouts
    print("\n💪 Creating workouts...")
    workouts = create_workouts(habits)
    
    # Create exercises
    print("\n🏋️ Creating exercises...")
    exercises = create_exercises(workouts)
    
    # Create habit progress
    print("\n📊 Creating habit progress...")
    progress_entries = create_habit_progress(habits)
    
    # Create user stats
    print("\n📈 Creating user stats...")
    user_stats = create_user_stats(users)
    
    # Create workout stats
    print("\n🏃 Creating workout stats...")
    workout_stats = create_workout_stats(users)
    
    # Create nutrition stats
    print("\n🥗 Creating nutrition stats...")
    nutrition_stats = create_nutrition_stats(users)
    
    # Summary
    print("\n" + "=" * 50)
    print("🎉 Test Data Generation Complete!")
    print("=" * 50)
    print(f"✅ Users: {len(users)}")
    print(f"✅ Habits: {len(habits)}")
    print(f"✅ Nutrition Entries: {len(nutrition_entries)}")
    print(f"✅ Workouts: {len(workouts)}")
    print(f"✅ Exercises: {len(exercises)}")
    print(f"✅ Habit Progress: {len(progress_entries)}")
    print(f"✅ User Stats: {len(user_stats)}")
    print(f"✅ Workout Stats: {len(workout_stats)}")
    print(f"✅ Nutrition Stats: {len(nutrition_stats)}")
    print("\n🔐 Login Credentials:")
    print("   Admin: username=admin, password=admin123")
    print("   Joseph: username=joseph, password=joseph123")
    print("\n🌐 Access the API at: http://127.0.0.1:8000/api/docs/")

if __name__ == "__main__":
    main()
