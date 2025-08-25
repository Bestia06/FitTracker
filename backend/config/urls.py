from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.tokens import RefreshToken
from apps.habits.models import Habit
from apps.accounts.models import User
import json

def api_home(request):
    return JsonResponse({
        'message': '🚀 FitTracker API v2.0 - JWT + API Ninja',
        'status': 'running',
        'features': {'jwt_auth': True, 'api_ninja': True},
        'endpoints': {
            'auth': {
                'jwt_login': 'POST /api/auth/jwt/login/',
                'jwt_refresh': 'POST /api/auth/jwt/refresh/',
                'register': 'POST /api/auth/register/',
            },
            'habits': 'GET/POST /api/habits/',
            'nutrition_enrich': 'POST /api/nutrition/enrich/',
            'exercise_search': 'GET /api/workouts/exercises/search/',
            'admin': '/admin/'
        }
    })

@method_decorator(csrf_exempt, name='dispatch')
class HabitAPI(View):
    def get(self, request, habit_id=None):
        try:
            if habit_id:
                habit = Habit.objects.get(id=habit_id)
                return JsonResponse({
                    'id': habit.id,
                    'title': habit.title,
                    'kind': habit.kind,
                    'target_value': habit.target_value,
                    'color_hex': habit.color_hex,
                    'created_at': habit.created_at.isoformat()
                })
            else:
                habits = Habit.objects.all()
                habit_list = [{
                    'id': h.id,
                    'title': h.title,
                    'kind': h.kind,
                    'target_value': h.target_value,
                    'color_hex': h.color_hex,
                    'created_at': h.created_at.isoformat()
                } for h in habits]
                
                return JsonResponse({
                    'count': len(habit_list),
                    'results': habit_list,
                    'message': f'📋 {len(habit_list)} hábitos (JWT + API Ninja activos)'
                })
        except Habit.DoesNotExist:
            return JsonResponse({'error': 'Hábito no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            user, created = User.objects.get_or_create(
                username='defaultuser',
                defaults={'email': 'default@fittracker.com'}
            )
            
            habit = Habit.objects.create(
                title=data['title'],
                kind=data['kind'],
                target_value=float(data['target_value']),
                color_hex=data['color_hex'],
                user=user
            )
            
            return JsonResponse({
                'success': True,
                'message': '🎯 Hábito creado con JWT + API Ninja!',
                'habit': {
                    'id': habit.id,
                    'title': habit.title,
                    'kind': habit.kind,
                    'target_value': habit.target_value,
                    'color_hex': habit.color_hex
                }
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        data = request.data
        
        if User.objects.filter(username=data['username']).exists():
            return Response({'error': 'Usuario ya existe'}, status=400)
        
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'success': True,
            'message': '🎉 Usuario registrado con JWT!',
            'user': {
                'id': str(user.id),
                'username': user.username,
                'email': user.email
            },
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        }, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def enrich_nutrition(request):
    try:
        import requests
        from django.conf import settings
        
        food_name = request.data.get('name', '')
        if not food_name:
            return Response({'error': 'Nombre del alimento requerido'}, status=400)
        
        if not settings.API_NINJA_KEY:
            return Response({'error': 'API Ninja no configurado - revisa archivo .env'}, status=503)
        
        headers = {'X-Api-Key': settings.API_NINJA_KEY}
        response = requests.get(
            f"{settings.API_NINJA_BASE_URL}/nutrition",
            headers=headers,
            params={'query': food_name},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if data:
                enriched = data[0]
                return Response({
                    'success': True,
                    'message': f'✨ Datos nutricionales obtenidos para: {food_name}',
                    'data': {
                        'name': enriched.get('name', food_name),
                        'calories': enriched.get('calories', 0),
                        'protein_g': enriched.get('protein_g', 0),
                        'carbs_g': enriched.get('carbohydrates_total_g', 0),
                        'fat_g': enriched.get('fat_total_g', 0),
                        'sugar_g': enriched.get('sugar_g', 0),
                        'fiber_g': enriched.get('fiber_g', 0)
                    },
                    'source': 'API Ninja'
                })
        
        return Response({'error': f'No se encontraron datos nutricionales para: {food_name}'}, status=404)
    except Exception as e:
        return Response({'error': f'Error: {str(e)}'}, status=500)

@api_view(['GET'])  
@permission_classes([AllowAny])
def search_exercises(request):
    try:
        import requests
        from django.conf import settings
        
        exercise_name = request.GET.get('name', '')
        if not exercise_name:
            return Response({'error': 'Parámetro name requerido. Ejemplo: /api/workouts/exercises/search/?name=push-up'}, status=400)
        
        if not settings.API_NINJA_KEY:
            return Response({'error': 'API Ninja no configurado - revisa archivo .env'}, status=503)
        
        headers = {'X-Api-Key': settings.API_NINJA_KEY}
        response = requests.get(
            f"{settings.API_NINJA_BASE_URL}/exercises",
            headers=headers,
            params={'name': exercise_name},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            return Response({
                'success': True,
                'message': f'🏋️ Ejercicios encontrados para: {exercise_name}',
                'count': len(data),
                'results': data,
                'source': 'API Ninja'
            })
        
        return Response({'error': f'No se encontraron ejercicios para: {exercise_name}'}, status=404)
    except Exception as e:
        return Response({'error': f'Error: {str(e)}'}, status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT Authentication endpoints
    path('api/auth/jwt/login/', TokenObtainPairView.as_view(), name='jwt_login'),
    path('api/auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('api/auth/jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
    path('api/auth/register/', register_user, name='register'),
    
    # API endpoints
    path('api/habits/', HabitAPI.as_view(), name='habits'),
    path('api/habits/<int:habit_id>/', HabitAPI.as_view(), name='habit_detail'),
    
    # API Ninja endpoints  
    path('api/nutrition/enrich/', enrich_nutrition, name='enrich_nutrition'),
    path('api/workouts/exercises/search/', search_exercises, name='search_exercises'),
    
    # Home
    path('', api_home, name='home'),
]