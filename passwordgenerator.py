# password generator

import random
import json

print("password generator and save")
s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "0123456789"
def main():
    l = input("password length: ")
    if l == "exit":
        leave()
    generate(int(l))
def save(x):
    print("password is {}".format(x))
def generate(x):
    p1 = ""
    p2 = random.choice(s2)
    for i in range(x-1):
        p1 += random.choice(s1)
    p = p1 + p2
    u = p.capitalize()
    save(u)
def leave():
    exit()
while True:
    main()
