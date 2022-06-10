import requests
from typing import NamedTuple
from weiver.exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    longitude: float
    latitude: float


def get_coordinates() -> Coordinates:
    send_url = "http://ipinfo.io/loc"
    geo_req = requests.get(send_url)
    if geo_req.status_code != 200:
        raise CantGetCoordinates
    longitude, latitude = geo_req.text.strip().split(",")
    return Coordinates(longitude=longitude, latitude=latitude)
