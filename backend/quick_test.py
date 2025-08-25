import requests
import time

def test_api_ninja_endpoints():
    """Probar endpoints de API Ninja"""
    base_url = "http://localhost:8000"
    
    print("🧪 Probando endpoints de API Ninja")
    print("=" * 50)
    
    # Esperar que el servidor inicie
    time.sleep(2)
    
    # Test 1: Endpoint de nutrición
    print("\n🍎 Probando /api/nutrition/enrich/")
    try:
        response = requests.post(
            f"{base_url}/api/nutrition/enrich/",
            json={"name": "apple"},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        print(f"📊 Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Éxito: {data.get('message', 'N/A')}")
            if 'data' in data:
                food_data = data['data']
                print(f"   🔥 Calorías: {food_data.get('calories', 'N/A')}")
                print(f"   🥩 Proteína: {food_data.get('protein_g', 'N/A')}g")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Excepción: {str(e)}")
    
    # Test 2: Endpoint de ejercicios
    print("\n💪 Probando /api/workouts/exercises/search/")
    try:
        response = requests.get(
            f"{base_url}/api/workouts/exercises/search/",
            params={"name": "push-up"},
            timeout=10
        )
        print(f"📊 Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Éxito: {data.get('message', 'N/A')}")
            print(f"   📊 Encontrados: {data.get('count', 0)} ejercicios")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Excepción: {str(e)}")

if __name__ == "__main__":
    test_api_ninja_endpoints()
