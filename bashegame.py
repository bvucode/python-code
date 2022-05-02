import random

print('Game Bashe. There are 11 items. Rivals go in turn, for each move \nany of the players can take 1, 2 or 3 items. \nLoses the one who is forced to take the last item.')
print('Игра Баше. 11 предметов. Соперники ходят по очереди, за каждый ход \nлюбой  из играющих может взять 1, 2 или 3 предмета. \nПроигрывает тот, кто вынужден \nвзять последний предмет.')

things = 11 # 11 things. The game can have 7, 11, 15, 19, 21, ... things.
first = 0

def main():
    global things
    user = int(input('Enter: number 1, 2 or 3: '))
    things -= user
    vl = logic(user)
    if things == 1:
        things -= vl
        printr(vl, things)
    elif things == 0:
        printr(vl, things)
    else:
        things -= vl
        printr(vl, things)

def printr(apptake, targ):
    global things
    if targ == 0:
        print("You win!")
        things = 11
    else:
        print("The app took {}. Total left {}".format(apptake, targ))
        if targ == 1:
            print("You lost! Total left {}".format(targ))
            things = 11 

def logic(xarg):
    global things
    global first
    if things > 1:
        if first == 0:
            if xarg == 2:
                xarg = random.randint(1, 3)
            else:
                xarg = 4 - xarg
            first = 1
        if things == 7:
            xarg = 2
        elif things == 4:
            xarg = 3
        elif things % 2 == 0:
            xarg = 1
        else:
            xarg = 4 - xarg
    else:
        xarg = 1
    return xarg

while True:
    main()
