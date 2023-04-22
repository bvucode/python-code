import random

print("password generator and save")
char = "abcdefghijklmnopqrstuvwxyz"
numb = "0123456789"
symb = "@!.,"
def main():
    lenpass = input("password length: ")
    if lenpass == "exit":
        leave()
    generate(int(lenpass))
def generate(arg):
    part1 = ""
    part2 = random.choice(numb)
    part3 = random.choice(symb)
    for i in range(arg-2):
        part1 += random.choice(char)
    passst = part1 + part2 + part3
    print("password is {}".format(passst.capitalize()))
def leave():
    exit()
while True:
    main()
