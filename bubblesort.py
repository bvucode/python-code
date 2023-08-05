def bubblesort(arr, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

l = [28, 35, 46, 67, 24, 32, 44]

res = bubblesort(l, 7)
print(res)
