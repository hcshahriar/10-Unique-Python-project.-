import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

def get_weather(city):
    """Fetch weather data for a city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
        return weather
    else:
        return None

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    weather = get_weather(city)
    
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temp']}°C")
        print(f"Conditions: {weather['description']}")
    else:
        print("City not found or API error.")
