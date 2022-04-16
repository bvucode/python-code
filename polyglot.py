import random
import re
import json

data = """{"i will not travel in winter":"я не буду путешествовать зимой",
     "what are you doing next week?":"что ты делаешь на следующей неделе?",
     "what do you think?":"что скажешь?",
     "how long have you know her?":"как давно вы с ней знакомы?",
     "is this your cellphone?":"это твой телефон?"}"""

d = json.loads(data)

def main():
    count = 0
    engvar, ruvar = random.choice(list(d.items()))
    print("\n{}\n".format(ruvar))
    wlist = []
    wlist = re.split("[\W\s]", engvar) 
    for i in wlist:
        print(i)
    tr = input("\ntranslate: ")
    if tr == "exit":
        leave()
    wlist2 = []
    wlist2 = re.split("[\W\s]", tr)
    for i in wlist2:
        count += 1
        if i != wlist[count-1]:
            print("\nright answer: {}".format(engvar))
            break
        elif count == len(wlist):
            print("\ngood!")

def leave():
    exit()
while True:
    main()
