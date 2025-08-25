import requests
from apps.accounts.models import User
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


def api_home(request):
    """API home page"""
    return JsonResponse(
        {
            "message": "🚀 FitTracker API v2.0 - Modular Structure",
            "status": "running",
            "features": {
                "jwt_auth": True,
                "modular_structure": True,
                "api_ninja": True,
            },
            "endpoints": {
                "auth": {
                    "jwt_login": "POST /api/auth/jwt/login/",
                    "jwt_refresh": "POST /api/auth/jwt/refresh/",
                    "register": "POST /api/accounts/register/",
                    "profile": "GET /api/accounts/profile/",
                },
                "habits": {
                    "list": "GET/POST /api/habits/",
                    "detail": "GET/PUT/DELETE /api/habits/<id>/",
                },
                "nutrition": {
                    "list": "GET/POST /api/nutrition/",
                    "detail": "GET/PUT/DELETE /api/nutrition/<id>/",
                    "enrich": "POST /api/nutrition/enrich/",
                },
                "workouts": {
                    "list": "GET/POST /api/workouts/",
                    "detail": "GET/PUT/DELETE /api/workouts/<id>/",
                    "search_exercises": "GET /api/workouts/exercises/search/",
                },
                "stats": {
                    "summary": "GET /api/stats/summary/",
                    "user_stats": "GET/PUT /api/stats/user/",
                    "habit_progress": "GET/POST /api/stats/habits/progress/",
                    "workout_stats": "GET/POST /api/stats/workouts/",
                    "nutrition_stats": "GET/POST /api/stats/nutrition/",
                },
                "admin": "/admin/",
            },
        }
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    """Register new user with JWT"""
    try:
        data = request.data

        if User.objects.filter(username=data["username"]).exists():
            return Response({"error": "User already exists"}, status=400)

        user = User.objects.create_user(
            username=data["username"],
            email=data["email"],
            password=data["password"],
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
        )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "success": True,
                "message": "🎉 User registered with JWT!",
                "user": {
                    "id": str(user.id),
                    "username": user.username,
                    "email": user.email,
                },
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            },
            status=201,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(["POST"])
@permission_classes([AllowAny])
def enrich_nutrition(request):
    """Enrich nutritional data with API Ninja or local database"""
    try:
        from apps.nutrition.nutrition_data import search_nutrition_data
        from django.conf import settings

        food_name = request.data.get("name", "")
        if not food_name:
            return Response({"error": "Food name required"}, status=400)

        # First try with API Ninja (only if configured)
        if settings.API_NINJA_KEY and settings.API_NINJA_KEY != "demo-key-for-testing":
            try:
                headers = {"X-Api-Key": settings.API_NINJA_KEY}
                response = requests.get(
                    f"{settings.API_NINJA_BASE_URL}/nutrition",
                    headers=headers,
                    params={"query": food_name},
                    timeout=10,
                )

                if response.status_code == 200:
                    data = response.json()
                    if data:
                        enriched = data[0]
                        # Check if data is complete (not premium)
                        calories = enriched.get("calories", 0)
                        protein = enriched.get("protein_g", 0)

                        # If data is complete, use API Ninja
                        if (
                            calories != "Only available for premium subscribers"
                            and protein != "Only available for premium subscribers"
                        ):
                            return Response(
                                {
                                    "success": True,
                                    "message": f"✨ Nutritional data for: {food_name}",
                                    "data": {
                                        "name": enriched.get("name", food_name),
                                        "calories": enriched.get("calories", 0),
                                        "protein_g": enriched.get("protein_g", 0),
                                        "carbs_g": enriched.get(
                                            "carbohydrates_total_g", 0
                                        ),
                                        "fat_g": enriched.get("fat_total_g", 0),
                                        "sugar_g": enriched.get("sugar_g", 0),
                                        "fiber_g": enriched.get("fiber_g", 0),
                                    },
                                    "source": "API Ninja",
                                }
                            )
            except Exception:
                pass  # Continue with local database

        # Fallback: use local database
        local_data = search_nutrition_data(food_name)
        if local_data:
            return Response(
                {
                    "success": True,
                    "message": f"✨ Nutritional data for: {food_name}",
                    "data": {
                        "name": local_data["name"],
                        "calories": local_data["calories"],
                        "protein_g": local_data["protein_g"],
                        "carbs_g": local_data["carbs_g"],
                        "fat_g": local_data["fat_g"],
                        "sugar_g": local_data["sugar_g"],
                        "fiber_g": local_data["fiber_g"],
                    },
                    "source": "Local database",
                }
            )

        return Response(
            {"error": f"No data found for: {food_name}"}, status=404
        )
    except Exception as e:
        return Response({"error": f"Error: {str(e)}"}, status=500)


