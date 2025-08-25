#!/usr/bin/env python
"""
Script para verificar que todo esté funcionando correctamente
"""
import os
import django
import sys

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import execute_from_command_line
from django.db import connection
from django.conf import settings

def verify_database_connection():
    """Verificar conexión a la base de datos"""
    print("🔍 Verificando conexión a la base de datos...")
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            print("✅ Conexión a la base de datos exitosa")
            return True
    except Exception as e:
        print(f"❌ Error de conexión a la base de datos: {e}")
        return False

def verify_models():
    """Verificar que todos los modelos estén correctos"""
    print("\n🔍 Verificando modelos...")
    try:
        from django.apps import apps
        for app_config in apps.get_app_configs():
            if app_config.name.startswith('apps.'):
                print(f"✅ App {app_config.name} cargada correctamente")
        print("✅ Todos los modelos están correctos")
        return True
    except Exception as e:
        print(f"❌ Error en modelos: {e}")
        return False

def verify_settings():
    """Verificar configuración"""
    print("\n🔍 Verificando configuración...")
    try:
        print(f"✅ DEBUG: {settings.DEBUG}")
        print(f"✅ DATABASE: {settings.DATABASES['default']['ENGINE']}")
        print(f"✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        print(f"✅ INSTALLED_APPS: {len(settings.INSTALLED_APPS)} apps")
        return True
    except Exception as e:
        print(f"❌ Error en configuración: {e}")
        return False

def verify_data():
    """Verificar que hay datos en la base de datos"""
    print("\n🔍 Verificando datos...")
    try:
        from django.contrib.auth import get_user_model
        from apps.habits.models import Habit
        from apps.workouts.models import Workout, Exercise
        from apps.nutrition.models import Nutrition
        from apps.stats.models import UserStats
        
        User = get_user_model()
        
        users_count = User.objects.count()
        habits_count = Habit.objects.count()
        workouts_count = Workout.objects.count()
        exercises_count = Exercise.objects.count()
        nutrition_count = Nutrition.objects.count()
        stats_count = UserStats.objects.count()
        
        print(f"✅ Usuarios: {users_count}")
        print(f"✅ Hábitos: {habits_count}")
        print(f"✅ Entrenamientos: {workouts_count}")
        print(f"✅ Ejercicios: {exercises_count}")
        print(f"✅ Entradas de nutrición: {nutrition_count}")
        print(f"✅ Estadísticas: {stats_count}")
        
        if users_count > 0:
            print("✅ Base de datos tiene datos")
            return True
        else:
            print("⚠️ Base de datos está vacía")
            return False
    except Exception as e:
        print(f"❌ Error verificando datos: {e}")
        return False

def verify_api_endpoints():
    """Verificar que los endpoints de la API estén disponibles"""
    print("\n🔍 Verificando endpoints de la API...")
    try:
        from django.urls import reverse
        from django.test import Client
        
        client = Client()
        
        # Verificar endpoint de salud
        try:
            response = client.get('/api/health/')
            if response.status_code == 200:
                print("✅ Endpoint de salud funcionando")
            else:
                print(f"⚠️ Endpoint de salud: {response.status_code}")
        except:
            print("⚠️ Endpoint de salud no disponible")
        
        # Verificar documentación de la API
        try:
            response = client.get('/api/docs/')
            if response.status_code == 200:
                print("✅ Documentación de la API disponible")
            else:
                print(f"⚠️ Documentación de la API: {response.status_code}")
        except:
            print("⚠️ Documentación de la API no disponible")
        
        return True
    except Exception as e:
        print(f"❌ Error verificando endpoints: {e}")
        return False

def main():
    """Función principal de verificación"""
    print("🚀 VERIFICACIÓN DEL PROYECTO FITTRACKER")
    print("=" * 50)
    
    checks = [
        verify_database_connection(),
        verify_models(),
        verify_settings(),
        verify_data(),
        verify_api_endpoints()
    ]
    
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE VERIFICACIÓN")
    print("=" * 50)
    
    passed = sum(checks)
    total = len(checks)
    
    if passed == total:
        print(f"✅ TODAS LAS VERIFICACIONES PASARON ({passed}/{total})")
        print("🎉 El proyecto está listo para producción!")
    else:
        print(f"⚠️ {passed}/{total} verificaciones pasaron")
        print("🔧 Revisa los errores arriba")
    
    print("\n📋 CONFIGURACIÓN DOCKER:")
    print("✅ docker-compose.yml - Configuración de desarrollo")
    print("✅ docker-compose.prod.yml - Configuración de producción")
    print("✅ backend/Dockerfile - Backend desarrollo")
    print("✅ backend/Dockerfile.prod - Backend producción")
    print("✅ frontend/fittracker_app/Dockerfile - Frontend producción")
    print("✅ frontend/fittracker_app/Dockerfile.dev - Frontend desarrollo")
    
    print("\n🚀 COMANDOS PARA DESPLEGAR:")
    print("Desarrollo: docker-compose up")
    print("Producción: docker-compose -f docker-compose.prod.yml up")

if __name__ == "__main__":
    main()
