from lib.directions import print_route_direction_options, get_direction_choice_index
from lib.routes import fetch_routes, get_route_choice, print_route_list
from lib.stops import fetch_stops, print_stops_list, get_stop_choice
from lib.departures import fetch_departure_times, determine_next_departure_time
from lib.utils import exit_if_no_data

print(" ")
print("Hello and welcome to the MBTA Departure Time Application")
print(" ")
print("To start, please select a route number from the list below: ")
print(" ")

# ROUTE
routes = fetch_routes()
exit_if_no_data(routes, "routes")

print_route_list(routes)

print(" ")
route = get_route_choice(routes)
print(" ")

route_id = route["id"]
route_name = route["name"]

# DIRECTION
print(" ")
print(
    "Please select a {route_name} direction from the options below:".format(
        route_name=route_name
    )
)
print(" ")
print_route_direction_options(route)
print(" ")
direction_index = get_direction_choice_index(route["directions"])
print(" ")

direction_name = route["directions"][direction_index]

# STOPS
stops = fetch_stops(route["id"], direction_index)
exit_if_no_data(stops, "stops")

print(" ")
print(
    "Please select a stop for {route_name} trains heading {direction_name} from the list below:".format(
        route_name=route_name, direction_name=direction_name
    )
)
print(" ")

print_stops_list(stops)

print(" ")
stop = get_stop_choice(stops)
print(" ")

stop_id = stop["id"]

# DEPARTURE TIME PREDICTION
print("Getting the next departure...")

departure_times = fetch_departure_times(
    route_id=route_id,
    stop_id=stop_id,
    direction_id=direction_index,
)
exit_if_no_data(departure_times, "departure times")

next_departure_time = determine_next_departure_time(departure_times)
print(" ")

if next_departure_time is None:
    print("Sorry, we were unable to get a depature time")
else:
    print(
        "The next {route_name} train heading {direction} from {stop} stop departs at {departure_time} ET".format(
            route_name=route["name"],
            direction=route["directions"][direction_index],
            stop=stop["name"],
            departure_time=next_departure_time,
        )
    )
