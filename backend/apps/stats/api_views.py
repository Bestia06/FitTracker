from datetime import timedelta

from django.db.models import Count, Q, Sum
from django.utils import timezone
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.conf import settings

from .models import HabitProgress, NutritionStats, UserStats, WorkoutStats
from .serializers import (
    HabitProgressSerializer,
    NutritionStatsSerializer,
    StatsSummarySerializer,
    UserStatsSerializer,
    WorkoutStatsSerializer,
)


class UserStatsView(generics.RetrieveUpdateAPIView):
    """Vista para estadísticas generales del usuario"""

    serializer_class = UserStatsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_stats, created = UserStats.objects.get_or_create(user=self.request.user)
        return user_stats


class HabitProgressListCreateView(generics.ListCreateAPIView):
    """Listar y crear progreso de hábitos"""

    serializer_class = HabitProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HabitProgress.objects.filter(
            habit__user=self.request.user
        ).select_related("habit")

    def perform_create(self, serializer):
        serializer.save()


class HabitProgressDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Ver, actualizar y eliminar progreso de hábito"""

    serializer_class = HabitProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HabitProgress.objects.filter(
            habit__user=self.request.user
        ).select_related("habit")


class WorkoutStatsListCreateView(generics.ListCreateAPIView):
    """Listar y crear estadísticas de entrenamientos"""

    serializer_class = WorkoutStatsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkoutStats.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutStatsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Ver, actualizar y eliminar estadísticas de entrenamiento"""

    serializer_class = WorkoutStatsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkoutStats.objects.filter(user=self.request.user)


