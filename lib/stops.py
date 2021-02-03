import requests
from typing import List
from lib.types import Stop
from lib.utils import validate_number_choice


def fetch_stops(route_id: str, direction_index: int) -> List[Stop]:
    """
    Fetches a list of stops for a given route and direction from the MBTA API.
    """

    try:
        response = requests.get(
            "https://api-v3.mbta.com/stops?filter%5Bdirection_id%5D={direction_id}&filter%5Broute%5D={route_id}".format(
                direction_id=direction_index, route_id=route_id
            )
        )
        stops = response.json()["data"]
    except Exception:
        return None

    formatted_stops = [
        {"id": stop["id"], "name": stop["attributes"]["name"]} for stop in stops
    ]

    return formatted_stops


def print_stops_list(stops: List[Stop]):
    """
    Prints out a list of stops.
    """

    for stop_index, stop in enumerate(stops):
        print("{}) {}".format(stop_index + 1, stop["name"]))


def get_stop_choice(stops: List[Stop]) -> Stop:
    """
    Prompts user to select a stop from a list of Stops.
    """

    maximum_choice = len(stops)
    stop_choice = input("Enter a number between 1 and {}: ".format(maximum_choice))

    stop_choice_number = validate_number_choice(maximum_choice, stop_choice)
    if stop_choice_number is None:
        return get_stop_choice(stops)

    return stops[stop_choice_number - 1]
