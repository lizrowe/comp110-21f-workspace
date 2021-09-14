"""Drawing forests in a loop."""

__author__ = "730403539"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: str = input("Depth: ")

counter: int = 0

maximum: int = int(depth)

if maximum > 0:
    print(TREE)