class NutritionStatsListCreateView(generics.ListCreateAPIView):
    """Listar y crear estadísticas de nutrición"""

    serializer_class = NutritionStatsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return NutritionStats.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NutritionStatsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Ver, actualizar y eliminar estadísticas de nutrición"""

    serializer_class = NutritionStatsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return NutritionStats.objects.filter(user=self.request.user)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def stats_summary(request):
    """Obtener resumen de estadísticas del usuario"""
    user = request.user
    today = timezone.now().date()

    # Obtener estadísticas generales
    user_stats, created = UserStats.objects.get_or_create(user=user)

    # Calcular progreso semanal
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    weekly_workouts = WorkoutStats.objects.filter(
        user=user, date__range=[week_start, week_end]
    ).aggregate(
        total_duration=Sum("total_duration"),
        total_calories=Sum("total_calories_burned"),
        workout_count=Sum("workout_count"),
    )

    weekly_nutrition = NutritionStats.objects.filter(
        user=user, date__range=[week_start, week_end]
    ).aggregate(
        total_calories=Sum("total_calories"),
        total_protein=Sum("total_protein"),
        total_carbs=Sum("total_carbs"),
        total_fat=Sum("total_fat"),
    )

    weekly_habits = HabitProgress.objects.filter(
        habit__user=user, date__range=[week_start, week_end]
    ).aggregate(
        completed_count=Count("id", filter=Q(completed=True)), total_count=Count("id")
    )

    # Calcular progreso mensual
    month_start = today.replace(day=1)
    next_month = month_start.replace(day=28) + timedelta(days=4)
    month_end = next_month - timedelta(days=next_month.day)

    monthly_workouts = WorkoutStats.objects.filter(
        user=user, date__range=[month_start, month_end]
    ).aggregate(
        total_duration=Sum("total_duration"),
        total_calories=Sum("total_calories_burned"),
        workout_count=Sum("workout_count"),
    )

    monthly_nutrition = NutritionStats.objects.filter(
        user=user, date__range=[month_start, month_end]
    ).aggregate(
        total_calories=Sum("total_calories"),
        total_protein=Sum("total_protein"),
        total_carbs=Sum("total_carbs"),
        total_fat=Sum("total_fat"),
    )

    monthly_habits = HabitProgress.objects.filter(
        habit__user=user, date__range=[month_start, month_end]
    ).aggregate(
        completed_count=Count("id", filter=Q(completed=True)), total_count=Count("id")
    )

    summary_data = {
        "total_workouts": user_stats.total_workouts,
        "total_habits_completed": user_stats.total_habits_completed,
        "total_calories_consumed": user_stats.total_calories_consumed,
        "total_calories_burned": user_stats.total_calories_burned,
        "current_streak": user_stats.current_streak,
        "longest_streak": user_stats.longest_streak,
        "weekly_progress": {
            "workouts": weekly_workouts,
            "nutrition": weekly_nutrition,
            "habits": weekly_habits,
        },
        "monthly_progress": {
            "workouts": monthly_workouts,
            "nutrition": monthly_nutrition,
            "habits": monthly_habits,
        },
    }

    serializer = StatsSummarySerializer(summary_data)
    return Response(serializer.data)


# Vistas adicionales para funcionalidades específicas
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    """Vista del dashboard principal - versión API"""
    from .services import StatsService, NutritionStatsService
    
    user = request.user
    
    # Obtener estadísticas básicas
    stats = StatsService.get_user_stats(user)
    
    # Obtener progreso semanal
    weekly_progress = StatsService.get_weekly_progress(user, weeks_back=4)
    
    # Obtener resumen nutricional de hoy
    today_nutrition = NutritionStatsService.get_daily_nutrition_summary(user)
    
    dashboard_data = {
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        },
        'stats': {
            'total_workouts': stats.total_workouts,
            'total_habits_completed': stats.total_habits_completed,
            'current_streak': stats.current_streak,
        },
        'weekly_progress': weekly_progress,
        'today_nutrition': today_nutrition,
    }
    
    return Response(dashboard_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def habit_progress_view(request, habit_id):
    """Vista para ver progreso de un hábito específico"""
    from apps.habits.models import Habit
    from .services import HabitProgressService
    from datetime import date, timedelta
    
    try:
        habit = Habit.objects.get(id=habit_id, user=request.user)
    except Habit.DoesNotExist:
        return Response({'error': 'Hábito no encontrado'}, status=404)
    
    # Calcular tasa de completación
    completion_rate = HabitProgressService.get_habit_completion_rate(habit)
    
    # Obtener progreso de los últimos 30 días
    today = date.today()
    start_date = today - timedelta(days=30)
    
    progress_data = []
    for i in range(30):
        check_date = start_date + timedelta(days=i)
        try:
            progress = habit.progress.get(date=check_date)
            progress_data.append({
                'date': check_date.isoformat(),
                'completed': progress.completed,
                'actual_value': progress.actual_value,
            })
        except:
            progress_data.append({
                'date': check_date.isoformat(),
                'completed': False,
                'actual_value': 0,
            })
    
    response_data = {
        'habit': {
            'id': habit.id,
            'title': habit.title,
            'kind': habit.kind,
            'target_value': habit.target_value,
            'color_hex': habit.color_hex,
        },
        'completion_rate': completion_rate,
        'progress_data': progress_data,
    }
    
    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def mark_habit_completed_view(request, habit_id):
    """Vista para marcar un hábito como completado"""
    from apps.habits.models import Habit
    from .services import HabitProgressService
    from datetime import datetime
    
    try:
        habit = Habit.objects.get(id=habit_id, user=request.user)
    except Habit.DoesNotExist:
        return Response({'error': 'Hábito no encontrado'}, status=404)
    
    try:
        date_completed = request.data.get('date')
        actual_value = request.data.get('actual_value')
        
        if date_completed:
            date_completed = datetime.strptime(date_completed, '%Y-%m-%d').date()
        
        progress = HabitProgressService.mark_habit_completed(
            habit, date_completed, actual_value
        )
        
        return Response({
            'success': True,
            'message': 'Hábito marcado como completado',
            'progress': {
                'id': progress.id,
                'date': progress.date.isoformat(),
                'completed': progress.completed,
                'actual_value': progress.actual_value,
            }
        })
        
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def mark_habit_incomplete_view(request, habit_id):
    """Vista para marcar un hábito como incompleto"""
    from apps.habits.models import Habit
    from .services import HabitProgressService
    from datetime import datetime
    
    try:
        habit = Habit.objects.get(id=habit_id, user=request.user)
    except Habit.DoesNotExist:
        return Response({'error': 'Hábito no encontrado'}, status=404)
    
    try:
        date_incomplete = request.data.get('date')
        
        if date_incomplete:
            date_incomplete = datetime.strptime(date_incomplete, '%Y-%m-%d').date()
        
        progress = HabitProgressService.mark_habit_incomplete(habit, date_incomplete)
        
        if progress:
            return Response({
                'success': True,
                'message': 'Hábito marcado como incompleto',
                'progress': {
                    'id': progress.id,
                    'date': progress.date.isoformat(),
                    'completed': progress.completed,
                    'actual_value': progress.actual_value,
                }
            })
        else:
            return Response({
                'success': True,
                'message': 'No había progreso registrado para esta fecha'
            })
        
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(['GET'])
@permission_classes([])
def health_check(request):
    """
    Endpoint de salud para verificar que la API esté funcionando
    """
    try:
        # Verificar conexión a la base de datos
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        return Response({
            'status': 'healthy',
            'database': 'connected',
            'debug': settings.DEBUG,
            'timestamp': '2025-08-25T15:30:00Z'
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': '2025-08-25T15:30:00Z'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
