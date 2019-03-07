"""
Given two array find pair with minmum difference , pair should take one element from each array.
Brute force solution using two loops will be O(n2)
"""
import sys
def MinDiffPair(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    minDiff = sys.maxsize
    arr1.sort()
    arr2.sort()
    first = 0
    second = 0
    output = [0, 0]
    while first < size1 and second < size2:
        diff = abs(arr1[first] - arr2[second])
        if minDiff > diff:
            minDiff = diff
            output[0] = arr1[first]
            output[1] = arr2[second]
        if arr1[first] < arr2[second]:
            first += 1
        else:
            second += 1
    print(output)
    print(minDiff)
    return minDiff

arr1 = [1, 4, 12, 10, 2]
arr2 = [20, 128, 2354, 18, 7]
MinDiffPair(arr1, arr2)