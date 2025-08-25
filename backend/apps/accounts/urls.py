"""
URLs for accounts app.
"""

from django.urls import path

from . import api_views

app_name = "accounts"

urlpatterns = [
    # Autenticación
    path("register/", api_views.register_user, name="register"),
    path("login/", api_views.login_user, name="login"),
    path("profile/", api_views.user_profile, name="profile"),
]
