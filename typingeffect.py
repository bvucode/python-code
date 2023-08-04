import os
import sys
import time

def typingeffect(m):
    for char in m:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)

t1 = "hello, wordld!"
t2 = "python is awesome"

mlist = [t1, t2]

for i in mlist:
    typingeffect(i)
    time.sleep(1)
