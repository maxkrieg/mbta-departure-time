# import mock
# import pytest
from .routes import fetch_routes, get_route_choice

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


def test_get_route_choice(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "foo",
    )
    result = get_route_choice(mock_routes)
    second_result = get_route_choice(mock_routes)
    print(result)
    print(second_result)


def test_get_routes():
    result = fetch_routes()
    assert len(result) > 0
