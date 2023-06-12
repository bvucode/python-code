import random, time
print("\x1b[2J", end = "")
char = " a b c d e f g h i j k l m n "
char2 = ".,/)(><^?_+-%':&][#$!abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0123456789"
while True:
    print('\x1b[H', end='')
    flag = 0
    tlist = []
    c = []
    for x, j in enumerate(range(21)):
        while flag == 0:
            c = [(random.choice(char), random.randint(1, 10)) for i in range(40)]
            flag = 1
        else:
            xlist = []
            for l in c:
                if l[0] == " ":
                    xlist.append(" ")
                else:
                    if l[1] < x:
                        c2 = " "
                    else:
                        c2 = random.choice(char2)
                    xlist.append(c2)
            print(" ".join(xlist))
            tlist.append(xlist)
    time.sleep(0.15)
    print('\x1b[H', end='')
    for y, j in enumerate(tlist):
        if y == len(tlist) - 3:
            break
        else:
            for x, k in enumerate(j):
                if k != " ":
                    if c[x][1] >= 5:
                        for l in range(len(tlist) - (y + 1)):
                            try:
                                if tlist[y + l][x] == " ":
                                    tlist[y + l][x] = random.choice(char2)
                                    break
                            except IndexError:
                                break
                    else:
                        for l in range(len(tlist) - (y + 1)):
                            try:
                                if tlist[y + l][x] == " ":
                                    tlist[y + l][x] = random.choice(char2)
                                    j[x] = " "
                                    break
                            except IndexError:
                                break
            for i in tlist:
                print(" ".join(i))
            time.sleep(0.16)
            print('\x1b[H', end='')
    
