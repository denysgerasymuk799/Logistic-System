from geopy.geocoders import Nominatim
from math import radians, sin, cos, acos


def price_for_transport(city1, city2):
    """
    (str, str) -> int
    Return: a distance between two cities
    """
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode(city1)

    slat = radians(location.latitude)
    slon = radians(location.longitude)

    location = geolocator.geocode(city2)

    elat = radians(location.latitude)
    elon = radians(location.longitude)

    dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    dist += dist * 0.12
    return dist
