tasklist = []

print("taskmanager")
print("\ntop tasks is most important and urgent")
print("\n add - text and enter \n show - show task \n take - take task \n exit - exit \n")

def main():
    inputtask = input(">> ")
    getfunc(inputtask)

def getfunc(arg):
    if not arg:
        main()
    elif arg == "show":
        print("to do:")
        for i in range(len(tasklist)):
            print("{}) {}".format(i + 1, tasklist[i]))
    elif arg == "take":
        print("{} is done.".format(tasklist[0]))
        del tasklist[0]
    elif arg == "exit":
        leave()
    else:
        tasklist.append(arg)

def leave():
    exit()

while True:
    main()
