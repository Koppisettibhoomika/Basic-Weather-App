import requests
import json
api_key ="61c6a6e3b0f650f495f2634d1e876fbd"  

loc = input("Enter city name: ")

url = "http://api.openweathermap.org/data/2.5/weather"

params = {
    'q': loc,
    'appid': api_key,
    'units': 'metric'  
}

try:
    response = requests.get(url, params=params)  

    data = response.json()

    if 'message' in data:
        print(f"Error: {data['message']}")
    else:
        print("\nCurrent Weather:")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
except Exception as e:
    print(f"Error fetching weather data: {str(e)}")
