import requests
from typing import List
from lib.types import Route
from lib.utils import validate_number_choice


def fetch_routes() -> List[Route]:
    """
    Fetches all light and heavy routes from the MBTA API.
    """

    try:
        response = requests.get(
            "https://api-v3.mbta.com/routes?sort=type&filter%5Btype%5D=0%2C1"
        )
        routes = response.json()["data"]
    except Exception:
        return None

    formatted_routes = [
        {
            "id": route["id"],
            "name": route["attributes"]["long_name"],
            "directions": route["attributes"]["direction_names"],
            "type": "light" if route["attributes"]["type"] == 0 else "heavy",
        }
        for route in routes
    ]

    return formatted_routes


def get_route_choice(routes: List[Route]) -> Route:
    """
    Prompts the user to choose a Route from the list of routes.
    """

    maximum_choice = len(routes)
    route_choice = input(
        "Please enter a number between 1 and {}: ".format(maximum_choice)
    )

    route_choice_number = validate_number_choice(maximum_choice, route_choice)
    if route_choice_number is None:
        return get_route_choice(routes)

    return routes[route_choice_number - 1]


def print_route_list(routes: List[Route]):
    for route_index, route_name in enumerate(routes):
        print("{}) {}".format(route_index + 1, route_name["name"]))
