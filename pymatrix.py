import random, time
print("\x1b[2J", end = "")
char = ".,/)(><^?_+-%':&][#$!abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0123456789"
while True:
    print('\x1b[H', end='')
    flag = 0
    tlist = []
    c = []
    for x, j in enumerate(range(51)):
        while flag == 0:
            c = [(random.choice(" ."), random.randint(1, 20)) for i in range(104)]
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
                        c2 = random.choice(char)
                    xlist.append(c2)
            print(" ".join(xlist))
            tlist.append(xlist)
    time.sleep(0.035)
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
                                    tlist[y + l][x] = random.choice(char)
                                    break
                            except IndexError:
                                break
                    else:
                        for l in range(len(tlist) - (y + 1)):
                            try:
                                if tlist[y + l][x] == " ":
                                    tlist[y + l][x] = random.choice(char)
                                    j[x] = " "
                                    break
                            except IndexError:
                                break
            for i in tlist:
                print(" ".join(i))
            time.sleep(0.035)
            print('\x1b[H', end='')
    
