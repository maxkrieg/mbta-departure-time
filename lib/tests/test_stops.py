import requests
from lib.stops import fetch_stops, get_stop_choice
from .mocks import mock_stops, mock_get_error


def test_fetch_stops_success():
    results = fetch_stops(route_id="Red", direction_index=0)

    assert len(results) == 22

    no_errors = True
    for result in results:
        try:
            assert result["id"] is not None
            assert result["name"] is not None
        except Exception:
            no_errors = False
            break

    assert no_errors


def test_fetch_stops_error(monkeypatch):
    monkeypatch.setattr(requests, "get", mock_get_error)
    result = fetch_stops(route_id="Red", direction_index=0)
    assert result is None


def test_get_stop_choice(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1",
    )
    result = get_stop_choice(mock_stops)
    assert result == mock_stops[0]
