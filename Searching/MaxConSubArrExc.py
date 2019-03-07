"""
Given an array A of intergers and array B of integers, 
find maximum contigious subarray in A such that it does not contains elements in B.
"""

"""
Kadane’s Algorithm : to find maximum contigious subarray sum.
"""
def MaxConSub(A):
    sizeA = len(A)
    currMax = 0
    maximum =0
    for i in range(sizeA):
        currMax = max(A[i], currMax+A[i])
        if currMax < 0:
            currMax = 0
        if maximum < currMax:
            maximum = currMax
    print(maximum)


def MaxConSubArr(A, B):
    sizeA = len(A)
    sizeB = len(B)
    hs = {}
    for i in range(sizeB):
        hs[B[i]] = 1
    
    currMax = 0
    maximum =0
    for i in range(sizeA):
        if A[i] in hs:
            currMax = 0
        else :
            currMax = max(A[i], currMax+A[i])
            if currMax < 0:
                currMax = 0
            if maximum < currMax:
                maximum = currMax
    print(maximum)

def BinarySearch(arr, size, value):
    start = 0 
    stop = size - 1
    while start <= stop:
        mid = (start + stop)//2
        if value == arr[mid]:
            return True
        elif value > arr[mid]:
            start = mid+1
        else:
            stop = mid-1
    return False

"""
O(M + N) Solution.
"""


def MaxConSubArr2(A, B):
    sizeA = len(A)
    sizeB = len(B)
    B.sort()
    currMax = 0
    maximum =0
    for i in range(sizeA):
        if BinarySearch(B, sizeB, A[i]):
            currMax = 0
        else :
            currMax = max(A[i], currMax+A[i])
            if currMax < 0:
                currMax = 0
            if maximum < currMax:
                maximum = currMax
    print(maximum)

"""
O(MlogM + NlogM)  Solution.
for sorting and then for search each element.
"""

A = [1, 2, 3, 4, 5, -10, 6,7]
B = [ 1, 3]
MaxConSubArr(A, B)
MaxConSubArr2(A, B)