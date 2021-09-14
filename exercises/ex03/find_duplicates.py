"""Finding duplicate letters in a word."""

__author__ = "730403539"

word: str = (input("Enter a word: "))

duplicate: bool = False

counter: int = 0

while counter < len(word):
    j: int = counter + 1
    hold: str = word[counter]
    while j < len(word):
        if word[j] == hold:
            duplicate: bool = True
        j += 1
    
    counter += 1

duplicate_str: str = str(duplicate)

print("Found duplicate: " + duplicate_str)

    