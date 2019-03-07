"""
Given an array of integers, find minimum absoulute difference pair of all the possible pairs.

first approach is to find each pair by runnning two loop and finding minimum among them.
O(n2)
"""
"""
Using sorting munimum diff pairs will be adjacent to each other.
"""
import sys
def MinAbsPairDifferences(arr):
    size = len(arr)
    minimum = sys.maxsize
    for i in range(size):
        for j in range(i+1, size):
            minimum = min(abs(arr[i] - arr[j]), minimum)
    return minimum 


def MinAbsPairDifferences2(arr):
    size = len(arr)
    arr.sort()
    minimum = min(abs(arr[0] - arr[1]), abs(arr[size-2] - arr[size-1]))
    for i in range(1, size - 1):
        temp = min(abs(arr[i] - arr[i - 1]), abs(arr[i] - arr[i + 1]))
        minimum = min(temp, minimum)
    return minimum 
         
 
# Driver code
arr = [5, 101, 11, 14, 18, 71]
print(MinAbsPairDifferences(arr))
print(MinAbsPairDifferences2(arr))