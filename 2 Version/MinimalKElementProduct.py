"""
Given an array of possitive elements. Find minimum product of k elements in array.
"""
def KSmallestProduct(arr, k):
    arr.sort()
    product = 1
    for i in range(k):
        product *= arr[i]
    return product

import heapq
def KSmallestProduct2(arr, k):
    size = len(arr)
    heapq.heapify(arr)
    i = 0
    product = 1
    while i < size and i < k:
        product *= heapq.heappop(arr)
        i += 1
    return product

"""
Quick select method
"""
def KSmallestProduct3(array, k):
    arr = array
    size = len(arr)
    QuickSelectUtil(arr, 0, size-1, k)
    product = 1
    for i in range(k):
        product *= arr[i]
    return product

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
            swap(arr, upper, lower)
    swap(arr, upper, start)    # upper is the pivot position
    
    if k < upper: 
        # pivot -1 is the upper for left sub array.
        QuickSelectUtil(arr, start, upper - 1, k)
    
    if k > upper:
        #  pivot + 1 is the lower for right sub array.
        QuickSelectUtil(arr, upper + 1, stop, k)   
          
def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]


def main():
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(KSmallestProduct(first, 5))
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(KSmallestProduct2(first, 5))
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(KSmallestProduct3(first, 5))

main()