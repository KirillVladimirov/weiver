from weiver.utils.gps import Coordinates
from typing import NamedTuple
from enum import Enum
import requests
import json
from json.decoder import JSONDecodeError
from weiver.exceptions import ApiServiceError


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
    is_day: bool
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    weather_response = _get_weather_response(coordinates)
    weather = _parse_weather_response(weather_response)
    return weather


def _get_weather_response(coordinates: Coordinates):
    q = ",".join([str(coordinates.longitude), str(coordinates.latitude)])
    weather_api_key = "a8dab6f673ea4667b44221602220806"
    weather_url = f"https://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={q}&aqi=no"
    response = requests.get(weather_url)
    if response.status_code != 200:
        raise ApiServiceError
    return response


def _parse_weather_response(service_output: requests.Response) -> Weather:
    try:
        weather_dict = json.loads(service_output.text)
    except JSONDecodeError:
        raise ApiServiceError
    return Weather(
        temperature=_parse_temperature(weather_dict),
        weather_type=_parse_weather_type(weather_dict),
        is_day=_parse_day(weather_dict),
        city=_parse_city(weather_dict)
    )


def _parse_temperature(weather_dict: dict) -> Celsius:
    return round(weather_dict['current']['temp_c'])


def _parse_city(weather_dict: dict) -> str:
    return weather_dict['location']['name']


def _parse_weather_type(weather_dict: dict) -> WeatherType:
    try:
        weather_text = weather_dict['current']['condition']['text']
    except Exception:
        raise ApiServiceError
    values = set(item.value for item in WeatherType)
    if weather_text not in values:
        raise ApiServiceError
    return WeatherType(weather_text)


def _parse_day(weather_dict: dict) -> bool:
    return bool(weather_dict['current']['is_day'])

# {
#     'location': {
#         'name': 'Moskau',
#         'region': 'Moscow City',
#         'country': 'Russia',
#         'lat': 55.75,
#         'lon': 37.62,
#         'tz_id': 'Europe/Moscow',
#         'localtime_epoch': 1654904326,
#         'localtime': '2022-06-11 2:38'
#     },
#     'current': {
#         'last_updated_epoch': 1654903800,
#         'last_updated': '2022-06-11 02:30',
#         'temp_c': 15.0,
#         'temp_f': 59.0,
#         'is_day': 0,
#         'condition': {
#             'text': 'Clear',
#             'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png',
#             'code': 1000
#         },
#         'wind_mph': 2.2,
#         'wind_kph': 3.6,
#         'wind_degree': 333,
#         'wind_dir': 'NNW',
#         'pressure_mb': 1015.0,
#         'pressure_in': 29.97,
#         'precip_mm': 0.0,
#         'precip_in': 0.0,
#         'humidity': 82,
#         'cloud': 0,
#         'feelslike_c': 15.7,
#         'feelslike_f': 60.2,
#         'vis_km': 10.0,
#         'vis_miles': 6.0,
#         'uv': 1.0,
#         'gust_mph': 4.9,
#         'gust_kph': 7.9
#     }
# }
