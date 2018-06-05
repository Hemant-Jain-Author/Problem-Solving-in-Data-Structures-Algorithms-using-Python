
"""
Given an array and two numbers X and Y, 
find the minimum distance between X and Y in array.
"""
import sys

def minDist(arr, first, second):
    size = len(arr)
    minDist = sys.maxsize
    for i in range(size):
        for j in range(i + 1, size):
            if ((arr[i] == first and arr[j] == second) or (arr[i] == second and arr[j] == first)) and minDist > (j - i):
                minDist = (j - i)
        return minDist

def minDist2(arr, first, second):
    size = len(arr)
    minDist = sys.maxsize
    prev = -1
    for i in range(size):
        if arr[i] == first or arr[i] == second :
            if prev == -1 :
                prev = i
            elif arr[prev] != arr[i] and (i - prev) < minDist :
                minDist = (i - prev)
                prev = i
            else :
                prev = i
    return minDist

arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
first = 3
second = 6
print minDist(arr, first, second)
print minDist2(arr, first, second)