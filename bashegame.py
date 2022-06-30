import random

THINGS = 11 # 11 things. The game can have 7, 11, 15, 19, 21, ... things.

def main():
    things = THINGS #make same number THINGS
    firststep = 0
    print("""Game Bashe. There are 11 items. Rivals go in turn, for each move
any of the players can take 1, 2 or 3 items.
Loses the one who is forced to take the last item.
Игра Баше. 11 предметов. Соперники ходят по очереди, за каждый ход
любой  из играющих может взять 1, 2 или 3 предмета.
Проигрывает тот, кто вынужден взять последний предмет.""")
    while True:
        user = int(input('Enter: number 1, 2 or 3: '))
        if user > 3:
            print("try again")
        else:
            things -= user
            if firststep == 0:
                if user == 2:
                    apptake = random.randint(1, 3)
                    firststep = 1
                elif user == 1:
                    if THINGS == 7 or THINGS == 11:
                        apptake = 1
                    else:
                        apptake = 4 - user
                elif user != 2:
                    apptake = 4 - user
                    firststep = 1
            elif things == 7:
                apptake = 2
            elif things <= 3:
                apptake = things
            elif things != 7 and user == 4 - apptake:
                apptake = random.randint(1, 3)
            elif things != 7 and user != 4 - apptake:
                apptake = 4 - user
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
if __name__ == "__main__":
    main()
