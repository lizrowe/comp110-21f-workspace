"""Practice with dictionaries."""

__author__ = "730403539"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    inverse: dict[str, str] = {}

    for key in inverse:
        if [a[key]] in inverse:
            raise KeyError("Duplicate key detected.")
        inverse[a[key]] = key
    
    return(inverse)


def favorite_color(a: dict[str, str]) -> str:
    """Returns the color that appears most frequently, or the first color in the dictionary if there is a tie."""
    favorite_color_dict: dict[str, str] = {}

    for key, value in favorite_color_dict:
        if value in favorite_color_dict:
            favorite_color_dict[value] = favorite_color_dict[value] + 1
        else:
            favorite_color_dict[value] = 1
    
    return value


def count(a: list[str]) -> dict[str, int]:
    """Produces a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    count_list: list[str] = []
    count_dict: dict[str, int] = {}
    
        


    
