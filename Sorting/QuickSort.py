#!/usr/bin/env python
def QuickSort(array):
    arr = array
    size = len(arr)
    QuickSortUtil(arr, 0, size - 1)

def QuickSortUtil(arr, lower, upper):
    if upper <= lower:
        return
    pivot = arr[lower]
    start = lower
    stop = upper
    while lower < upper:
        while arr[lower] <= pivot and lower < upper:
            lower += 1
        while arr[upper] > pivot and lower <= upper:
            upper -= 1
        if lower < upper:
            swap(arr, upper, lower)
    swap(arr, upper, start)
    # upper is the pivot position
    QuickSortUtil(arr, start, upper - 1)
    # pivot -1 is the upper for left sub array.
    QuickSortUtil(arr, upper + 1, stop)
    #  pivot + 1 is the lower for right sub array.
    
def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


array = [3, 4, 2, 1, 6, 5, 7, 8, 1, 1]
QuickSort(array)
print array

