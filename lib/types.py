from typing import TypedDict, List


class Route(TypedDict):
    id: str
    name: str
    directions: List[int]
    type: str


class Stop(TypedDict):
    id: str
    name: str
