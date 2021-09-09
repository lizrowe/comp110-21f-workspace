"""Repeating a beat in a loop."""

__author__ = "730403539"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")

number: str = input("How many times do you want to repeat it? ")

counter: int = 0
counter2: int = 0
maximum: int = int(number)
flag: bool = True
all_beats: str = ""


while (flag):
    if (maximum <= 0):
        print("No beat...")
        flag = False
    else:
        while (counter < maximum):
            if (counter == 0):
                all_beats = beat
            else:
                all_beats = all_beats + " " + beat
            counter = counter + 1
        print(all_beats)
        flag = False
