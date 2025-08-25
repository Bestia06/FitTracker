#!/usr/bin/env python
"""
Script de prueba para verificar endpoints principales
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_home_endpoint():
    """Probar endpoint principal"""
    print("🔍 Probando endpoint principal...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Endpoint principal funcionando: {data['message']}")
            return True
        else:
            print(f"❌ Error en endpoint principal: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error conectando al servidor: {e}")
        return False

def test_nutrition_enrich():
    """Probar enriquecimiento de nutrición"""
    print("\n🔍 Probando enriquecimiento de nutrición...")
    try:
        data = {"name": "apple"}
        response = requests.post(
            f"{BASE_URL}/api/nutrition/enrich/",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Enriquecimiento exitoso: {result['message']}")
            print(f"   Fuente: {result['source']}")
            return True
        else:
            print(f"❌ Error en enriquecimiento: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error en enriquecimiento: {e}")
        return False

def test_exercise_enrich():
    """Probar enriquecimiento de ejercicios"""
    print("\n🔍 Probando enriquecimiento de ejercicios...")
    try:
        data = {"name": "push-ups"}
        response = requests.post(
            f"{BASE_URL}/api/workouts/exercises/enrich/",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Enriquecimiento exitoso: {result['message']}")
            print(f"   Fuente: {result['source']}")
            return True
        else:
            print(f"❌ Error en enriquecimiento: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error en enriquecimiento: {e}")
        return False

def test_admin_endpoint():
    """Probar endpoint de admin"""
    print("\n🔍 Probando endpoint de admin...")
    try:
        response = requests.get(f"{BASE_URL}/admin/")
        if response.status_code == 200:
            print("✅ Admin endpoint funcionando")
            return True
        else:
            print(f"❌ Error en admin: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error en admin: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Iniciando pruebas de endpoints...\n")
    
    tests = [
        test_home_endpoint,
        test_nutrition_enrich,
        test_exercise_enrich,
        test_admin_endpoint,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Resultados: {passed}/{total} pruebas exitosas")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron! El backend está funcionando correctamente.")
    else:
        print("⚠️  Algunas pruebas fallaron. Revisar configuración.")

if __name__ == "__main__":
    main()
