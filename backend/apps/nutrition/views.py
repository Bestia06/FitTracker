import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .services import api_ninja_service


@csrf_exempt
@require_http_methods(["GET"])
def get_nutrition_info(request):
    """Get nutrition information for a food item"""
    query = request.GET.get("query")
    if not query:
        return JsonResponse({"error": "Query parameter is required"}, status=400)

    try:
        nutrition_data = api_ninja_service.get_nutrition_info(query)
        if nutrition_data:
            return JsonResponse({"data": nutrition_data})
        else:
            return JsonResponse({"error": "No nutrition data found"}, status=404)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=500)
    except Exception as e:
        return JsonResponse({"error": "Internal server error"}, status=500)


@csrf_exempt
@require_http_methods(["GET"])
def get_exercise_info(request):
    """Get exercise information by name"""
    name = request.GET.get("name")
    if not name:
        return JsonResponse({"error": "Name parameter is required"}, status=400)

    try:
        exercise_data = api_ninja_service.get_exercise_info(name)
        if exercise_data:
            return JsonResponse({"data": exercise_data})
        else:
            return JsonResponse({"error": "No exercise data found"}, status=404)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=500)
    except Exception as e:
        return JsonResponse({"error": "Internal server error"}, status=500)


@csrf_exempt
@require_http_methods(["GET"])
def get_exercises_by_muscle(request):
    """Get exercises by muscle group"""
    muscle = request.GET.get("muscle")
    if not muscle:
        return JsonResponse({"error": "Muscle parameter is required"}, status=400)

    try:
        exercises_data = api_ninja_service.get_exercises_by_muscle(muscle)
        if exercises_data:
            return JsonResponse({"data": exercises_data})
        else:
            return JsonResponse(
                {"error": "No exercises found for this muscle"}, status=404
            )
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=500)
    except Exception as e:
        return JsonResponse({"error": "Internal server error"}, status=500)
