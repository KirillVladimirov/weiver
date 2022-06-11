from weiver.utils.gps import get_coordinates
from weiver.api_service import get_weather
from weiver.utils.weather_formater import format_weather
from weiver.exceptions import CantGetCoordinates, ApiServiceError
from weiver.utils.history import save_weather, JSONFileWeatherStorage
from pathlib import Path


def main():
    try:
        coordinates = get_coordinates()
    except CantGetCoordinates:
        print("Cant get GPS coordinates.")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print("Cant get weather from the service.")
        exit(1)
    print(format_weather(weather))
    save_weather(weather, JSONFileWeatherStorage(Path.cwd() / "history.json"))


if __name__ == "__main__":
    main()
