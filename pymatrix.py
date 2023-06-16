import random, time
print("\x1b[2J", end = "")
tlist = []
flag = 0
char = ".,/)(><^?_+-%':&][#$!abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0123456789"
W = 104
H = 50
while True:
    print("\x1b[H", end="")
    c = [(random.choice("01"), random.randint(1, 30)) for i in range(W)]
    if flag == 0:
        for x, i in enumerate(range(H)):
            xlist = []
            for j in c:
                if j[0] == "0":
                    xlist.append(" ")
                else:
                    if j[1] < x:
                        c3 = " "
                    else:
                        c3 = random.choice(char)
                    xlist.append(c3)
            tlist.append(xlist)
            flag = 1
    c2 = [(random.choice("01"), random.randint(1, 30)) for i in range(W)]
    for y, j in enumerate(tlist):
        for x, k in enumerate(j):
            if k != " ":
                if c[x][1] >= 20:
                    for l in range(len(tlist)):
                        try:
                            if tlist[y + (l + 1)][x] == " ":
                                tlist[y + (l + 1)][x] = random.choice(char)
                                break
                        except IndexError:
                            j[x] = " "
                elif c[x][1] >= 4 and c[x][1] <= 8:
                    for l in range(len(tlist)):
                        try:
                            tlist[y + (l + 1)][x] = random.choice(char)
                            if tlist[y + (l + 1)][x] == " ":
                                tlist[y + (l + 1)][x] = random.choice(char)
                                break
                        except IndexError:
                            j[x] = " "
                else:
                    for l in range(len(tlist)):
                        try:
                            if tlist[y + (l + 1)][x] == " ":
                                tlist[y + (l + 1)][x] = random.choice(char)
                                j[x] = " "
                                break
                        except IndexError:
                            j[x] = " "
            else:
                if y + 1 >= c2[x][1] and c2[x][0] == "1":
                    tlist[y][x]  = random.choice(char)   
        for i in tlist:
            print(" ".join(i))
        time.sleep(0.45)
        print("\x1b[H", end="")
