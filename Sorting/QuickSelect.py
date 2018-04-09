#!/usr/bin/env python
def QuickSelect(array, k):
    arr = array
    size = len(arr)
    SelectUtil(arr, 0, size-1, k)
    return arr[k-1]

def SelectUtil(arr, lower, upper, k):
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
    swap(arr, upper, start)    # upper is the pivot position
    
    if k < upper: 
        # pivot -1 is the upper for left sub array.
        SelectUtil(arr, start, upper - 1, k)
    
    if k > upper:
        #  pivot + 1 is the lower for right sub array.
        SelectUtil(arr, upper + 1, stop, k)   
          
def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
    

array = [3, 4, 2, 1, 6, 5, 7, 8, 10, 9]
value = QuickSelect(array, 5)
print("value at index 5 is : " , value, end=' ')

