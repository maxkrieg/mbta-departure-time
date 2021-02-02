import requests
from pprint import pprint


def get_routes():
    response = requests.get(
        "https://api-v3.mbta.com/routes?sort=type&filter%5Btype%5D=0%2C1"
    )

    routes = response.json()["data"]

    formatted_routes = [
        {
            "name": route["attributes"]["long_name"],
            "direction_names": route["attributes"]["direction_names"],
        }
        for route in routes
    ]

    pprint(formatted_routes)
