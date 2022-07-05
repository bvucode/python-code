def binarysearch(xlist, item):
    low:int = 0
    high:int = len(xlist)-1

    while low <= high:
        mid:int = (low + high) // 2
        if xlist[mid] == item:
            return True
        elif xlist[mid] < item:
            low = mid + 1
        elif xlist[mid] > item:
            high = mid - 1
    return False
print(binarysearch(["a", "d", "e", "f", "x"], "f"))
    
