import requests
from lib.departures import fetch_departure_times
from .mocks import mock_get_error


def test_fetch_departure_times_success():
    results = fetch_departure_times(
        route_id="Red", stop_id="place-brntn", direction_id=1
    )
    assert len(results) > 0


def test_fetch_departure_times_error(monkeypatch):
    monkeypatch.setattr(requests, "get", mock_get_error)
    result = fetch_departure_times(
        route_id="Red", stop_id="place-brntn", direction_id=1
    )
    assert result is None
