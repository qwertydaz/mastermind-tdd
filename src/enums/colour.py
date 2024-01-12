from enum import Enum


def num_of_colours():
    return len(Colour)


class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    BLACK = 5
