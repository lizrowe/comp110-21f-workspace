"""List utility functions part 2."""

__author__ = "730403539"

# Define your functions below


def only_evens(number_list: list[int]) -> list[int]:
    """Return only even numbers from the list."""
    i: int = 0
    empty_list: list = []
    final_list: list[int] = []
    if len(number_list) == 0:
        return empty_list
    while i < len(number_list):
        if number_list[i] % 2 == 0:
            final_list.append(number_list[i])
        i += 1
    
    return final_list