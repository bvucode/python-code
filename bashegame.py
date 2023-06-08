import random

def main():
    # The game can have 7, 11, 15, 19, 21, ... things.
    THINGS = 11
    things = THINGS
    firststep = 0
    winalg = 0
    print("""Game Bashe. There are 11 items. Rivals go in turn, \nfor each move any of the players can take 1, 2 or 3 items. \nLoses the one who is forced to take the last item.
             \nИгра Баше. 11 предметов. Соперники ходят по очереди, за каждый ход любой  из играющих может взять 1, 2 или 3 предмета. \nПроигрывает тот, кто вынужден взять последний предмет.\n""")
    while True:
        user = int(input('Enter: number 1, 2 or 3: '))
        if user > 3 :
            print("from 1 to 3 only")
        else:
            things -= user
            if firststep == 0 and user != 2:
                apptake = user
                winalg = 1
                firststep = 1
            else:
                if winalg == 1:
                    apptake = 4 - user
                elif winalg == 1 and things == 2:
                    apptake = 1
                else:
                    if things == 1:
                        apptake = 1
                    else:
                        apptake = random.randint(1, 3)
            things -= apptake
        print("The app took {}. Total left {}".format(apptake, things))
        if things == 0:
            print("You win!")
        elif things == 1:
            print("You lost! Total left {}".format(things))
        if things == 0 or things == 1:
            print("Do you want play again? (y or n)")
            if input("> ").lower().startswith("n"):
                break
            else:
                print("Thanks for playing!")
                things = THINGS
if __name__ == "__main__":
    main()
