"""
Servicios para estadísticas de FitTracker
"""
from datetime import date, timedelta
from decimal import Decimal
from django.db.models import Sum, Count, Avg
from django.utils import timezone

from apps.habits.models import Habit
from apps.workouts.models import Workout
from apps.nutrition.models import Nutrition
from apps.stats.models import UserStats, HabitProgress, WorkoutStats, NutritionStats


class StatsService:
    """Servicio para calcular estadísticas del usuario"""
    
    @staticmethod
    def get_user_stats(user):
        """Obtiene o crea estadísticas del usuario"""
        stats, created = UserStats.objects.get_or_create(user=user)
        return stats
    
    @staticmethod
    def update_user_stats(user):
        """Actualiza las estadísticas del usuario"""
        stats = StatsService.get_user_stats(user)
        
        # Calcular totales
        stats.total_workouts = Workout.objects.filter(user=user).count()
        stats.total_habits_completed = HabitProgress.objects.filter(
            habit__user=user, completed=True
        ).count()
        
        # Calcular streak actual
        stats.current_streak = StatsService.calculate_current_streak(user)
        
        stats.save()
        return stats
    
    @staticmethod
    def calculate_current_streak(user):
        """Calcula el streak actual de hábitos completados"""
        today = date.today()
        streak = 0
        
        # Verificar días consecutivos hacia atrás
        for i in range(30):  # Máximo 30 días hacia atrás
            check_date = today - timedelta(days=i)
            completed_today = HabitProgress.objects.filter(
                habit__user=user,
                date=check_date,
                completed=True
            ).exists()
            
            if completed_today:
                streak += 1
            else:
                break
        
        return streak
    
    @staticmethod
    def get_weekly_progress(user, weeks_back=4):
        """Obtiene progreso semanal de los últimos N semanas"""
        today = date.today()
        weekly_data = []
        
        for week in range(weeks_back):
            week_start = today - timedelta(weeks=week, days=today.weekday())
            week_end = week_start + timedelta(days=6)
            
            # Hábitos completados en la semana
            habits_completed = HabitProgress.objects.filter(
                habit__user=user,
                date__range=[week_start, week_end],
                completed=True
            ).count()
            
            # Entrenamientos en la semana
            workouts_count = Workout.objects.filter(
                user=user,
                date__range=[week_start, week_end]
            ).count()
            
            # Calorías quemadas en la semana
            calories_burned = Workout.objects.filter(
                user=user,
                date__range=[week_start, week_end]
            ).aggregate(total=Sum('calories'))['total'] or 0
            
            weekly_data.append({
                'week': week_start.strftime('%Y-%m-%d'),
                'habits_completed': habits_completed,
                'workouts_count': workouts_count,
                'calories_burned': calories_burned,
            })
        
        return list(reversed(weekly_data))
    
    @staticmethod
    def get_monthly_progress(user, months_back=6):
        """Obtiene progreso mensual de los últimos N meses"""
        today = date.today()
        monthly_data = []
        
        for month in range(months_back):
            # Calcular primer día del mes
            if today.month - month <= 0:
                year = today.year - 1
                month_num = 12 + (today.month - month)
            else:
                year = today.year
                month_num = today.month - month
            
            month_start = date(year, month_num, 1)
            
            # Calcular último día del mes
            if month_num == 12:
                next_month = date(year + 1, 1, 1)
            else:
                next_month = date(year, month_num + 1, 1)
            month_end = next_month - timedelta(days=1)
            
            # Hábitos completados en el mes
            habits_completed = HabitProgress.objects.filter(
                habit__user=user,
                date__range=[month_start, month_end],
                completed=True
            ).count()
            
            # Entrenamientos en el mes
            workouts_count = Workout.objects.filter(
                user=user,
                date__range=[month_start, month_end]
            ).count()
            
            # Calorías quemadas en el mes
            calories_burned = Workout.objects.filter(
                user=user,
                date__range=[month_start, month_end]
            ).aggregate(total=Sum('calories'))['total'] or 0
            
            monthly_data.append({
                'month': month_start.strftime('%Y-%m'),
                'habits_completed': habits_completed,
                'workouts_count': workouts_count,
                'calories_burned': calories_burned,
            })
        
        return list(reversed(monthly_data))