@api_view(["POST"])
@permission_classes([AllowAny])
def enrich_exercise(request):
    """Enrich exercise data with API Ninja or local database"""
    try:
        from django.conf import settings
        from apps.workouts.exercise_data import search_exercise_data

        exercise_name = request.data.get("name", "")
        if not exercise_name:
            return Response({"error": "Exercise name required"}, status=400)

        # First try with API Ninja (only if configured)
        if (settings.API_NINJA_KEY and 
            settings.API_NINJA_KEY != "demo-key-for-testing"):
            try:
                headers = {"X-Api-Key": settings.API_NINJA_KEY}
                response = requests.get(
                    f"{settings.API_NINJA_BASE_URL}/exercises",
                    headers=headers,
                    params={"name": exercise_name},
                    timeout=10,
                )

                if response.status_code == 200:
                    data = response.json()
                    if data:
                        enriched = data[0]
                        return Response(
                            {
                                "success": True,
                                "message": f"✨ Exercise data for: {exercise_name}",
                                "data": {
                                    "name": enriched.get("name", exercise_name),
                                    "type": enriched.get("type", ""),
                                    "muscle": enriched.get("muscle", ""),
                                    "equipment": enriched.get("equipment", ""),
                                    "difficulty": enriched.get("difficulty", ""),
                                    "instructions": enriched.get("instructions", ""),
                                },
                                "source": "API Ninja",
                            }
                        )
            except Exception:
                pass  # Continue with local database

        # Fallback: use local database
        local_data = search_exercise_data(exercise_name)
        if local_data:
            return Response(
                {
                    "success": True,
                    "message": f"✨ Exercise data for: {exercise_name}",
                    "data": local_data,
                    "source": "Local database",
                }
            )

        return Response(
            {"error": f"No data found for: {exercise_name}"}, status=404
        )
    except Exception as e:
        return Response({"error": f"Error: {str(e)}"}, status=500)


@api_view(["GET"])
@permission_classes([AllowAny])
def search_exercises(request):
    """Search exercises with API Ninja"""
    try:
        from django.conf import settings

        exercise_name = request.GET.get("name", "")
        if not exercise_name:
            return Response({"error": "Name parameter required"}, status=400)

        if not settings.API_NINJA_KEY:
            return Response({"error": "API Ninja not configured"}, status=503)

        headers = {"X-Api-Key": settings.API_NINJA_KEY}
        response = requests.get(
            f"{settings.API_NINJA_BASE_URL}/exercises",
            headers=headers,
            params={"name": exercise_name},
            timeout=10,
        )

        if response.status_code == 200:
            data = response.json()
            return Response(
                {
                    "success": True,
                    "message": f"🏋️ Exercises found for: {exercise_name}",
                    "count": len(data),
                    "results": data,
                    "source": "API Ninja",
                }
            )

        return Response(
            {"error": f"No exercises found for: {exercise_name}"}, status=404
        )
    except Exception as e:
        return Response({"error": f"Error: {str(e)}"}, status=500)


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # JWT Authentication endpoints
    path("api/auth/jwt/login/", TokenObtainPairView.as_view(), name="jwt_login"),
    path("api/auth/jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("api/auth/jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
    # Modular API endpoints
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/habits/", include("apps.habits.urls")),
    path("api/nutrition/", include("apps.nutrition.urls")),
    path("api/workouts/", include("apps.workouts.urls")),
    path("api/stats/", include("apps.stats.urls")),
    # Legacy endpoints (maintain compatibility)
    path("api/auth/register/", register_user, name="register"),
    path("api/nutrition/enrich/", enrich_nutrition, name="enrich_nutrition"),
    path("api/workouts/exercises/enrich/", enrich_exercise, name="enrich_exercise"),
    path("api/workouts/exercises/search/", search_exercises, name="search_exercises"),
    # Swagger/OpenAPI Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # Home
    path("", api_home, name="home"),
]
