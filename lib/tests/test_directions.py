from lib.directions import get_direction_choice_index

mock_direction_options = ["East", "West"]


def test_get_direction_choice_index(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "2",
    )
    result = get_direction_choice_index(mock_direction_options)
    assert mock_direction_options[result] == mock_direction_options[1]
