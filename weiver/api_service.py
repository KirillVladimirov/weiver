from weiver.utils.gps import Coordinates
from typing import NamedTuple
from datetime import datetime
from enum import Enum
import requests
import json


Celsius = int


class WeatherType(Enum):
    MIST = 'Mist'
    SUNNY = 'Sunny'
    CLEAR = 'Clear'
    FOG = 'Fog'
    SNOW = 'Snow'
    CLOUD = 'Cloud'


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinate: Coordinates) -> Weather:
    q = ",".join([str(coordinate.longitude), str(coordinate.latitude)])
    weather_api_key = "a8dab6f673ea4667b44221602220806"
    weather_url = f"https://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={q}&aqi=no"
    weather = requests.get(weather_url)
    weather_dict = json.loads(weather.text)
    print(weather_dict)
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLOUD,
        sunrise=datetime.fromisoformat("2022-05-04 04:00:00"),
        sunset=datetime.fromisoformat("2022-05-04 20:00:00"),
        city="Moscow"
    )

