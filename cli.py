from lib.get_routes import get_routes


def get_route_choice():
    route_choice = input("Please select a route: ")
    routes = ["Red", "Blue", "Green"]
    if route_choice not in routes:
        print("Please choose a valid route")
        return get_route_choice()
    else:
        return route_choice


print("getting routes")
get_routes()
route_choice = get_route_choice()

print(route_choice)