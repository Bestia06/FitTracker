from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin para el modelo Notification"""
    
    list_display = [
        'id', 
        'user', 
        'title', 
        'notification_type', 
        'status', 
        'is_important',
        'created_at'
    ]
    list_filter = [
        'notification_type', 
        'status', 
        'is_important', 
        'created_at'
    ]
    search_fields = ['title', 'message', 'user__username', 'user__email']
    readonly_fields = ['created_at', 'updated_at', 'read_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('user', 'title', 'message', 'notification_type')
        }),
        ('Estado', {
            'fields': ('status', 'is_important', 'scheduled_time', 'read_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
