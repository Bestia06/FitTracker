from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom admin for User model"""

    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "fitness_level",
        "is_active",
    )
    list_filter = ("fitness_level", "is_active", "is_staff", "date_joined")
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("-date_joined",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "FitTracker Info",
            {"fields": ("date_of_birth", "height", "weight", "fitness_level")},
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "FitTracker Info",
            {"fields": ("date_of_birth", "height", "weight", "fitness_level")},
        ),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin for UserProfile model"""

    list_display = ("user", "bio")
    search_fields = ("user__email", "user__username")
