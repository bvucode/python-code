import random, time
print("\x1b[2J", end = "")
char = "abcdifg"
while True:
    print('\x1b[H', end='')
    for i in range(20):
        c = [random.choice(char) for i in range(20)]
        print(" ".join(c))
