"""
URLs for notifications app.
"""

from django.urls import path
from . import api_views

app_name = "notifications"

urlpatterns = [
    # Notificaciones
    path("", api_views.NotificationListCreateView.as_view(), name="notification_list"),
    path(
        "<int:pk>/",
        api_views.NotificationDetailView.as_view(),
        name="notification_detail",
    ),
    # Acciones específicas
    path(
        "<int:pk>/read/",
        api_views.mark_notification_read,
        name="mark_notification_read",
    ),
    path(
        "<int:pk>/dismiss/",
        api_views.mark_notification_dismissed,
        name="mark_notification_dismissed",
    ),
    path(
        "mark-all-read/",
        api_views.mark_all_notifications_read,
        name="mark_all_notifications_read",
    ),
    path(
        "count/",
        api_views.notification_count,
        name="notification_count",
    ),
]
