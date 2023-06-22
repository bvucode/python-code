import random, time
print("\x1b[2J", end = "")
tlist = []
flag = 0
W = 104
H = 50
char = ".,/)(><^?_+-%':&][#$!abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0123456789"
while True:
    print("\x1b[H", end="")
    if flag == 0:
        cf = [(random.randint(0, 3), random.randint(5, H)) for i in range(W)]
        for i in range(H):
            c = [" " for i in range(W)]
            tlist.append(c)
        for y, j in enumerate(tlist[0]):
            if cf[y][0] == 1:
                for i in range(cf[y][1]):
                    tlist[i][y] = random.choice(char)
        flag = 1
    for y, j in enumerate(tlist):
        for x, k in enumerate(j):
            if k != " ":
                try:
                    for i in range(H):
                        if tlist[y + i][x] == " ":
                            tlist[y + i][x] = random.choice(char)
                            j[x] = " "
                            try:
                                if tlist[y][x + 1] == " " and random.randint(1, 10) == 1:
                                    rn = random.randint(5, H)
                                    for l in range(rn):
                                        tlist[l][x + 1] = random.choice(char)
                            except IndexError:
                                pass
                            break
                except IndexError:
                    j[x] = " "
                    tlist[-1][x] = " "
                    """
                try:
                    if tlist[y][x + 1] == " ":
                        rn = random.randint(1, H // 2)
                        for l in range(rn):
                            tlist[l][x + 1] = random.choice(char)
                except IndexError:
                    pass
                    """
            for i in tlist:
                print(" ".join(i))
            time.sleep(0.00001)
            print("\x1b[H", end="")
