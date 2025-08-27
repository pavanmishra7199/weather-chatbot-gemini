Weather Chatbot with Gemini
This is a simple yet powerful weather chatbot built using Python's FastAPI framework and integrated with the Gemini API for natural language understanding and conversation. It uses a weather API to fetch real-time weather data based on user queries.

Features
Natural Language Processing: The chatbot understands conversational queries thanks to the Gemini API.

Weather Information: Fetches current weather conditions for a specified city.

Dynamic Tool Use: Intelligently uses specific tools (functions) to retrieve data, such as weather information, time, and general web search.

Simple Web Interface: A basic HTML/JavaScript frontend for easy user interaction.

Project Structure
main.py: The core FastAPI application that defines the API endpoints and integrates with the Gemini model.

tools.py: Contains a set of functions (tools) that the Gemini model can call to perform specific tasks, like get_weather or get_time.

index.html: The frontend user interface for the chatbot.

requirements.txt: A list of all Python dependencies required to run the application.

.env: A file to store your API keys securely.

Getting Started
Prerequisites
A Python 3.8+ environment.

An API key for the Google Gemini API.

An API key for a weather service. This project uses a weather API that can be accessed with a key. You can sign up for a free tier at services like OpenWeatherMap or WeatherAPI.com.

Installation
Clone the repository:

git clone https://github.com/pavanmishra7199/weather-chatbot-gemini.git
cd weather-chatbot-gemini

Install the dependencies:

pip install -r requirements.txt

Configuration
Create a .env file in the root directory of your project and add your API keys.

GEMINI_API_KEY=your_gemini_api_key_here
WEATHER_API_KEY=your_weather_api_key_here

Note: Do not commit this file to your Git repository. It contains sensitive information.

Running the Application
Start the FastAPI application using uvicorn:

uvicorn main:app --reload

The --reload flag is for development and will automatically restart the server when you make code changes.

Open your web browser and navigate to http://127.0.0.1:8000/. You should see the chatbot interface.

Usage
Simply type a weather-related query into the chat box, and the chatbot will respond. For example:

"What's the weather in New York?"

"Tell me about the weather in London right now."

"What's the temperature in Tokyo?"

Tools & Integrations
The chatbot leverages the following Python libraries for its functionality:

fastapi: A modern, fast web framework for building APIs.

uvicorn: An ASGI server to run the FastAPI application.

python-dotenv: To load environment variables from the .env file.

requests: For making HTTP requests to external APIs, like the weather service.

google-generativeai: The official Python SDK for the Google Gemini API.

Contributing
Feel free to open an issue or submit a pull request if you'd like to contribute to this project.
