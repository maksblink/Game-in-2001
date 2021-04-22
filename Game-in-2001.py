import random
from random import randint as ran


def game():
    usr_pt = 0
    com_pt = 0
    while True:
        usr_choice = input("Choose the type of dice you wanna throw.")
        if usr_choice == "":
            usr_choice = "2D6"
        usr_throws = dice(usr_choice)
        usr_pt += sum(usr_throws)
        print(f"Your throws was; {usr_throws}.\nYour score is {usr_pt}.")
        if usr_pt >= 2001:
            print("You win!")
            return "User is the winner."
        com_throws = dice("2D" + random.choice(["3", "4", "6", "8", "10", "12", "20", "100"]))
        com_pt += sum(com_throws)
        print(f"Computer's throws was; {com_throws}.\nComputer's score is {com_pt}.\n")
        if com_pt >= 2001:
            print("Computer win!")
            return "Computer is the winner."


def dice(code: str):
    print(code)
    dices = [3, 4, 6, 8, 10, 12, 20, 100]
    try:
        x = int(code[: code.index("D")])
        y = int(code[code.index("D") + 1:])
    except ValueError as ve:
        print(ve)
        return None
    if not y in dices:
        print("There is no such dice!")
        return None
    throws = []
    for i in range(x):
        throws.append(ran(1, y))
    return throws


game()
