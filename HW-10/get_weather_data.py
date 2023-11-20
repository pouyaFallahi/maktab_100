import requests

def get_weather_data(city_name):
    API_KEY = 'e92abd3ea576142b2768761470dd1d3d'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    params ={
        'q': city_name,
        'appid': API_KEY,
        'units': 'imperial'
    }

    try:
        req = requests.get(URL, params=params)
        req.raise_for_status()
        weather_data = req.json()
        return weather_data

    except requests.exceptions.RequestException as e:
        return f'Error: {e}'
