import requests


def fetch_routes():
    response = requests.get(
        "https://api-v3.mbta.com/routes?sort=type&filter%5Btype%5D=0%2C1"
    )

    routes = response.json()["data"]

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


def get_route_choice(routes):
    maximum_choice = len(routes)
    route_choice = input(
        "Please enter a number between 1 and {}: ".format(maximum_choice)
    )

    try:
        route_choice_number = int(route_choice)
    except ValueError:
        print("Input must be an integer")
        return get_route_choice(routes)

    if route_choice_number <= 0 or route_choice_number > maximum_choice:
        return get_route_choice(routes)

    return routes[route_choice_number - 1]


def print_route_list(routes):
    for route_index, route_name in enumerate(routes):
        print("{}) {}".format(route_index + 1, route_name["name"]))


def print_route_direction_options(route):
    print(" ")
    print("Please select a {} direction:".format(route["name"]))
    print(" ")
    route_direction_options = route["directions"]
    for direction_index, direction_name in enumerate(route_direction_options):
        print("{}) {}".format(direction_index + 1, direction_name))


def get_direction_choice_index(direction_options):
    maximum_choice = len(direction_options)
    direction_choice = input(
        "Please enter a number between 1 and {}: ".format(maximum_choice)
    )

    try:
        direction_choice_number = int(direction_choice)
    except ValueError:
        print("Input must be an integer")
        return get_direction_choice(direction_options)

    if direction_choice_number <= 0 or direction_choice_number > maximum_choice:
        return get_direction_choice(direction_options)

    return direction_choice_number - 1
