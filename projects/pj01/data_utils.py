"""Utility functions."""

__author__ = "730403539"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_data: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table."""
    returned_dict: dict[str, list[str]] = {}
    for key in column_data:
        counter: int = 0
        empty_list: list[str] = []
        while counter < number_of_rows:
            empty_list.append(column_data[key][counter])
            counter += 1
        returned_dict[key] = empty_list
    return returned_dict


def select(column_table: dict[str, list[str]], names_of_columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table."""
    empty_dict: dict[str, list[str]] = {}
    for column in names_of_columns:
        empty_dict[column] = column_table[column]
    return empty_dict


def concat(column_one: dict[str, list[str]], column_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table."""
    final_dict: dict[str, list[str]] = {}
    for column in column_one:
        final_dict[column] = column_one[column]
    for column in column_two:
        final_dict[column] = column_two[column]
    return final_dict


def count(values_list: list[str]) -> dict[str, int]:
    """Count the number of times a value appears in the input list."""
    result_dict: dict[str, int] = {}
    counter: int = 0
    for item in values_list:
        if item in result_dict:
            result_dict[item] = counter
            counter += 1
        else:
            result_dict[item] = counter = 1
    
    return result_dict