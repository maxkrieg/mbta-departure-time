from lib.departures import fetch_departure_times


def test_fetch_departure_times_success():
    results = fetch_departure_times(
        route_id="Red", stop_id="place-brntn", direction_id=1
    )
    assert len(results) > 0


def test_fetch_departure_times_error():
    pass
