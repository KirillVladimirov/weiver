from weiver.utils.gps import get_coordinates
from weiver.api_service import get_weather
from weiver.utils.weather_formater import format_weather


def main():
    coordinates = get_coordinates()
    print(coordinates)
    weather = get_weather(coordinates)
    print(weather)
    print(format_weather(weather))


if __name__ == "__main__":
    main()
