from weiver.api_service import Weather


def format_weather(weather: Weather) -> str:
    return (f"{weather.city}, {'day' if weather.is_day else 'night'}\n"
            f"{weather.weather_type.value}, temperature {weather.temperature}C")
