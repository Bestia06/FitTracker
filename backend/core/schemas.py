"""
Schemas para validación y documentación de la API de FitTracker
"""

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import serializers


# Schemas para documentación de respuestas
class ErrorResponseSchema(serializers.Serializer):
    """Schema para respuestas de error"""

    error = serializers.CharField(help_text="Mensaje de error")
    detail = serializers.CharField(help_text="Detalles del error", required=False)
    code = serializers.CharField(help_text="Código de error", required=False)


class SuccessResponseSchema(serializers.Serializer):
    """Schema para respuestas exitosas"""

    message = serializers.CharField(help_text="Mensaje de éxito")
    data = serializers.DictField(help_text="Datos de la respuesta", required=False)


# Schemas para filtros comunes
class DateRangeFilterSchema(serializers.Serializer):
    """Schema para filtros de rango de fechas"""

    start_date = serializers.DateField(
        help_text="Fecha de inicio (YYYY-MM-DD)", required=False
    )
    end_date = serializers.DateField(
        help_text="Fecha de fin (YYYY-MM-DD)", required=False
    )


class PaginationSchema(serializers.Serializer):
    """Schema para parámetros de paginación"""

    page = serializers.IntegerField(
        help_text="Número de página", default=1, required=False
    )
    page_size = serializers.IntegerField(
        help_text="Elementos por página", default=20, required=False
    )


# Decoradores para documentación
def habit_list_schema():
    """Decorador para documentar listado de hábitos"""
    return extend_schema(
        summary="Listar hábitos",
        description="Obtiene una lista paginada de hábitos del usuario",
        parameters=[
            OpenApiParameter(
                name="kind",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Filtrar por tipo de hábito (daily, weekly, monthly)",
                required=False,
            ),
            OpenApiParameter(
                name="search",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Buscar hábitos por título",
                required=False,
            ),
        ],
        examples=[
            OpenApiExample(
                "Ejemplo de respuesta",
                value={
                    "count": 5,
                    "next": "http://localhost:8000/api/habits/?page=2",
                    "previous": None,
                    "results": [
                        {
                            "id": 1,
                            "title": "Ejercicio diario",
                            "kind": "daily",
                            "target_value": 30.0,
                            "color_hex": "#FF5733",
                            "created_at": "2024-01-01T00:00:00Z",
                        }
                    ],
                },
            )
        ],
    )


def habit_create_schema():
    """Decorador para documentar creación de hábitos"""
    return extend_schema(
        summary="Crear hábito",
        description="Crea un nuevo hábito para el usuario",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Título del hábito"},
                    "kind": {"type": "string", "enum": ["daily", "weekly", "monthly"]},
                    "target_value": {"type": "number", "description": "Valor objetivo"},
                    "color_hex": {
                        "type": "string",
                        "description": "Color en formato hexadecimal",
                    },
                },
                "required": ["title", "kind", "target_value"],
            }
        },
        responses={201: SuccessResponseSchema, 400: ErrorResponseSchema},
    )


def nutrition_list_schema():
    """Decorador para documentar listado de nutrición"""
    return extend_schema(
        summary="Listar entradas nutricionales",
        description="Obtiene una lista paginada de entradas nutricionales",
        parameters=[
            OpenApiParameter(
                name="date",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description="Filtrar por fecha (YYYY-MM-DD)",
                required=False,
            ),
            OpenApiParameter(
                name="min_calories",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description="Calorías mínimas",
                required=False,
            ),
        ],
    )


def workout_list_schema():
    """Decorador para documentar listado de entrenamientos"""
    return extend_schema(
        summary="Listar entrenamientos",
        description="Obtiene una lista paginada de entrenamientos",
        parameters=[
            OpenApiParameter(
                name="workout_type",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Tipo de entrenamiento (cardio, strength, flexibility, sports, other)",
                required=False,
            ),
            OpenApiParameter(
                name="date",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description="Filtrar por fecha (YYYY-MM-DD)",
                required=False,
            ),
        ],
    )


def stats_summary_schema():
    """Decorador para documentar resumen de estadísticas"""
    return extend_schema(
        summary="Obtener resumen de estadísticas",
        description="Obtiene un resumen completo de las estadísticas del usuario",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "total_workouts": {"type": "integer"},
                    "total_habits_completed": {"type": "integer"},
                    "current_streak": {"type": "integer"},
                    "weekly_progress": {"type": "object"},
                    "monthly_progress": {"type": "object"},
                },
            }
        },
    )


# Schemas para validación de entrada
class HabitCreateSchema(serializers.Serializer):
    """Schema para validar creación de hábitos"""

    title = serializers.CharField(max_length=200, help_text="Título del hábito")
    kind = serializers.ChoiceField(
        choices=[("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly")],
        help_text="Tipo de hábito",
    )
    target_value = serializers.FloatField(help_text="Valor objetivo")
    color_hex = serializers.CharField(
        max_length=7, help_text="Color en formato hexadecimal (#RRGGBB)", required=False
    )


class NutritionCreateSchema(serializers.Serializer):
    """Schema para validar creación de entradas nutricionales"""

    name = serializers.CharField(max_length=200, help_text="Nombre del alimento")
    date = serializers.DateField(help_text="Fecha de la entrada")
    calories = serializers.IntegerField(min_value=0, help_text="Calorías")
    protein_g = serializers.DecimalField(
        max_digits=6, decimal_places=2, min_value=0, help_text="Proteína en gramos"
    )
    carbs_g = serializers.DecimalField(
        max_digits=6, decimal_places=2, min_value=0, help_text="Carbohidratos en gramos"
    )
    fat_g = serializers.DecimalField(
        max_digits=6, decimal_places=2, min_value=0, help_text="Grasa en gramos"
    )


class WorkoutCreateSchema(serializers.Serializer):
    """Schema para validar creación de entrenamientos"""

    name = serializers.CharField(max_length=200, help_text="Nombre del entrenamiento")
    date = serializers.DateField(help_text="Fecha del entrenamiento")
    workout_type = serializers.ChoiceField(
        choices=[
            ("cardio", "Cardio"),
            ("strength", "Strength Training"),
            ("flexibility", "Flexibility"),
            ("sports", "Sports"),
            ("other", "Other"),
        ],
        help_text="Tipo de entrenamiento",
    )
    calories = serializers.IntegerField(min_value=0, help_text="Calorías quemadas")
    duration_minutes = serializers.IntegerField(
        min_value=1, help_text="Duración en minutos"
    )
    notes = serializers.CharField(required=False, help_text="Notas adicionales")
