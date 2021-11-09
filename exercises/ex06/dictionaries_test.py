"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730403539"


def test_invert_empty() -> None:
    """Tests invert with an empty dictionary."""
    inverse: dict[str, str] = {}
    assert invert(inverse) == {}


def test_invert_single_item() -> None:
    """Tests invert with a single item in a dictionary."""
    inverse: dict[str, str] = {'bat': 'cat'}
    assert invert(inverse) == {'cat': 'bat'}


def test_invert_multiple_items() -> None:
    """Tests invert with multiple items in a dictionary."""
    inverse: dict[str, str] = {'bat': 'cat', 'bird': 'worm', 'goose': 'slug'}
    assert invert(inverse) == {'cat': 'bat', 'worm': 'bird', 'slug': 'goose'}


def test_favorite_color_empty() -> None:
    """Tests favorite_color with an empty dictionary."""
    favorite_color_dict: dict[str, str] = {}
    assert favorite_color(favorite_color_dict) == {}


def test_favorite_color_single_item() -> None:
    """Tests favorite_color with a single item in a dictionary."""
    favorite_color_dict: dict[str, str] = {'Lizzie': 'orange'}
    assert favorite_color(favorite_color_dict) == 'orange'


def test_favorite_color_multiple_items() -> None:
    """Tests favorite_color with multiple items in a dictionary."""
    favorite_color_dict: dict[str, str] = {'Lizzie': 'orange', 'Will': 'blue', 'Katherine': 'purple', 'Jeri': 'blue'}
    assert favorite_color(favorite_color_dict) == 'blue'


def test_count_empty() -> None:
    """Tests count with an empty list."""
    count_list: list[str] = []
    assert count(count_list) == []


def test_count_single_item() -> None:
    """Tests count with a single item."""
    count_list: list[str] = ['yo']
    assert count(count_list) == ['yo', 2]


def test_count_multiple_items() -> None:
    """Tests count with multiple items."""
    count_list: list[str] = ['yo', 'yo', 'ma']
    assert count(count_list) == ['yo': 2, 'yo': 2, 'ma':2]