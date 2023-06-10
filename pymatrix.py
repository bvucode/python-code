import random
print("\x1b[2J", end = "")
char = " a b c d e "
while True:
    xlist = []
    c = ""
    for i in range(200):
        c += random.choice(char)
    xlist.append(c)
    for j in range(40):
        for k in xlist[0]:
            a = ""
            for l in k:
                if l == " ":
                    a += " "
                else:
                    a += random.choice(char)
            xlist.append(a)    
    print("\x1b[H", end = "")
    for i in xlist:
        for j in i:
            print(j, end = "")
