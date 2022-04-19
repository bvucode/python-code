# password generator

import random

print("password generator and save")
s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "0123456789"
s3 = "@!.,"
def main():
    l = input("password length: ")
    if l == "exit":
        leave()
    generate(int(l))
def generate(x):
    p1 = ""
    p2 = random.choice(s2)
    p3 = random.choice(s3)
    for i in range(x-2):
        p1 += random.choice(s1)
    p = p1 + p2 + p3
    u = p.capitalize()
    print("password is {}".format(u))
def leave():
    exit()
while True:
    main()
