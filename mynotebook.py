# mynotebook
# author Bulat

import tkinter

root = tkinter.Tk()
root.title("mynotebook")
root.geometry("450x200")
forcount = {}
with open("enru.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            eng, rus = row.split(":")
            forcount[eng] = rus
count = len(forcount.items())
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
lbl1 = tkinter.Label(root, text = "english")
lbl2 = tkinter.Label(root, text = "russian")
lbl3 = tkinter.Label(root, text = "")
lbl4 = tkinter.Label(root, text = "")
lbl5 = tkinter.Label(root, text = "")
ent_eng = tkinter.Entry(root, width = 40)
ent_eng.focus()
ent_ru = tkinter.Entry(root, width = 40)
btn1 = tkinter.Button(root, text = "save", command = save)
lbl1.pack()
ent_eng.pack()
lbl2.pack()
ent_ru.pack()
btn1.pack()
lbl3.pack()
lbl4.pack()
lbl5.pack()
countwords()
root.mainloop()
