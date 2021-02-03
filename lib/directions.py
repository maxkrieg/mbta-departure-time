from typing import List
from lib.types import Route
from lib.utils import validate_number_choice


def print_route_direction_options(route: Route):
    """
    Prints out a list of direction options.
    """

    route_direction_options = route["directions"]
    for direction_index, direction_name in enumerate(route_direction_options):
        print("{}) {}".format(direction_index + 1, direction_name))


def get_direction_choice_index(direction_options: List[str]) -> int:
    """
    Prompts the user to choose a direction option.
    """

    maximum_choice = len(direction_options)
    direction_choice = input("Enter a number between 1 and {}: ".format(maximum_choice))

    direction_choice_number = validate_number_choice(maximum_choice, direction_choice)
    if direction_choice_number is None:
        return get_direction_choice_index(direction_options)

    return direction_choice_number - 1
