import random

print("game orel or reshka")

def main():
    guess = ""
    xlist = ["reshka", "orel"]
    while guess not in xlist:
        guess = input("orel or reshka: ")
        t = random.randint(0, 1)
        if guess == xlist[t]:
            print("yes")
        else:
            print("no")
while True:
    main()
