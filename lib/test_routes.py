from lib.get_routes import get_routes


def test_get_routes():
    result = get_routes()
    assert len(result) > 0
