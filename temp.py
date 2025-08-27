import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

if not api_key:
    print("❌ WEATHER_API_KEY not found in environment")
else:
    print(f"✅ API Key found: {api_key[:8]}...")
    
    # Test API call
    url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
