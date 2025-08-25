"""
Base de datos nutricional local para alimentos comunes
"""
NUTRITION_DATABASE = {
    "apple": {
        "name": "Apple",
        "calories": 95,
        "protein_g": 0.5,
        "carbs_g": 25.0,
        "fat_g": 0.3,
        "fiber_g": 4.4,
        "sugar_g": 19.0
    },
    "banana": {
        "name": "Banana",
        "calories": 105,
        "protein_g": 1.3,
        "carbs_g": 27.0,
        "fat_g": 0.4,
        "fiber_g": 3.1,
        "sugar_g": 14.0
    },
    "chicken breast": {
        "name": "Chicken Breast",
        "calories": 165,
        "protein_g": 31.0,
        "carbs_g": 0.0,
        "fat_g": 3.6,
        "fiber_g": 0.0,
        "sugar_g": 0.0
    },
    "salmon": {
        "name": "Salmon",
        "calories": 208,
        "protein_g": 25.0,
        "carbs_g": 0.0,
        "fat_g": 12.0,
        "fiber_g": 0.0,
        "sugar_g": 0.0
    },
    "broccoli": {
        "name": "Broccoli",
        "calories": 55,
        "protein_g": 3.7,
        "carbs_g": 11.0,
        "fat_g": 0.6,
        "fiber_g": 5.2,
        "sugar_g": 2.6
    },
    "rice": {
        "name": "White Rice",
        "calories": 130,
        "protein_g": 2.7,
        "carbs_g": 28.0,
        "fat_g": 0.3,
        "fiber_g": 0.4,
        "sugar_g": 0.1
    },
    "eggs": {
        "name": "Eggs",
        "calories": 155,
        "protein_g": 13.0,
        "carbs_g": 1.1,
        "fat_g": 11.0,
        "fiber_g": 0.0,
        "sugar_g": 1.1
    },
    "milk": {
        "name": "Milk",
        "calories": 103,
        "protein_g": 8.0,
        "carbs_g": 12.0,
        "fat_g": 2.4,
        "fiber_g": 0.0,
        "sugar_g": 12.0
    },
    "bread": {
        "name": "Whole Wheat Bread",
        "calories": 247,
        "protein_g": 13.0,
        "carbs_g": 41.0,
        "fat_g": 4.2,
        "fiber_g": 7.0,
        "sugar_g": 6.0
    },
    "avocado": {
        "name": "Avocado",
        "calories": 160,
        "protein_g": 2.0,
        "carbs_g": 9.0,
        "fat_g": 15.0,
        "fiber_g": 7.0,
        "sugar_g": 0.7
    }
}

def search_nutrition_data(food_name):
    """
    Buscar datos nutricionales en la base de datos local
    """
    food_name_lower = food_name.lower().strip()
    
    # Búsqueda exacta
    if food_name_lower in NUTRITION_DATABASE:
        return NUTRITION_DATABASE[food_name_lower]
    
    # Búsqueda parcial
    for key, data in NUTRITION_DATABASE.items():
        if food_name_lower in key or key in food_name_lower:
            return data
    
    return None
