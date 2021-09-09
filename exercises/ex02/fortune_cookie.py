"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730403539"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

rand_int: int = randint(1, 4)

if rand_int == 1:
    print("You're gonna kill this assessment.")
else:
    if rand_int == 2:
        print("You're gonna get a 4.0 this semester.")
    else:
        if rand_int == 3:
            print("Love is coming your way.")
        else:
            print("You're gonna be a millionaire.")

print("Now, go spread positive vibes!")