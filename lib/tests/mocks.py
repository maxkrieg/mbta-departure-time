mock_routes = [
    {
        "directions": ["West", "East"],
        "id": "Green-B",
        "name": "Green Line B",
        "type": "light",
    },
    {
        "directions": ["West", "East"],
        "id": "Green-C",
        "name": "Green Line C",
        "type": "light",
    },
]

mock_stops = [{"id": "foo", "name": "bar"}, {"id": "cats", "name": "dogs"}]


def mock_get_error(*args, **kwargs):
    raise Exception("Fake error")
