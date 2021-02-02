import requests

# from pprint import pprint


def fetch_stops(route_id, direction_index):
    response = requests.get(
        "https://api-v3.mbta.com/stops?filter%5Bdirection_id%5D={}&filter%5Broute%5D={}".format(
            direction_index, route_id
        )
    )
    stops = response.json()["data"]

    formatted_stops = [
        {"id": stop["id"], "name": stop["attributes"]["name"]} for stop in stops
    ]

    return formatted_stops


def print_stops_list(stops):
    print(" ")
    print("Please select a stop:")
    print(" ")
    for stop_index, stop in enumerate(stops):
        print("{}) {}".format(stop_index + 1, stop["name"]))


def get_stop_choice(stops):
    maximum_choice = len(stops)
    stop_choice = input(
        "Please enter a number between 1 and {}: ".format(maximum_choice)
    )

    try:
        stop_choice_number = int(stop_choice)
    except ValueError:
        print("Input must be an integer")
        return get_stop_choice(stops)

    if stop_choice_number <= 0 or stop_choice_number > maximum_choice:
        return get_stop_choice(stops)

    return stops[stop_choice_number - 1]
