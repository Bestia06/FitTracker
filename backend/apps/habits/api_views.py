from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.shortcuts import get_object_or_404
from datetime import date
from .models import Habit
from .serializers import HabitSerializer
from apps.stats.services import HabitProgressService


class HabitListCreateView(generics.ListCreateAPIView):
    """Listar y crear hábitos"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['kind']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']
    
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Ver, actualizar y eliminar hábito"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_habit_completed(request, pk):
    """Marcar hábito como completado"""
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    
    date_completed = request.data.get('date')
    actual_value = request.data.get('actual_value')
    
    if date_completed:
        from datetime import datetime
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
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_habit_incomplete(request, pk):
    """Marcar hábito como incompleto"""
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    
    date_incomplete = request.data.get('date')
    
    if date_incomplete:
        from datetime import datetime
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
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'success': True,
            'message': 'No había progreso registrado para esta fecha'
        }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_habit_progress(request, pk):
    """Obtener progreso de un hábito"""
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    
    # Calcular tasa de completación
    completion_rate = HabitProgressService.get_habit_completion_rate(habit)
    
    # Obtener progreso de los últimos 30 días
    from datetime import timedelta
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
    
    return Response({
        'habit': {
            'id': habit.id,
            'title': habit.title,
            'kind': habit.kind,
            'target_value': habit.target_value,
            'color_hex': habit.color_hex,
        },
        'completion_rate': completion_rate,
        'progress_data': progress_data,
    }, status=status.HTTP_200_OK)
