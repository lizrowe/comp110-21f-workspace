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


def sub(list_1: list[int], start: int, end: int) -> list[int]:
    """Return a subset of the given list."""
    i: int = start
    empty_list: list = []
    final_list: list = []
    if len(list_1) == 0:
        return empty_list
    if len(list_1) == i:
        return empty_list
    while i < end:
        final_list.append(list_1[i])
        i += 1
    
    return final_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Return a new list which contains all the elements of the first list and second list."""
    final_list: list[int] = []
    final_list = list_1 + list_2
    return final_list