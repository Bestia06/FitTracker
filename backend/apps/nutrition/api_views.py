# nutrition/api_views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Nutrition
from .serializers import NutritionSerializer

class NutritionListCreateView(generics.ListCreateAPIView):
    """Listar y crear entradas nutricionales"""
    serializer_class = NutritionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'created_at']
    ordering = ['-date', '-created_at']
    
    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)

class NutritionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Ver, actualizar y eliminar entrada nutricional"""
    serializer_class = NutritionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)