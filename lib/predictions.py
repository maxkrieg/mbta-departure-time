from datetime import datetime, timedelta
import pytz

import requests


eastern = pytz.timezone("US/Eastern")


def fetch_predictions(route_id, stop_id, direction_id):
    try:
        url = "https://api-v3.mbta.com/predictions?filter%5Bdirection_id%5D={direction_id}&filter%5Bstop%5D={stop_id}&filter%5Broute%5D={route_id}".format(
            route_id=route_id, stop_id=stop_id, direction_id=direction_id
        )

        response = requests.get(url)
        predictions = response.json()["data"]
    except Exception:
        return None

    return predictions


def determine_next_departure_time(predictions):
    departure_times = sorted(
        [
            datetime.fromisoformat(prediction["attributes"]["departure_time"])
            for prediction in predictions
        ]
    )

    now = eastern.localize(datetime.utcnow() - timedelta(hours=5))

    next_dep_time = None
    for dep_time in departure_times:
        if now < dep_time:
            next_dep_time = dep_time
            break

    if next_dep_time is None:
        return None

    return datetime.strftime(next_dep_time, "%I:%M %p")
