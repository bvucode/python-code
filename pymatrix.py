import random, time
print("\x1b[2J", end = "")
char = " abcdifg "
while True:
    print('\x1b[H', end='')
    flag = 0
    c = []
    for i in range(20):
        while flag == 0:
            c = [random.choice(char) for i in range(20)]
            print(" ".join(c))
            flag = 1
        else:
            xlist = []
            for l in c:
                if l == " ":
                    xlist.append(" ")
                else:
                    c2 = random.choice(char)
                    xlist.append(c2)
            print(" ".join(xlist))
    time.sleep(0.5)
