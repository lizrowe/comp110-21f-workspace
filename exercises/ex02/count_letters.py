"""Counting letters in a string."""

__author__ = "730403539"


# Begin your solution here...

from typing import Counter

word: str = input("What letter do you want to search for? ")

search: str = input("Enter a word: ")

Counter: int = 0

word_int: int = int(word)

while Counter < word_int:
    if Counter <= 0:
        print("Count: " + str(0))
    else Counter > 0:
        print("Count: " + str(word_int))
