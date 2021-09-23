"""The first project for COMP 110."""

__author__ = "730403539"

player: str
points: int
BRRR_FACE: str
WIND_FACE: str
YAY_EMOJI: str
SAD_EMOJI: str


def main():
    global points
    points = 0
    global player
    global BRRR_FACE
    BRRR_FACE = '\U0001F976'
    global WIND_FACE
    WIND_FACE = '\U0001F62E'
    global YAY_EMOJI
    YAY_EMOJI = '\U0001F389'
    global SAD_EMOJI
    SAD_EMOJI = '\U0001F62D'
    greet()
    experience()
    while points == 1:
        experience_2()
    while points == 3:
        final(3, 0)


def greet() -> None:
    global player
    player = str(input("What's your name?"))
    print(f"Hello, {player}, the Fire Nation is attacking! Choose your team and help save the world from Fire Nation domination!")
    

def experience() -> None:
    global player
    global points
    global BRRR_FACE
    global WIND_FACE
    choice: str = str(input("Do you want to quit, join the Water Team, or join the Air Team?"))
    if choice == "Join the Water Team":
        points = points + 1
        print(f"{player}, you've successfully joined the Water Team {BRRR_FACE}! You have {points} adventure point.")
    if choice == "Join the Air Team":
        points = points + 1
        print(f"{player}, you've sucessfully joined the Air Team {WIND_FACE}! You have {points} adventure point.")
    if choice == "Quit":
        print(f"{player}, you've successfully exited the game. Goodbye!")
        points = points
        print(f"You earned {points} adventure points.")


def experience_2() -> None:
    global player
    global points
    global YAY_EMOJI
    global SAD_EMOJI
    new_choice: str = str(input("Do you want to attack or surrender?"))
    if new_choice == "Surrender":
        points = 0
        print(f"{player}, you surrendered and lost the game{SAD_EMOJI}! You lost your adventure point and left the game with {points} adventure points.")
    if new_choice == "Attack":
        points = points + 2
        print(f"{player}, you attacked and won {YAY_EMOJI}! You have {points} adventure points.")


def final(a: int, b: int) -> int:
    global player
    global points
    global YAY_EMOJI
    global SAD_EMOJI
    from random import randint
    a = 3
    b = 0
    print("The final outcome of the war depends on you rolling a 6. Good luck!")
    print(randint(1, 6))
    if randint == 6:
        points = points + 3
        print(f"{player}, you won the war {YAY_EMOJI}! You earned {points} adventure points.")
        return (points + a)
    else:
        points = points + 2
        print(f"You didn't roll a 6, you lost the war {SAD_EMOJI}! You earned {points} adventure points.")
        return (points + b)
    

if __name__ == "__main__":
    main()