import random, time

class PyMatrix:
    tlist = []
    w = 106
    h = 50
    char = ".,/)(><^?_+-%':&][#$!abcdefghijklmnopqrstuvwxyzABCDIFGHIJKLMNOPQRSTUVWXYZ0123456789"
    def __int__(self):
        self.tlist = tlist
        self.w = w
        self.h = h
        self.char = char
    def start(self):
        cf = [(random.randint(1, self.h), random.randint(1, self.h + 25)) for i in range(self.w)]
        for i in range(self.h):
            c = [" " for i in range(self.w)]
            self.tlist.append(c)
        for x, i in enumerate(self.tlist):
            for y, j in enumerate(i):
                if cf[y][0] >= x and cf[y][1] - x <= x:
                   self.tlist[x][y] = random.choice(self.char)
                   for i in self.tlist:
                       print(" ".join(i))
                   time.sleep(0.001)
                   print("\x1b[H", end="")
    def update(self):
        start = 0
        for i in range(self.w):
            c = 0
            for j in range(self.h):
                if self.tlist[j][i]  == " ":
                    c += 1
            if c == self.h:
                rn = random.randint(1, self.h - (self.h // 3))
                rr = random.randint(1, self.h - (self.h // 3))
                for k in range(rr - rn):
                    self.tlist[rn + (k + 1)][i] = random.choice(self.char)
        for i in range(self.w):
            for j in range(self.h):
                try:
                    if self.tlist[j][i] != " " and start == 0:
                        self.tlist[j][i] = " "
                        start = 1
                    elif self.tlist[j][i] == " " and start == 1:
                        self.tlist[j][i] = random.choice(self.char)
                        start = 0
                except IndexError:
                    self.tlist[j][i] = " "
                    self.tlist[0][i] = random.choice(self.char)
            for i in self.tlist:
                print(" ".join(i))
            time.sleep(0.001)
            print("\x1b[H", end="")
        return self.update()

m = PyMatrix()
m.start()
m.update()
