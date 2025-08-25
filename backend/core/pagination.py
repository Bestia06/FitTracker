"""
Paginación personalizada para FitTracker
"""

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class FitTrackerPagination(PageNumberPagination):
    """
    Paginación personalizada para FitTracker
    """

    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100
    page_query_param = "page"

    def get_paginated_response(self, data):
        """
        Respuesta paginada personalizada
        """
        return Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": data,
                "page_info": {
                    "current_page": self.page.number,
                    "total_pages": self.page.paginator.num_pages,
                    "has_next": self.page.has_next(),
                    "has_previous": self.page.has_previous(),
                },
            }
        )


class SmallPagination(PageNumberPagination):
    """
    Paginación para listas pequeñas
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class LargePagination(PageNumberPagination):
    """
    Paginación para listas grandes
    """

    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 200


class HabitPagination(FitTrackerPagination):
    """
    Paginación específica para hábitos
    """

    page_size = 15


class NutritionPagination(FitTrackerPagination):
    """
    Paginación específica para nutrición
    """

    page_size = 25


class WorkoutPagination(FitTrackerPagination):
    """
    Paginación específica para entrenamientos
    """

    page_size = 20


class StatsPagination(FitTrackerPagination):
    """
    Paginación específica para estadísticas
    """

    page_size = 30
