import requests
import pytz
from datetime import datetime, timedelta
from typing import List

eastern = pytz.timezone("US/Eastern")


def fetch_departure_times(
    route_id: str, stop_id: str, direction_id: int
) -> List[datetime]:
    """
    Fetches departure times for a given, route, stop, and direction from the MBTA API.
    """

    try:
        url = "https://api-v3.mbta.com/predictions?filter%5Bdirection_id%5D={direction_id}&filter%5Bstop%5D={stop_id}&filter%5Broute%5D={route_id}".format(
            route_id=route_id, stop_id=stop_id, direction_id=direction_id
        )

        response = requests.get(url)
        predictions = response.json()["data"]
    except Exception:
        return None

    departure_times = []
    for prediction in predictions:
        iso_departure_time = prediction["attributes"]["departure_time"]
        if iso_departure_time is not None:
            departure_times.append(datetime.fromisoformat(iso_departure_time))

    departure_times_sorted = sorted(departure_times)

    return departure_times_sorted


def determine_next_departure_time(departure_times: List[datetime]) -> str:
    """
    Given a list of upcoming departure times, determines what the next departure time is.
    """

    now = eastern.localize(datetime.utcnow() - timedelta(hours=5))

    next_dep_time = None
    for dep_time in departure_times:
        if now < dep_time:
            next_dep_time = dep_time
            break

    if next_dep_time is None:
        return None

    return datetime.strftime(next_dep_time, "%I:%M %p")
