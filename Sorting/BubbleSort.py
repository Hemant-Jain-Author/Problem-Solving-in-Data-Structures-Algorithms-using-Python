#!/usr/bin/env python

def less(value1, value2):
    return value1 < value2

def more(value1, value2):
    return value1 > value2

def BubbleSort(arr):
    size = len(arr)
    i = 0
    while i < (size - 1):
        j = 0
        while j < size - i - 1:
            if more(arr[j], arr[j + 1]):
                #  Swapping 
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
        i += 1

def BubbleSort2(arr):
    size = len(arr)
    swapped = 1
    i = 0
    while i < (size - 1) and swapped == 1:
        swapped = 0
        j = 0
        while j < size - i - 1:
            if more(arr[j], arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = 1
            j += 1
        i += 1


array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
BubbleSort(array)
print(array)

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
BubbleSort2(array)
print(array)
