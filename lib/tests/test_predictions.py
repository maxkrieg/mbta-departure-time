from lib.predictions import fetch_predictions


def test_fetch_predictions():
    result = fetch_predictions(route_id="Red", stop_id="place-brntn", direction_id=1)
    print(result)
