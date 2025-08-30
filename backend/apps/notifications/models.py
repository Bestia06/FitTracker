from django.db import models
from apps.accounts.models import User


class Notification(models.Model):
    """
    Modelo para notificaciones del usuario
    """
    NOTIFICATION_TYPES = [
        ('reminder', 'Reminder'),
        ('achievement', 'Achievement'),
        ('workout', 'Workout'),
        ('nutrition', 'Nutrition'),
        ('habit', 'Habit'),
        ('general', 'General'),
    ]
    
    STATUS_CHOICES = [
        ('unread', 'Unread'),
        ('read', 'Read'),
        ('dismissed', 'Dismissed'),
    ]
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='notifications'
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(
        max_length=20, 
        choices=NOTIFICATION_TYPES,
        default='general'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='unread'
    )
    is_important = models.BooleanField(default=False)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    read_at = models.DateTimeField(null=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['user', 'status']),
            models.Index(fields=['notification_type']),
        ]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    def mark_as_read(self):
        """Marcar notificación como leída"""
        from django.utils import timezone
        self.status = 'read'
        self.read_at = timezone.now()
        self.save()
    
    def mark_as_dismissed(self):
        """Marcar notificación como descartada"""
        self.status = 'dismissed'
        self.save()
