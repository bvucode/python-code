# taskmanager

print("taskmanager")
print("\ntop tasks is most important and urgent")
print("\n show - show task \n take - take task \n exit - exit \n")

tasklist = []
def main():
    global xt
    xt = input(">> ")
    getf(xt)
def getf(arg):
    if not arg:
        main()
    elif arg == "show":
        print("to do:")
        for i in range(len(tasklist)):
            tvar = i
            tvar += 1
            print("{}) {}".format(tvar, tasklist[i]))
    elif arg == "take":
        print("{} is done.".format(tasklist[0]))
        del tasklist[0]
    elif arg == "exit":
        leave()
    else:
        tasklist.append(xt)
def leave():
    exit()
while True:
    main()
