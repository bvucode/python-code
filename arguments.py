import sys

args = sys.argv[:]
string = ""
c = 0
print("Len of elements in arguments is : {}".format(len(args)))
for i in args:
    if c == 1:
        string += i
    elif c > 1:
        string += " " + i
    c += 1
print(string)
