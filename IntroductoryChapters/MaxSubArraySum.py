# Find maximum contiguous subarray

import sys

def maxSubArraySum(arr):
    size = len(arr)
      
    maximum = 0
    maxCurr = 0
      
    for i in range(size):
        maxCurr = maxCurr + a[i]
        if maxCurr < 0:
            maxCurr = 0
        elif (maximum < maxCurr):
            maximum = maxCurr
 
    return maximum
  
# Driver function to check the above function 
a = [-1, -3, 4, -1, -2, 1, 5]
print(maxSubArraySum(a))