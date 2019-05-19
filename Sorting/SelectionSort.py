#!/usr/bin/env python
def SelectionSort(arr):
    # back array
    size = len(arr)
    for i in range(size - 1):
        maxIndex = 0
        for j in range(1, size - i):
            if arr[j] > arr[maxIndex]:
                maxIndex = j
        temp = arr[size - 1 - i]
        arr[size - 1 - i] = arr[maxIndex]
        arr[maxIndex] = temp

def SelectionSort2(arr):
    # front array
    size = len(arr)
    for i in range(size - 1):
        minIndex = i
        for j in range(i+1, size):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
array = [4, 5, 3, 2, 6, 7, 1, 8, 9, 10]
SelectionSort(array)
print(array)