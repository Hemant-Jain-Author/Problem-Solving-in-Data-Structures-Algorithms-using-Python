"""
Given an array of N intergers you need to find if array elements can form an Arithimatic 
progression.
"""
import sys

def isAP(arr):
    size = len(arr)
    if (size <= 1): 
        return True

    arr.sort()
 
    diff = arr[1] - arr[0]
    for i in range(2, size):
        if (arr[i] - arr[i-1] != diff):
            return False
 
    return True

def isAP2(arr):
    size = len(arr)
    first = sys.maxint
    second = sys.maxint
    hs = {}
    for i in range(size):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif arr[i] < second:
            second = arr[i]
        
    diff = second - first

    for i in range(size):
        if arr[i] in hs:
            return False
        hs[arr[i]] = 1
    
    for i in range(size):
        value = first + i * diff
        if value not in hs or hs[value] != 1:
            return False
    return True

def isAP3(arr):
    size = len(arr)
    first = sys.maxint
    second = sys.maxint
    count = [0]*size
    for i in range(size):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif arr[i] < second:
            second = arr[i]
    
    diff = second - first

    for i in range(size):
        index = (arr[i] - first )/ diff
        if index > size - 1 or count[index] != 0:
            return False
        count[index] = 1
    
    for i in range(size):
        if count[i] != 1:
            return False
    return True

arr = [ 20, 25, 15, 5, 0, 10, 35, 30 ]
print isAP(arr)
arr = [ 20, 25, 15, 5, 0, 10, 35, 30 ]
print isAP2(arr)
arr = [ 20, 25, 15, 5, 0, 10, 35, 30 ]
print isAP3(arr)