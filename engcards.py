# save and remember english words with cards
# author Bulat

import tkinter
import random

root = tkinter.Tk()
root.title("engcards")
root.geometry("500x250")
forcount = {}
startstopflag = 0
with open("enru.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            eng, rus = row.split(":")
            forcount[eng] = rus
count = len(forcount.items())
def showcards():
    global startstopflag
    while startstopflag == 1:
        engvar, ruvar = random.choice(list(forcount.items()))
        lbl3.configure(text = engvar)
        lbl4.configure(text = ruvar)
        root.after(5000)
        root.update()
def startstopshowcards():
    global startstopflag
    if startstopflag == 0:
        btn2["text"] = "pause"
        startstopflag = 1
        showcards()
    else:
        btn2["text"] = "show cards"
        startstopflag = 0
def countwords():
    global count
    lbl5.configure(text = count)
def save():
    global count
    lbl3.configure(text = ent_eng.get())
    lbl4.configure(text = ent_ru.get())
    if forcount.get(ent_eng.get()):
        ent_eng.delete(0, "end")
        ent_ru.delete(0, "end")  
    else:
        with open("enru.txt", "a") as file:
            file.write("{}:{}\n".format(ent_eng.get(),ent_ru.get()))
            forcount[ent_eng.get()] = ent_ru.get()
        count += 1
        ent_eng.delete(0, "end")
        ent_ru.delete(0, "end")
    countwords()
lbl1 = tkinter.Label(root, text = "english") # label "english"
lbl2 = tkinter.Label(root, text = "translated") # label "russian"
lbl3 = tkinter.Label(root, text = "") # label word in english 
lbl4 = tkinter.Label(root, text = "") # label translated
lbltotal = tkinter.Label(root, text = "total words: ") # label text of total of dictionary
lbl5 = tkinter.Label(root, text = "") # label of number count dict.
ent_eng = tkinter.Entry(root, width = 40) # entry of english word
ent_eng.focus()
ent_ru = tkinter.Entry(root, width = 40) # entry of translated
btn1 = tkinter.Button(root, text = "save", command = save)
btn2 = tkinter.Button(root, text = "show cards", command = startstopshowcards)
lbl1.pack()
ent_eng.pack()
lbl2.pack()
ent_ru.pack()
btn1.pack()
lbl3.pack()
lbl4.pack()
lbltotal.pack()
lbl5.pack()
btn2.pack()
countwords()
if __name__ == "__main__":
    root.mainloop()
