# Bashe Game

import random

print('Game Bashe. There are 11 items. Rivals go in turn, for each move \nany of the players can take 1, 2 or 3 items. \nLoses the one who is forced to take the last item.')
print('Игра Баше. 11 предметов. Соперники ходят по очереди, за каждый ход \nлюбой  из играющих может взять 1, 2 или 3 предмета. \nПроигрывает тот, кто вынужден \nвзять последний предмет.')

things = 11 # 11 things. The game can have 7, 11, 15, 19, 21, ... things.
first = 0

def main():
    global things
    user = int(input('Enter: number 1, 2 or 3: '))
    things -= user
    logic(user, things)
def printr(apptake, targ):
    global things
    global first
    if targ == 0:
        print("You win!")
        things = 11
        first = 0
    elif targ == 1:
        print("You lost! Total left {}".format(targ))
        things = 11
        first = 0
    else:
        print("The app took {}. Total left {}".format(apptake, targ))
        things = targ
def logic(usertake, targ):
    global first
    if targ > 1:
        if first == 0:
            if usertake == 1:
                first = 1
                apptake = 1
                targ -= apptake
                printr(apptake, targ)
            elif usertake == 2:
                first = 1
                apptake = random.randint(1, 3)
                targ -= apptake
                printr(apptake, targ)
            elif usertake == 3:
                first = 1
                apptake = 3
                targ -= apptake
                printr(apptake, targ)
        else:
           apptake = winalgorithm(usertake)
           targ -= apptake
           printr(apptake, targ)
    elif targ == 1:
        apptake = 1
        targ -= apptake
        printr(apptake, targ)
def winalgorithm(usertake):
    var = 4 - usertake
    return var
while True:
    main()
