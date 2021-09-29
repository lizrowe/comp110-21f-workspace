"""List utility functions."""

__author__ = "730403539"


# TODO: Implement your functions here.


def all(number_list: list[int], number: int) -> bool:
    """Return True if the number is in the number list, False otherwise."""
    i: int = 0
    while i < len(number_list):
        if number_list[i] != number:
            return False
        i += 1
    return True


def is_equal(number_list_one: list[int], number_list_two: list[int]) -> bool:
    """Return True if lists are equal, False otherwise."""
    i: int = 0
    while i < len(number_list_one):
        if number_list_one[i] != number_list_two[i]:
            return False
        i += 1
    return True  


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")