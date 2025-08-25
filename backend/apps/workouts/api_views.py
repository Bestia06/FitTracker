# workout/api_views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Workout
from .serializers import WorkoutSerializer, WorkoutCreateSerializer

class WorkoutListCreateView(generics.ListCreateAPIView):
    """Listar y crear entrenamientos"""
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['date', 'workout_type']
    ordering_fields = ['date', 'created_at']
    ordering = ['-date', '-created_at']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WorkoutCreateSerializer
        return WorkoutSerializer
    
    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

class WorkoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Ver, actualizar y eliminar entrenamiento"""
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)