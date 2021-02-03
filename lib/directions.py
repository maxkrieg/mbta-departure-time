from typing import List
from lib.types import Route


def print_route_direction_options(route: Route):
    route_direction_options = route["directions"]
    for direction_index, direction_name in enumerate(route_direction_options):
        print("{}) {}".format(direction_index + 1, direction_name))


def get_direction_choice_index(direction_options: List[str]) -> int:
    maximum_choice = len(direction_options)
    direction_choice = input("Enter a number between 1 and {}: ".format(maximum_choice))

    try:
        direction_choice_number = int(direction_choice)
    except ValueError:
        return get_direction_choice_index(direction_options)

    if direction_choice_number <= 0 or direction_choice_number > maximum_choice:
        return get_direction_choice_index(direction_options)

    return direction_choice_number - 1
