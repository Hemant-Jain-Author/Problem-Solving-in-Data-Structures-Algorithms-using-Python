"""
Given an array integers with even number of elements
You need to make groups of 2 using these array elements 
such that the difference between the group with highest sum 
and the one with lowest sum is minimum.
"""
import sys
def PairMinimumSum(arr):
    size = len(arr)
    start = 0
    stop = size -1
    minimum = sys.maxsize
    maximum = -sys.maxsize
    arr.sort()
    while start < stop:
        minimum = min(minimum, arr[stop] + arr[start])
        maximum = max(maximum, arr[stop] + arr[start])
        start += 1
        stop -= 1

    return maximum - minimum

arr = [1, 4, 3, 2]
print(PairMinimumSum(arr))