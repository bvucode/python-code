# remember english words with cards
# author Bulat

import tkinter
import random

root = tkinter.Tk()
root.title("engcards")
root.geometry("500x350")
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
def stopshowcards():
    global startstopflag
    startstopflag = 1
def startshowcards():
    global startstopflag
    while startstopflag == 0:
        engvar, ruvar = random.choice(list(forcount.items()))
        lbl6.configure(text = engvar)
        lbl7.configure(text = ruvar)
        root.after(5000)
        root.update()
    else:
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
lbl2 = tkinter.Label(root, text = "russian") # label "russian"
lbl3 = tkinter.Label(root, text = "") # label word in english 
lbl4 = tkinter.Label(root, text = "") # label translated
lbltotal = tkinter.Label(root, text = "total words: ") # label text of total of dictionary
lbl5 = tkinter.Label(root, text = "") # label of number count dict.
lbl6 = tkinter.Label(root, text = "") # key
lbl7 = tkinter.Label(root, text = "") # value
ent_eng = tkinter.Entry(root, width = 40) # entry of english word
ent_eng.focus()
ent_ru = tkinter.Entry(root, width = 40) # entry of translated
btn1 = tkinter.Button(root, text = "save", command = save)
btn2 = tkinter.Button(root, text = "show cards", command = startshowcards)
btn3 = tkinter.Button(root, text = "stop show", command = stopshowcards)
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
btn3.pack()
lbl6.pack()
lbl7.pack()
countwords()
if __name__ == "__main__":
    root.mainloop()
