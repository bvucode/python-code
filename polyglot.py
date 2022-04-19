import random
import re
import json

data = """{"i will not travel in winter":"я не буду путешествовать зимой",
     "what are you doing next week?":"что ты делаешь на следующей неделе?",
     "what do you think?":"что скажешь?",
     "how long have you know her?":"как давно вы с ней знакомы?",
     "is this your cellphone?":"это твой телефон?"}"""

listforhelp = ["i you he she we they it",
               "am are is",
               "was were won't",
               "have, has",
               "do did does",
               "this, that"]

d = json.loads(data)

def main():
    wl = []
    count = 0
    engvar, ruvar = random.choice(list(d.items()))
    print("\n{}\n".format(ruvar))
    ispl = spliting(engvar)
    for i in ispl:
        for j in listforhelp:
            x = spliting(j)
            tlist = []
            for k in x:
                if i == k:
                    tlist.append(k)
                    y = random.choice(x)
                    tlist.append(y)
                    print(tlist)
    tr = input("\ntranslate: ")
    if tr == "exit":
        leave()
    wl = spliting(tr)
    for i in wl:
        count += 1
        if i != ispl[count-1]:
            print("\nright answer: {}".format(engvar))
            break
        elif count == len(wl):
            print("\ngood!")
def spliting(text):
    wlist = []
    wlist = re.split("[\W\s]", text)
    return wlist
def leave():
    exit()
while True:
    main()
