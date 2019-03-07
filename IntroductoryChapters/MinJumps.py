"""
Given an array of positive integers indicates maximum number of steps jump that can be taken forward.
Write a function to return the minimum number of jumps needed to reach from start of array
to its end.

Use an auxilary array to store how many steps needed to reach some index.
O(nk)
"""
import sys
def minJumps(arr):
    size = len(arr)
    jumps = [sys.maxsize]*size
    jumps[0] = 0
 
    for i in range(size):
        steps = arr[i]
        # error checks can be added hear.
        j = i + 1
        while j <= i + steps and j < size:
            jumps[j] = min(jumps[j], jumps[i] + 1)
            j += 1
        print(jumps)
    return jumps[size-1]
 
arr = [1, 4, 3, 7, 6, 1, 0, 3, 5, 1, 10]
print(minJumps(arr))