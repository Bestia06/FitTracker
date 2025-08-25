#!/usr/bin/env python
"""
Script para probar Swagger y endpoints principales
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_swagger_endpoints():
    """Probar endpoints de Swagger"""
    print("🔍 Probando endpoints de Swagger...")
    
    # 1. Probar schema
    try:
        response = requests.get(f"{BASE_URL}/api/schema/")
        if response.status_code == 200:
            print("✅ Schema endpoint funciona")
        else:
            print(f"❌ Schema endpoint falló: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en schema: {e}")
    
    # 2. Probar Swagger UI
    try:
        response = requests.get(f"{BASE_URL}/api/docs/")
        if response.status_code == 200:
            print("✅ Swagger UI funciona")
        else:
            print(f"❌ Swagger UI falló: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en Swagger UI: {e}")
    
    # 3. Probar ReDoc
    try:
        response = requests.get(f"{BASE_URL}/api/redoc/")
        if response.status_code == 200:
            print("✅ ReDoc funciona")
        else:
            print(f"❌ ReDoc falló: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en ReDoc: {e}")

def test_api_endpoints():
    """Probar endpoints principales de la API"""
    print("\n🚀 Probando endpoints principales...")
    
    # 1. Probar home endpoint
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print("✅ Home endpoint funciona")
            print(f"   📝 Mensaje: {data.get('message', 'N/A')}")
        else:
            print(f"❌ Home endpoint falló: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en home endpoint: {e}")
    
    # 2. Probar login JWT
    try:
        login_data = {
            "username": "josep",
            "password": "josep123"
        }
        response = requests.post(f"{BASE_URL}/api/auth/jwt/login/", json=login_data)
        if response.status_code == 200:
            data = response.json()
            access_token = data.get('access')
            print("✅ Login JWT funciona")
            print(f"   🔑 Token obtenido: {access_token[:20]}...")
            return access_token
        else:
            print(f"❌ Login JWT falló: {response.status_code}")
            print(f"   📝 Response: {response.text}")
    except Exception as e:
        print(f"❌ Error en login JWT: {e}")
    
    return None

def test_protected_endpoints(token):
    """Probar endpoints protegidos con token"""
    if not token:
        print("❌ No se puede probar endpoints protegidos sin token")
        return
    
    print(f"\n🔐 Probando endpoints protegidos...")
    headers = {"Authorization": f"Bearer {token}"}
    
    # 1. Probar endpoint de hábitos
    try:
        response = requests.get(f"{BASE_URL}/api/habits/", headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("✅ Endpoint de hábitos funciona")
            print(f"   📊 Total hábitos: {data.get('count', 0)}")
        else:
            print(f"❌ Endpoint de hábitos falló: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en hábitos: {e}")
    
    # 2. Probar endpoint de nutrición
    try:
        response = requests.get(f"{BASE_URL}/api/nutrition/", headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("✅ Endpoint de nutrición funciona")
            print(f"   📊 Total entradas: {data.get('count', 0)}")
        else:
            print(f"❌ Endpoint de nutrición falló: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en nutrición: {e}")
    
    # 3. Probar endpoint de entrenamientos
    try:
        response = requests.get(f"{BASE_URL}/api/workouts/", headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("✅ Endpoint de entrenamientos funciona")
            print(f"   📊 Total entrenamientos: {data.get('count', 0)}")
        else:
            print(f"❌ Endpoint de entrenamientos falló: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en entrenamientos: {e}")
    
    # 4. Probar endpoint de estadísticas
    try:
        response = requests.get(f"{BASE_URL}/api/stats/summary/", headers=headers)
        if response.status_code == 200:
            print("✅ Endpoint de estadísticas funciona")
        else:
            print(f"❌ Endpoint de estadísticas falló: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en estadísticas: {e}")

def main():
    """Función principal"""
    print("🧪 Iniciando pruebas de Swagger y API...\n")
    
    # Probar Swagger
    test_swagger_endpoints()
    
    # Probar endpoints principales
    token = test_api_endpoints()
    
    # Probar endpoints protegidos
    test_protected_endpoints(token)
    
    print("\n🎉 Pruebas completadas!")
    print("\n📋 Resumen:")
    print("   🌐 Swagger UI: http://127.0.0.1:8000/api/docs/")
    print("   📚 ReDoc: http://127.0.0.1:8000/api/redoc/")
    print("   📄 Schema: http://127.0.0.1:8000/api/schema/")
    print("   🏠 Home: http://127.0.0.1:8000/")

if __name__ == "__main__":
    main()
