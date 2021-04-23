import random
from random import randint as ran


def game():
    usr_pt = 0
    com_pt = 0
    while True:
        usr_choice = int(input("Choose the type of dice you wanna throw."))
        usr_throws = dice(usr_choice)
        if usr_throws == 7:
            usr_pt = (usr_pt // 7) - 7
        if usr_throws == 11:
            usr_pt = (usr_pt * 11) - 11
        usr_pt += usr_throws
        usr_choice = int(input("Choose the type of dice you wanna throw."))
        usr_throws = [usr_throws]
        sec_throw = dice(usr_choice)
        if sec_throw == 7:
            usr_pt = (usr_pt // 7) - 7
        if sec_throw == 11:
            usr_pt = (usr_pt * 11) - 11
        usr_throws.append(sec_throw)
        usr_pt += sec_throw
        print(f"Your throws was; {usr_throws}.\nYour score is {usr_pt}.")
        if usr_pt >= 2001:
            print("You win!")
            return "User is the winner."
        com_throws = dice(random.choice([3, 4, 6, 8, 10, 12, 20, 100]))
        if com_throws == 7:
            com_pt = (com_pt // 7) - 7
        if com_throws == 11:
            com_pt = (com_pt * 11) - 11
        com_pt += com_throws
        com_throws = [com_throws]
        sec_com_throws = dice(random.choice([3, 4, 6, 8, 10, 12, 20, 100]))
        if sec_com_throws == 7:
            com_pt = (com_pt // 7) - 7
        if sec_com_throws == 11:
            com_pt = (com_pt * 11) - 11
        com_throws.append(sec_com_throws)
        com_pt += sec_com_throws
        print(f"Computer's throws was; {com_throws}.\nComputer's score is {com_pt}.\n")
        if com_pt >= 2001:
            print("Computer win!")
            return "Computer is the winner."


def dice(code=6):
    dices = [3, 4, 6, 8, 10, 12, 20, 100]
    if not code in dices:
        print("There is no such dice!")
        return None
    throw = ran(1, code)
    return throw


game()

"""
napisz zeby dice pobieralo kod typu liczba.liczba, rozdziel ten kod i zwroc liste
2 rzutow. w game stworz zmienna do zsumowanie tych rzutow z listy.
sprawdz czy jest 7 albo 11 itd.
dodaj sume tych liczb do punktacji.
zwroc napis z rzutami i punktacja usr.
zrob to samo dla com.
pomysl jak zabezpieczyc sie przed wpisaniem '' albo czegos innego w input, zrob to raczej za 
pomoca try a nie if.
"""