class HabitProgressService:
    """Servicio para manejar progreso de hábitos"""
    
    @staticmethod
    def mark_habit_completed(habit, date_completed=None, actual_value=None):
        """Marca un hábito como completado para una fecha específica"""
        if date_completed is None:
            date_completed = date.today()
        
        if actual_value is None:
            actual_value = habit.target_value
        
        progress, created = HabitProgress.objects.get_or_create(
            habit=habit,
            date=date_completed,
            defaults={
                'actual_value': actual_value,
                'completed': True,
            }
        )
        
        if not created:
            progress.actual_value = actual_value
            progress.completed = True
            progress.save()
        
        # Actualizar estadísticas del usuario
        StatsService.update_user_stats(habit.user)
        
        return progress
    
    @staticmethod
    def mark_habit_incomplete(habit, date_incomplete=None):
        """Marca un hábito como incompleto para una fecha específica"""
        if date_incomplete is None:
            date_incomplete = date.today()
        
        try:
            progress = HabitProgress.objects.get(
                habit=habit,
                date=date_incomplete
            )
            progress.completed = False
            progress.save()
            
            # Actualizar estadísticas del usuario
            StatsService.update_user_stats(habit.user)
            
            return progress
        except HabitProgress.DoesNotExist:
            return None
    
    @staticmethod
    def get_habit_completion_rate(habit, days_back=30):
        """Calcula la tasa de completación de un hábito"""
        today = date.today()
        start_date = today - timedelta(days=days_back)
        
        total_days = HabitProgress.objects.filter(
            habit=habit,
            date__range=[start_date, today]
        ).count()
        
        completed_days = HabitProgress.objects.filter(
            habit=habit,
            date__range=[start_date, today],
            completed=True
        ).count()
        
        if total_days == 0:
            return 0.0
        
        return (completed_days / total_days) * 100


class NutritionStatsService:
    """Servicio para estadísticas de nutrición"""
    
    @staticmethod
    def get_daily_nutrition_summary(user, target_date=None):
        """Obtiene resumen nutricional diario"""
        if target_date is None:
            target_date = date.today()
        
        nutrition_entries = Nutrition.objects.filter(
            user=user,
            date=target_date
        )
        
        summary = nutrition_entries.aggregate(
            total_calories=Sum('calories'),
            total_protein=Sum('protein_g'),
            total_carbs=Sum('carbs_g'),
            total_fat=Sum('fat_g'),
            entry_count=Count('id')
        )
        
        return {
            'date': target_date.isoformat(),
            'total_calories': summary['total_calories'] or 0,
            'total_protein_g': float(summary['total_protein'] or 0),
            'total_carbs_g': float(summary['total_carbs'] or 0),
            'total_fat_g': float(summary['total_fat'] or 0),
            'entry_count': summary['entry_count'],
            'entries': list(nutrition_entries.values('id', 'name', 'calories'))
        }
    
    @staticmethod
    def get_weekly_nutrition_average(user, weeks_back=4):
        """Obtiene promedio nutricional semanal"""
        today = date.today()
        weekly_averages = []
        
        for week in range(weeks_back):
            week_start = today - timedelta(weeks=week, days=today.weekday())
            week_end = week_start + timedelta(days=6)
            
            weekly_stats = Nutrition.objects.filter(
                user=user,
                date__range=[week_start, week_end]
            ).aggregate(
                avg_calories=Avg('calories'),
                avg_protein=Avg('protein_g'),
                avg_carbs=Avg('carbs_g'),
                avg_fat=Avg('fat_g'),
                total_entries=Count('id')
            )
            
            weekly_averages.append({
                'week': week_start.strftime('%Y-%m-%d'),
                'avg_calories': round(weekly_stats['avg_calories'] or 0, 1),
                'avg_protein_g': round(float(weekly_stats['avg_protein'] or 0), 1),
                'avg_carbs_g': round(float(weekly_stats['avg_carbs'] or 0), 1),
                'avg_fat_g': round(float(weekly_stats['avg_fat'] or 0), 1),
                'total_entries': weekly_stats['total_entries']
            })
        
        return list(reversed(weekly_averages))
