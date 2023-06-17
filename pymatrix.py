import random, time
print("\x1b[2J", end = "")
tlist = []
flag = 0
char = ".,/)(><^?_+-%':&][#$!abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0123456789"
W = 104
H = 50
while True:
    print("\x1b[H", end="")
    if flag == 0:
        c = [(random.randint(0, 1), random.randint(1, H)) for i in range(W)]
        for x, i in enumerate(range(H)):
            xlist = []
            for j in c:
                if j[0] == 0:
                    xlist.append(" ")
                else:
                    if x + 1 < j[1]:
                        c2 = random.choice(char)
                    else:
                        c2 = " "
                    xlist.append(c2)
            tlist.append(xlist)
        flag = 1
    c3 = [(random.randint(0, 1), random.randint(1, H * 2)) for i in range(W)]
    for y, j in enumerate(tlist):
        for x, k in enumerate(j):
            if k != " ":
                for l in range(len(tlist)):
                    try:
                        if tlist[y + (l + 1)][x] == " ":
                            tlist[y + (l + 1)][x] = random.choice(char)
                            j[x] = " "
                            break
                    except IndexError:
                        j[x] = " "
            try:
                if y + 1 <= c3[x][1] and c3[x][0] == 1:
                    j[x] = random.choice(char)
            except IndexError:
                pass
        for i in tlist:
            print(" ".join(i))
        time.sleep(0.025)
        print("\x1b[H", end="")
