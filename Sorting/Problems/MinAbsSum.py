"""
Given an array of integers with both +ve and -ve values. 
Find the two elements in the array such that their sum is minimum (closest to zero).

Compute sum for every pair of elements in array. 
Store minimum sum among them. Return the minimum sum.
"""
import sys

def MinAbsSum(arr):
    size = len(arr)
    arr.sort()
    minSum = sys.maxint
    low = 0
    high = size - 1

    while low < high:
        sum = arr[low] + arr[high]
        absSum = abs(sum)
        if absSum < minSum:
            minSum = absSum
        if sum < 0:
            low += 1
        else :
            high -= 1
    print minSum

arr = [1, 60, -10, 70, -80, 85]
print MinAbsSum(arr)