import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

# 1. Prueba de POST con datos válidos
def test_post_valid_data():
    print("Probando POST con datos válidos...")
    data = [
        {
            "name": "Toyota Corolla",
            "year": 2015,
            "selling_price": 15000.0,
            "km_driven": 80000,
            "fuel": "Petrol",
            "seller_type": "Individual",
            "transmission": "Manual",
            "owner": "First Owner",
            "mileage": "18 kmpl",
            "engine": "1498 cc",
            "max_power": "100 bhp",
            "torque": "150 Nm",
            "seats": 5
        }
    ]
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 200:
        print("POST con datos válidos: SUCCESS")
    else:
        print(f"POST con datos válidos: FAILED (Response code: {response.status_code})")

# 2. Prueba de POST con lista vacía
def test_post_empty_data():
    print("Probando POST con lista vacía...")
    response = requests.post(BASE_URL, json=[])
    if response.status_code == 400:
        print("POST con lista vacía: SUCCESS")
    else:
        print(f"POST con lista vacía: FAILED (Response code: {response.status_code})")

# 3. Prueba de GET (debe devolver autos insertados anteriormente)
def test_get_cars():
    print("Probando GET...")
    response = requests.get(f"{BASE_URL}?page=1&page_size=10")
    if response.status_code == 200:
        print("GET: SUCCESS")
    else:
        print(f"GET: FAILED (Response code: {response.status_code})")

# 4. Prueba de GET con un año que no existe (debe devolver 404)
def test_get_no_cars():
    print("Probando GET con min_year=2050...")
    response = requests.get(f"{BASE_URL}?page=1&min_year=2050")
    if response.status_code == 404:
        print("GET con min_year=2050: SUCCESS")
    else:
        print(f"GET con min_year=2050: FAILED (Response code: {response.status_code})")

if __name__ == "__main__":
    test_post_valid_data()
    test_post_empty_data()
    test_get_cars()
    test_get_no_cars()
