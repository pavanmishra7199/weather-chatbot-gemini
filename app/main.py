import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

import google.generativeai as genai
from app.tools import get_weather, calculate, get_time, web_search

# Load keys
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Init LLM
llm = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message")

    if not user_input:
        return JSONResponse({"response": "Please enter a valid query."})

    # 🔧 Tool selection
    response_text = None
    if "weather" in user_input.lower():
        city = user_input.split("in")[-1].strip()
        response_text = get_weather(city)
    elif any(op in user_input for op in ["+", "-", "*", "/", "sin", "cos"]):
        response_text = calculate(user_input)
    elif "time" in user_input.lower():
        zone = user_input.split("in")[-1].strip()
        response_text = get_time(zone)
    elif "search" in user_input.lower():
        query = user_input.replace("search", "").strip()
        response_text = web_search(query)

    # 🌐 Fallback → Gemini
    if not response_text:
        gemini_response = llm.generate_content(user_input)
        response_text = gemini_response.text

    return JSONResponse({"response": response_text})
