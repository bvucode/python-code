# generate and save password 
# author Bulat

import random
import json

print("password generator and save")
s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "0123456789"
dicw = {}
def main():
    l = int(input("password length: "))
    generate(l)
def save(x):
    print("password is {}".format(x))
    inp_q = input("save ? (y/n) ")
    if inp_q == "y":
        n = input("web-site: ")
        dicw[n] = x
        with open("passwords.json", "a") as file:
            json.dump(dicw, file)
            del dicw[n]
        print("save!")
def generate(x):
    p1 = ""
    p2 = random.choice(s2)
    for i in range(x-1):
        p1 += random.choice(s1)
    p = p1 + p2
    u = p.capitalize()
    save(u)
while True:
    main()
