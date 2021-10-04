"""List utility functions part 2."""

__author__ = "730403539"

# Define your functions below


def only_evens(number_list: list[int]) -> list[int]:
    """Return only even numbers from the list."""
    i: int = 0
    o: list = []
    if len(number_list) == 0:
        return o
    while i < len(number_list):
        if i % 2 == 0:
            return i
        i += 1
