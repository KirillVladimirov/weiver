import requests
from typing import NamedTuple
from weiver.exceptions import CantGetCoordinates


USE_ROUND_COORDINATES = False


class Coordinates(NamedTuple):
    longitude: float
    latitude: float


def get_coordinates() -> Coordinates:
    coordinates = _get_ipinfo_coordinates()
    return _round_coordinates(coordinates)


def _get_ipinfo_coordinates() -> Coordinates:
    coordinates_service_url = "http://ipinfo.io/loc"
    service_output = requests.get(coordinates_service_url)
    if service_output.status_code != 200:
        raise CantGetCoordinates
    coordinates = _parse_coordinates(service_output)
    return coordinates


def _parse_coordinates(service_output: requests.Response) -> Coordinates:
    try:
        longitude, latitude = service_output.text.strip().split(",")
    except Exception:
        raise CantGetCoordinates
    return Coordinates(
        longitude=_parse_coordinate(longitude),
        latitude=_parse_coordinate(latitude)
    )


def _parse_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not USE_ROUND_COORDINATES:
        return coordinates
    return Coordinates(*map(lambda x: round(x, 1), [coordinates.longitude, coordinates.latitude]))
