"""An exercise in remainders and boolean logic."""

__author__ = "730403539"


# Begin your solution here...

guess: int = int(input("Enter an int: "))

if guess % 2 == 0 and guess % 7 == 0:
    print("TAR HEELS")
else:
    if guess % 7 == 0:
        print("HEELS")
    if guess % 2 == 0:
        print("TAR")
    if guess % 2 != 0 and guess % 7 != 0:
        print("CAROLINA")