def Partition012(arr):
    size = len(arr)
    start = 0
    end = size - 1
    i = 0
    while i <= end:
        if arr[i] == 0 :
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1
        elif arr[i] == 2 :
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else :
            i += 1

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Partition012(arr)
print arr