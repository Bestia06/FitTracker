from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.utils import timezone

from .models import Notification
from .serializers import NotificationSerializer, NotificationCreateSerializer


class NotificationListCreateView(generics.ListCreateAPIView):
    """Listar y crear notificaciones"""
    
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['notification_type', 'status', 'is_important']
    ordering_fields = ['created_at', 'scheduled_time']
    ordering = ['-created_at']
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NotificationCreateSerializer
        return NotificationSerializer


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Ver, actualizar y eliminar notificación"""
    
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_notification_read(request, pk):
    """Marcar notificación como leída"""
    try:
        notification = Notification.objects.get(
            id=pk, 
            user=request.user
        )
        notification.mark_as_read()
        return Response({
            'success': True,
            'message': 'Notificación marcada como leída'
        })
    except Notification.DoesNotExist:
        return Response({
            'error': 'Notificación no encontrada'
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_notification_dismissed(request, pk):
    """Marcar notificación como descartada"""
    try:
        notification = Notification.objects.get(
            id=pk, 
            user=request.user
        )
        notification.mark_as_dismissed()
        return Response({
            'success': True,
            'message': 'Notificación descartada'
        })
    except Notification.DoesNotExist:
        return Response({
            'error': 'Notificación no encontrada'
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_all_notifications_read(request):
    """Marcar todas las notificaciones como leídas"""
    unread_notifications = Notification.objects.filter(
        user=request.user,
        status='unread'
    )
    count = unread_notifications.count()
    unread_notifications.update(
        status='read',
        read_at=timezone.now()
    )
    
    return Response({
        'success': True,
        'message': f'{count} notificaciones marcadas como leídas'
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notification_count(request):
    """Obtener conteo de notificaciones no leídas"""
    unread_count = Notification.objects.filter(
        user=request.user,
        status='unread'
    ).count()
    
    return Response({
        'unread_count': unread_count
    })
