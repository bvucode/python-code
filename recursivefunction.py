def somefunction(n):
    print(n)
    if n == 1:
        return n
    return somefunction(n - 1)

somefunction(3)
