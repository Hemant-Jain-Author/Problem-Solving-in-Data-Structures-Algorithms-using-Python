#!/usr/bin/env python
def SelectionSort(arr):
    # back array
    size = len(arr)
    i = 0
    while i < size - 1:
        maxIndex = 0
        j = 1
        while j < size - 1 - i:
            if arr[j] > arr[maxIndex]:
                maxIndex = j
            j += 1
        temp = arr[size - 1 - i]
        arr[size - 1 - i] = arr[maxIndex]
        arr[maxIndex] = temp
        i += 1

def SelectionSort2(arr):
    # front array
    size = len(arr)
    i = 0
    while i < size - 1:
        minIndex = i
        j = i + 1
        while j < size:
            if arr[j] < arr[minIndex]:
                minIndex = j
            j += 1
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
        i += 1


array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
SelectionSort(array)
print array


