import requests

# from pprint import pprint

# Url for getting Red line stop in direction index 1
# "https://api-v3.mbta.com/stops?filter%5Bdirection_id%5D=1&filter%5Broute%5D=Red"


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

    return formatted_routes
