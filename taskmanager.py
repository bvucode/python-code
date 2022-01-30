# mytaskmanager
# author Bulat

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
    elif arg == "help":
        xhelp()
    else:
        tasklist.append(xt)
def xhelp():
    print("this is taskmanager.")
    print("\n show - show task \n take - take task \n help - help\n")
xhelp()
while True:
    main()
