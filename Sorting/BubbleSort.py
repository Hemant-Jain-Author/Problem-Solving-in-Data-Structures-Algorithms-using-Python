#!/usr/bin/env python

def less(value1, value2):
    return value1 < value2

def more(value1, value2):
    return value1 > value2

def BubbleSort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if more(arr[j], arr[j + 1]):
                #  Swapping 
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def BubbleSort2(arr):
    size = len(arr)
    swapped = 1
    i = 0
    for i in range(size - 1):
        swapped = 0
        for j in range(size - i - 1):
            if more(arr[j], arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = 1
        if swapped == 0:
            break


array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
BubbleSort(array)
print(array)

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
BubbleSort2(array)
print(array)
