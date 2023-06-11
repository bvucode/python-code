import random, time
print("\x1b[2J", end = "")
char = " a b c d e f g h i j k l m n "
char2 = " .,/)(><^?_ +-%':&][#$! abcdefghijklmn opqrstuvwxyz ABCDIFGHIJKLMN OPQRSTUVWXYZ 01234 56789 "
while True:
    print('\x1b[H', end='')
    flag = 0
    c = []
    tlist = []
    for j in range(20):
        while flag == 0:
            c = [random.choice(char) for i in range(40)]
            tlist.append(c)
            print(" ".join(c))
            flag = 1
        else:
            xlist = []
            for l in c:
                if l == " ":
                    xlist.append(" ")
                else:
                    c2 = random.choice(char2)
                    xlist.append(c2)
            print(" ".join(xlist))
            tlist.append(xlist)
    time.sleep(0.45)
    print('\x1b[H', end='')
    for i in range(10):
        for y, j in enumerate(tlist):
            for x, k in enumerate(j):
                if k != " ":
                    j[x] = random.choice(char2)
        for i in tlist:
            print(" ".join(i))
        time.sleep(0.45)
        print('\x1b[H', end='')
    
