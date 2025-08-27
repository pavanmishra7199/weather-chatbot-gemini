import requests
import math
import pytz
from datetime import datetime
from duckduckgo_search import DDGS

from dotenv import load_dotenv
import os
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Weather tool
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    r = requests.get(url).json()
    if r.get("cod") != 200:
        return "❌ Could not fetch weather. Check city name."
    temp = r["main"]["temp"]
    desc = r["weather"][0]["description"]
    return f"🌦️ Weather in {city}: {temp}°C, {desc}"

# Calculator tool
def calculate(expression: str):
    try:
        return f"🧮 Result: {eval(expression, {'__builtins__': None}, math.__dict__)}"
    except:
        return "❌ Invalid calculation."

# Timezone tool
def get_time(zone: str):
    try:
        tz = pytz.timezone(zone)
        return f"⏰ Time in {zone}: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}"
    except:
        return "❌ Invalid timezone."

# Internet search tool
def web_search(query: str):
    try:
        results = DDGS().text(query, max_results=2)
        if not results:
            return "❌ No search results."
        return "🔍 " + " | ".join([r["title"] + ": " + r["href"] for r in results])
    except:
        return "❌ Search failed."
