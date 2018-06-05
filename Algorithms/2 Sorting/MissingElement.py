"""
Given an array, find the miximum and minimum value in the array and also find 
the values in range minimum and maximum that are absent in the array.
"""

def MissingValues(arr):
    size = len(arr)
    arr.sort()
    count = arr[0]
    missing = []
    i = 0
    while i < size:
        if count == arr[i]:
            count += 1
            i += 1
        else:
            missing.append(count)
            count += 1
    print missing

import sys
def MissingValues2(arr):
    size = len(arr)
    missing = []
    dict = {}
    minVal = sys.maxint
    maxVal = -sys.maxint
    for i in range(size):
        dict[arr[i]] = 1
        if minVal > arr[i]:
            minVal = arr[i]
        if maxVal < arr[i]:
            maxVal = arr[i]
    for i in range(minVal, maxVal+1):
        if i not in dict:
            missing.append(i)
    print missing



arr = [4, 5, 3, 8, 6,10]
MissingValues(arr)
MissingValues2(arr)
