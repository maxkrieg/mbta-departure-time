import requests
from lib.routes import fetch_routes, get_route_choice
from .mocks import mock_get_error, mock_routes


def test_fetch_routes_success():
    results = fetch_routes()

    assert len(results) == 8

    no_errors = True
    for result in results:
        try:
            assert result["id"] is not None
            assert len(result["directions"]) == 2
            assert result["name"] is not None
            assert result["type"] is not None
        except Exception:
            no_errors = False
            break

    assert no_errors


def test_fetch_routes_error(monkeypatch):
    monkeypatch.setattr(requests, "get", mock_get_error)
    result = fetch_routes()
    assert result is None


def test_get_route_choice(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1",
    )
    result = get_route_choice(mock_routes)
    assert result == mock_routes[0]
