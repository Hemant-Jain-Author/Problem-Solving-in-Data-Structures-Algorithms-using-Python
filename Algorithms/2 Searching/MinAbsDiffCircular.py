"""
Given an array of integers, find minimum absolute difference of adjacent element consider circular. array.
"""

import sys
def minAbsDiffAdjCircular(arr):
    size = len(arr)
    diff = sys.maxint
    if (size < 2): 
        return -1
    
    for i in range(size):
        diff = min(diff, abs(arr[i] - arr[(i + 1)%size]))
 
    return diff

arr = [5, 29, 18, 51, 11]
print minAbsDiffAdjCircular(arr)