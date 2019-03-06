"""
Given an array of size N, the elements in the array may be repeted. 
You need to find sum of distinct elements of the array.
"""

def SumDistinct(arr):
    size = len(arr)
    arr.sort()
    output = []
    sum = 0
    for i in range(size - 1):
        if arr[i] != arr[i+1]:
            output.append(arr[i])
            sum += arr[i]
    sum += arr[size - 1]
    print sum

arr = [1, 2, 3, 1, 1, 4, 5, 6]
SumDistinct(arr)