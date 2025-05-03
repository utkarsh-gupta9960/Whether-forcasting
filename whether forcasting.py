import requests

def get_weather(city):
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = "AIawsSyBUI3dkiUgubCj0fgya4OO95wPy1gyZf3z-oyty"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{http://api.openweathermap.org/data/2.5/weather?}q={"Bhopal"}&appid={"AIawsSyBUI3dkiUgubCj0fgya4OO95wPy1gyZf3z-oyty"}&units=metric"
    
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?")
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        city_name = data["name"]
        temp = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_desc = weather_data["description"]
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_desc.capitalize()}")
    else:
        print("City not found!")

def weather_app():
    print("Welcome to the Weather Forecast Application!")
    while True:
        city = input("\nEnter a city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    weather_app()