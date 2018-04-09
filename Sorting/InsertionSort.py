#!/usr/bin/env python

def more(value1, value2):
    return value1 > value2

def InsertionSort(arr):
    size = len(arr)
    i = 1
    while i < size:
        temp = arr[i]
        j = i;
        while j > 0 and more(arr[j - 1], temp):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
        i += 1


array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
InsertionSort(array)
print array
