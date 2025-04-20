from enum import Enum


class ObjectTypes(Enum):
    """
    https://docs.codequest.club/game_logic/types/
    """
    TANK = 1
    BULLET = 2
    WALL = 3
    DESTRUCTIBLE_WALL = 4
    BOUNDARY = 5
    CLOSING_BOUNDARY = 6
    POWERUP = 7