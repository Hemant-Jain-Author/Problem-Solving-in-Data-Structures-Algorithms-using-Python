"""Given a sorted array rearrange it in maximum minimum form.
Input  : [1, 2, 3, 4, 5, 6, 7]
Output : [7, 1, 6, 2, 5, 3, 4]
"""
def MaxMinArr(arr):
    size = len(arr)
    aux = list(arr)
    start = 0
    stop = size - 1
    for i in range(size):
        if i % 2 == 0 :
            arr[i] = aux[stop]
            stop -= 1
        else :
            arr[i] = aux[start]
            start += 1


arr = [1, 2, 3, 4, 5, 6, 7]
MaxMinArr(arr)
print(arr)

"""
Without using any auxilary array.
1, 2, 3, 4, 5, 6, 7
7, 6, 5, 4, 3, 2, 1
7, 1, 2, 3, 4, 5, 6
7, 1, 6, 5, 4, 3, 2
7, 1, 6, 2, 3, 4, 5
7, 1, 6, 2, 5, 4, 3
7, 1, 6, 2, 5, 3, 4
"""
def ReverseArr(arr, start, stop):
    while start < stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        start += 1
        stop -= 1

def MaxMinArr2(arr):
    size = len(arr)
    for i in range(size-1):
        ReverseArr(arr, i, size-1)

arr = [1, 2, 3, 4, 5, 6, 7]
MaxMinArr2(arr)
print(arr)