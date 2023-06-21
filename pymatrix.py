import random, time
print("\x1b[2J", end = "")
tlist = []
flag = 0
char = ".,/)(><^?_+-%':&][#$!abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0123456789"
W = 104
H = 50
while True:
    print("\x1b[H", end="")
    c = [(random.randint(0, 1), random.randint(1, H)) for i in range(W)]
    if flag == 0:
        for i in range(H):
            c = [" " for i in range(W)]
            tlist.append(c)
        flag = 1
    for y, j in enumerate(tlist):
        for x, k in enumerate(j):
            if c[x][0] == 1:
                for l in range(len(tlist)):
                    try:
                        if tlist[y + (l + 1)][x] == " ":
                            tlist[y + (l + 1)][x] = random.choice(char)
                            break
                    except IndexError:
                        j[x] = " "
            try:
                if y + 1 >= c[x][1] and c[x][0] == 1:
                    j[x] = random.choice(char)
                    j[x] = " "
            except IndexError:
                pass
        for i in tlist:
            print(" ".join(i))
        time.sleep(0.025)
        print("\x1b[H", end="")
