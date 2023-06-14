import random, time
print("\x1b[2J", end = "")
char = ".,/)(><^?_+-%':&][#$!abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0123456789"
W = 104
H = 51
while True:
    print('\x1b[H', end='')
    flag = 0
    tlist = []
    for x, j in enumerate(range(H)):
        while flag == 0:
            c = [(random.choice("01"), random.randint(1, H)) for i in range(W)]
            flag = 1
        else:
            xlist = []
            for l in c:
                if l[0] == "0":
                    xlist.append(" ")
                else:
                    if l[1] < x:
                        c2 = " "
                    else:
                        c2 = random.choice(char)
                    xlist.append(c2)
            tlist.append(xlist)
    for y, j in enumerate(tlist):
        if y == len(tlist) - 5:
            break
        else:
            for x, k in enumerate(j):
                if k != " ":
                    if c[x][1] > 25:
                        for l in range(len(tlist) - (y + 1)):
                            try:
                                if tlist[y + l][x] == " ":
                                    tlist[y + l][x] = random.choice(char)
                                    break
                            except IndexError:
                                pass
                    else:
                        try:
                            if c[x + 1][1] > c[x][1]:
                                for l in range(len(tlist) - (y + 1)):
                                    try:
                                        if c[x - 1][0] == "0" and y > 5:
                                            if tlist[y + l][x - 1] == " ":
                                                tlist[l + l][x - 1] = random.choice(char)
                                        if tlist[y + l][x] == " ":
                                            tlist[y + l][x] = random.choice(char)
                                            j[x] = " "
                                            break
                                    except IndexError:
                                        pass
                            else:
                                for l in range(len(tlist) - (y + 1)):
                                    try:
                                        tlist[y + l][x] = random.choice(char)
                                        if tlist[y + l][x] == " ":
                                            tlist[y + l][x] = random.choice(char)
                                            break
                                    except IndexError:
                                        pass
                        except IndexError:
                            pass
            for i in tlist:
                print(" ".join(i))
            time.sleep(0.05)
            print('\x1b[H', end='')
    
