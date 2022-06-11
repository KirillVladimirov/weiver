import json
from datetime import datetime
from pathlib import Path
from weiver.api_service import Weather
from weiver.utils.weather_formater import format_weather
from typing import TypedDict


class HistoryRecord(TypedDict):
    date: str
    weather: str


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


class JSONFileWeatherStorage(WeatherStorage):
    def __init__(self, file: Path):
        self._file = file
        self._init_storage()

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append({
            "date": str(datetime.now()),
            "weather": format_weather(weather)
        })
        self._write(history)

    def _init_storage(self) -> None:
        if not self._file.exists():
            self._file.write_text("[]")

    def _read_history(self) -> list[HistoryRecord]:
        with open(self._file, "r") as f:
            return json.load(f)

    def _write(self, history: list[HistoryRecord]) -> None:
        with open(self._file, "w") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    storage.save(weather)




