import sys


def exit_if_no_data(data, name):
    if data is None or len(data) < 1:
        print(
            "Sorry, we were unable to gather {name} data from the MBTA API, exiting".format(
                name=name
            )
        )
        sys.exit()


def validate_number_choice(maximum_choice: int, user_input: str):
    choice = None
    try:
        choice = int(user_input)
    except ValueError:
        return None

    if choice <= 0 or choice > maximum_choice:
        return None

    return choice
