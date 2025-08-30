import os
from datetime import timedelta
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-j0@quqxy!$=3)@j^9afrg7-wy3sqqvhplekm2&403mq9fy4x07",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="127.0.0.1,localhost,testserver",
    cast=lambda v: [s.strip() for s in v.split(",")],
)

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Django REST Framework
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",  # ← NEW: JWT
    # CORS for frontend connection
    "corsheaders",
    # Filters and documentation
    "django_filters",
    "drf_spectacular",  # ← ADDED: Swagger/OpenAPI
    # Your apps
    "apps.accounts",
    "apps.habits",
    "apps.nutrition",
    "apps.workouts",
    "apps.stats",  # ← ADDED: Stats app
    "apps.notifications",  # ← ADDED: Notifications app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # ← Moved up
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database - Flexible configuration with environment variables
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("DB_NAME", default=BASE_DIR / "db.sqlite3"),
        "USER": config("DB_USER", default=""),
        "PASSWORD": config("DB_PASSWORD", default=""),
        "HOST": config("DB_HOST", default=""),
        "PORT": config("DB_PORT", default=""),
    }
}

# Configuration to use custom user model
AUTH_USER_MODEL = "accounts.User"

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Django REST Framework configuration - UPDATED WITH JWT
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",  # ← JWT first
        "rest_framework.authentication.TokenAuthentication",  # ← Fallback
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "core.pagination.FitTrackerPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# JWT CONFIGURATION - NEW
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
}

# API NINJA CONFIGURATION - NEW
API_NINJA_KEY = config(
    "API_NINJA_KEY", default="n6ou0W+GEJfS20DbFPCvWA==3RuTgcuOXRykkFa3"
)
API_NINJA_BASE_URL = config(
    "API_NINJA_BASE_URL", default="https://api.api-ninjas.com/v1"
)

# CORS configuration (for frontend)
CORS_ALLOWED_ORIGINS = config(
    "CORS_ALLOWED_ORIGINS",
    default="http://localhost:3000,http://127.0.0.1:3000,http://localhost:8080,http://127.0.0.1:8080",
    cast=lambda v: [s.strip() for s in v.split(",")],
)

# For development, allow all origins (WARNING: only in production)
CORS_ALLOW_ALL_ORIGINS = config("CORS_ALLOW_ALL_ORIGINS", default=True, cast=bool)

# Internationalization
LANGUAGE_CODE = "es-es"
TIME_ZONE = "America/Santo_Domingo"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "fittracker.log",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

# drf-spectacular configuration for Swagger/OpenAPI
SPECTACULAR_SETTINGS = {
    "TITLE": "FitTracker API",
    "DESCRIPTION": """
    # FitTracker API Documentation
    
    ## Description
    Complete API for fitness tracking, habits, nutrition and workouts.
    
    ## Features
    - 🔐 JWT Authentication
    - 🎯 Habit Management
    - 🍎 Nutrition Tracking
    - 🏋️ Workouts and Exercises
    - 📊 Statistics and Progress
    - 🔗 API Ninja Integration
    
    ## Main Endpoints
    - **Authentication**: `/api/auth/jwt/`
    - **Users**: `/api/accounts/`
    - **Habits**: `/api/habits/`
    - **Nutrition**: `/api/nutrition/`
    - **Workouts**: `/api/workouts/`
    - **Statistics**: `/api/stats/`
    
    ## Authentication
    To use protected endpoints, include the JWT token in the header:
    ```
    Authorization: Bearer <your_jwt_token>
    ```
    """,
    "VERSION": "2.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_SPLIT_REQUEST": True,
    "SCHEMA_PATH_PREFIX": "/api/",
    "TAGS": [
        {"name": "auth", "description": "Authentication and users"},
        {"name": "habits", "description": "Habit management"},
        {"name": "nutrition", "description": "Nutrition tracking"},
        {"name": "workouts", "description": "Workouts and exercises"},
        {"name": "stats", "description": "Statistics and progress"},
        {"name": "api-ninja", "description": "API Ninja integration"},
    ],
    "SECURITY": [
        {
            "Bearer": []
        }
    ],
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
    },
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}
