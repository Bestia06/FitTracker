"""Base de datos local de ejercicios para entrenamientos"""

EXERCISE_DATABASE = {
    "push-ups": {
        "name": "Push-ups",
        "type": "strength",
        "muscle": "chest",
        "equipment": "body weight",
        "difficulty": "beginner",
        "instructions": "Start in a plank position, lower your body, then push back up"
    },
    "squats": {
        "name": "Squats",
        "type": "strength",
        "muscle": "quadriceps",
        "equipment": "body weight",
        "difficulty": "beginner",
        "instructions": "Stand with feet shoulder-width apart, lower your body as if sitting back"
    },
    "pull-ups": {
        "name": "Pull-ups",
        "type": "strength",
        "muscle": "lats",
        "equipment": "body weight",
        "difficulty": "intermediate",
        "instructions": "Hang from a bar and pull your body up until your chin is over the bar"
    },
    "running": {
        "name": "Running",
        "type": "cardio",
        "muscle": "legs",
        "equipment": "none",
        "difficulty": "beginner",
        "instructions": "Run at a steady pace for cardiovascular fitness"
    },
    "cycling": {
        "name": "Cycling",
        "type": "cardio",
        "muscle": "legs",
        "equipment": "bicycle",
        "difficulty": "beginner",
        "instructions": "Ride a bicycle for cardiovascular and leg strength"
    },
    "plank": {
        "name": "Plank",
        "type": "strength",
        "muscle": "core",
        "equipment": "body weight",
        "difficulty": "beginner",
        "instructions": "Hold a plank position to strengthen your core"
    },
    "burpees": {
        "name": "Burpees",
        "type": "strength",
        "muscle": "full body",
        "equipment": "body weight",
        "difficulty": "intermediate",
        "instructions": "Combine squat, push-up, and jump in one fluid movement"
    },
    "deadlift": {
        "name": "Deadlift",
        "type": "strength",
        "muscle": "back",
        "equipment": "barbell",
        "difficulty": "advanced",
        "instructions": "Lift a barbell from the ground to hip level with proper form"
    },
    "bench-press": {
        "name": "Bench Press",
        "type": "strength",
        "muscle": "chest",
        "equipment": "barbell",
        "difficulty": "intermediate",
        "instructions": "Lie on a bench and press a barbell up from your chest"
    },
    "yoga": {
        "name": "Yoga",
        "type": "flexibility",
        "muscle": "full body",
        "equipment": "mat",
        "difficulty": "beginner",
        "instructions": "Practice various yoga poses for flexibility and mindfulness"
    }
}


def search_exercise_data(exercise_name):
    """Buscar datos de ejercicios en la base de datos local"""
    exercise_name_lower = exercise_name.lower().strip()
    
    # Búsqueda exacta
    if exercise_name_lower in EXERCISE_DATABASE:
        return EXERCISE_DATABASE[exercise_name_lower]
    
    # Búsqueda parcial
    for key, data in EXERCISE_DATABASE.items():
        if exercise_name_lower in key or key in exercise_name_lower:
            return data
    
    return None


def get_all_exercises():
    """Obtener todos los ejercicios disponibles"""
    return list(EXERCISE_DATABASE.values())


def get_exercises_by_type(exercise_type):
    """Obtener ejercicios por tipo"""
    return [
        exercise for exercise in EXERCISE_DATABASE.values()
        if exercise["type"] == exercise_type
    ]
