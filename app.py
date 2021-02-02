from lib.routes import (
    fetch_routes,
    get_route_choice,
    print_route_list,
    print_route_direction_options,
    get_direction_choice_index,
)
from lib.stops import fetch_stops, print_stops_list, get_stop_choice

from pprint import pprint

routes = fetch_routes()

print(" ")
print("Hello and welcome to the MBTA Departure Time Application")
print(" ")
print("To start, please select a route number from the list below: ")
print(" ")

print_route_list(routes)

print(" ")

selected_route = get_route_choice(routes)

print(" ")
pprint(selected_route)
print(" ")

print_route_direction_options(selected_route)
selected_direction_index = get_direction_choice_index(selected_route["directions"])

stops = fetch_stops(selected_route["id"], selected_direction_index)
print_stops_list(stops)
selected_stop = get_stop_choice(stops)

print(" ")
pprint(selected_stop)
print(" ")
