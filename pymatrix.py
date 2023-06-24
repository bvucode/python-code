import random, time
print("\x1b[2J", end = "")
tlist = []
flag = 0
W = 104
H = 50
char = ".,/)(><^?_+-%':&][#$!abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0123456789"
while True:
    print("\x1b[H", end="")
    start = 0
    if flag == 0:
        cf = [(random.randint(1, H), random.randint(1, H + 25)) for i in range(W)]
        for i in range(H):
            c = [" " for i in range(W)]
            tlist.append(c)
        for x, i in enumerate(tlist):
            for y, j in enumerate(i):
                if cf[y][0] >= x and cf[y][1] - x <= x:
                   tlist[x][y] = random.choice(char)
        flag = 1
    for i in range(W):
        for j in range(H):
            try:
                if tlist[j][i] != " " and start == 0:
                    tlist[j][i] = " "
                    start = 1
                elif tlist[j][i] == " " and start == 1:
                    tlist[j][i] = random.choice(char)
                    start = 0
            except IndexError:
                tlist[j][i] = " "
        for i in tlist:
            print(" ".join(i))
        time.sleep(0.001)
        print("\x1b[H", end="")
