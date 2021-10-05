"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730403539"


def test_only_evens_empty() -> None:
    """Tests only_evens function when empty."""
    number_list: list[int] = []
    assert only_evens(number_list) == []


def test_only_evens_single_item() -> None:
    """Tests only_evens function when there is a single item."""
    number_list: list[int] = [2]
    assert only_evens(number_list) == [2]


def test_only_evens_many_items() -> None:
    """Tests only_evens function when there are many items."""
    number_list: list[int] = [1, 2, 3, 4]
    assert only_evens(number_list) == [2, 4]


def test_sub_empty() -> None:
    """Tests sub function when empty."""
    list_1: list[int] = []
    start: int = 0 
    end: int = 0
    assert sub(list_1, start, end) == []


def test_sub_single_item() -> None:
    """Tests sub function when there is a single item."""
    list_1: list[int] = [1]
    start: int = 1
    end: int = 1
    assert sub(list_1, start, end) == []


def test_sub_many_items() -> None:
    """Tests sub function when there are many items."""
    list_1: list[int] = [1, 2, 3, 4, 5]
    start: int = 1
    end: int = 4
    assert sub(list_1, start, end) == [2, 3, 4]


def test_concat_empty() -> None:
    """Tests concat function when empty."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_single_item() -> None:
    """Tests concat function when there is a single item."""
    list_1: list[int] = [1]
    list_2: list[int] = [2]
    assert concat(list_1, list_2) == [1, 2]


def test_concat_many_items() -> None:
    """Tests concat function when there are many items."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6]