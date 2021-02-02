import sys


def exit_if_no_data(data, name):
    if data is None or len(data) < 1:
        print("Oops, we were unable to gather {name} data, exiting")
        sys.exit()
