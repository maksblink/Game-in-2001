import random
from random import randint as ran


def game():
    print("In this game you can roll the following types of dice: (3, 4, 6, 8, 10, 12, 20, 100)-sided.")
    usr_pt = 0
    com_pt = 0
    while True:
        usr_throws = 0
        while usr_throws == 0:
            usr_throws = dice(input("Choose the types of dices you wanna throw, between the dices type \",\"."))
        if usr_throws == 7:
            usr_pt = (usr_pt // 7) - 7
        if usr_throws == 11:
            usr_pt = (usr_pt * 11) - 11
        usr_pt += usr_throws

        print(f"Your throws was equal to; {usr_throws}.\nYour score is {usr_pt}.")
        if usr_pt >= 2001:
            print("You win!")
            return "User is the winner."
        com_throws = dice(
            str(random.choice([3, 4, 6, 8, 10, 12, 20, 100])) + "," + str(random.choice([3, 4, 6, 8, 10, 12, 20, 100])))
        if com_throws == 7:
            com_pt = (com_pt // 7) - 7
        if com_throws == 11:
            com_pt = (com_pt * 11) - 11
        com_pt += com_throws

        print(f"Computer's throws was equal to; {com_throws}.\nComputer's score is {com_pt}.\n")
        if com_pt >= 2001:
            print("Computer win!")
            return "Computer is the winner."


def dice(code: str):
    dices = [3, 4, 6, 8, 10, 12, 20, 100]
    try:
        x = int(code[: code.index(",")])
        y = int(code[code.index(",") + 1:])
    except ValueError as ve:
        print(ve)
        print("incorrect input")
        return 0
    if x and y not in dices:
        print("There is no such dice!")
        return None
    result = 0
    result += ran(1, x)
    result += ran(1, y)
    return result


game()
