"""
Given an array you need to find balance point or balance index. 
An index is balanced index if the element in the right of it and 
elements in the right of it have same sum.
"""

def findBalancedPoint(arr):
    size = len(arr)
    first = 0
    second = 0
    for i in range(1, size):
        second += arr[i]
    
    for i in range(size):
        if first == second :
            print i ,
        if i < size - 1:
            first += arr[i]
            second -= arr[i+1]

    
arr = [-7, 1, 5, 2, -4, 3, 0]
findBalancedPoint(arr)