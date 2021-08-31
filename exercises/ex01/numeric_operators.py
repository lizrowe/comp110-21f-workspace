"""Part 2 of exercise 1."""
__author__: str = "730403539"
left_hand_number: str = input("Left-hand side: ")
right_hand_number: str = input("Right-hand side: ")
left_hand_number_int: int = int(left_hand_number)
right_hand_number_int: int = int(right_hand_number)
print(left_hand_number_int, " ** ", right_hand_number_int, " is ", (left_hand_number_int ** right_hand_number_int))
print(left_hand_number_int, " / ", right_hand_number_int, " is ", (left_hand_number_int / right_hand_number_int))
print(left_hand_number_int, " // ", right_hand_number_int, " is ", (left_hand_number_int // right_hand_number_int))
print(left_hand_number_int, " % ", right_hand_number_int, " is ", (left_hand_number_int % right_hand_number_int))