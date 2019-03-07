"""
Find minimum difference between any two array element.
"""
import sys
def findMinDiff(arr):
    size = len(arr)
    arr.sort()
    diff = sys.maxsize
 
    for i in range(size - 1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]

    return diff
 
arr = [1, 6, 4, 19, 17, 20]
print(findMinDiff(arr))