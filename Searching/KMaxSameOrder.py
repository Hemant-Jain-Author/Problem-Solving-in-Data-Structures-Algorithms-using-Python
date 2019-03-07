"""
Given an array of integers of size N, 
You need to print k largest elements in the array in order 
in which they appear in the array.

first copy the array into another array.
then using quich select find the N-Kth elements in the array.
then scan the original array and print all the elements which have value
grater then or equal to k.
O(N) for k and O(N) for scan.

Another solution is to sort the array and again find the kth largest element.
scan the array and print all the elements which have value grater then or equal 
to the kth largest element.
"""
def KLargestElements(arrIn, k):
    size = len(arrIn)
    arr = list(arrIn)
    arr.sort()
    for i in range(size):
        if arrIn[i] >= arr[size - k]:
            print(arrIn[i], end=' ')


def QuickSelectUtil(arr, lower, upper, k):
    if upper <= lower:
        return
    pivot = arr[lower]
    start = lower
    stop = upper
    while lower < upper:
        while arr[lower] <= pivot and lower < upper:
            lower += 1
        while arr[upper] > pivot and lower <= upper:
            upper -= 1
        if lower < upper:
            arr[upper], arr[lower] = arr[lower], arr[upper]
    arr[upper], arr[start] = arr[start], arr[upper]    # upper is the pivot position
    
    if k < upper: 
        QuickSelectUtil(arr, start, upper - 1, k)
    
    if k > upper:
        QuickSelectUtil(arr, upper + 1, stop, k)   
          
def KLargestElements2(arrIn, k):
    size = len(arrIn)
    arr = list(arrIn)
    QuickSelectUtil(arr, 0, size-1, size - k)
    for i in range(size):
        if arrIn[i] >= arr[size - k]:
            print(arrIn[i], end=' ')

arr = [10, 50, 30, 60, 15]
KLargestElements(arr, 2)
print("")
KLargestElements2(arr, 2)
print("")
arr = [50, 8, 45, 12, 25, 40, 84]
KLargestElements(arr, 3)
print("")
KLargestElements2(arr, 3)
print("")

def KSmallestElements(arrIn, k):
    size = len(arrIn)
    arr = list(arrIn)
    arr.sort()
    for i in range(size):
        if arrIn[i] <= arr[k-1]:
            print(arrIn[i], end=' ')

def KSmallestElements2(arrIn, k):
    size = len(arrIn)
    arr = list(arrIn)
    QuickSelectUtil(arr, 0, size-1, k)
    for i in range(size):
        if arrIn[i] <= arr[k-1]:
            print(arrIn[i], end=' ')

arr = [4, 2, 6, 1, 5]
KSmallestElements(arr, 3)
print("")
KSmallestElements2(arr, 3)
print("")
arr = [ 1, 5, 8, 9, 6, 7, 3, 4, 2, 0]
KSmallestElements(arr, 5)
print("")
KSmallestElements2(arr, 5)
print("")