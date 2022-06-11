from datetime import datetime
from pathlib import Path
from weiver.api_service import Weather
from weiver.utils.weather_formater import format_weather


class WeatherStorage:
    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class PlainFileWeatherStorage(WeatherStorage):
    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self._file, 'a') as f:
            f.write(f"{now}\n{formatted_weather}\n\n")


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    storage.save(weather)




