"""
Find kth smallest elements in an unsorted array.
"""

def KthSmallest(arr, k):
    arr.sort()
    return arr[k-1]

import heapq
def KthSmallest2(arr, k):
    size = len(arr)
    heapq.heapify(arr)
    i = 0
    value = 0
    while i < size and i < k:
        value = heapq.heappop(arr)
        i += 1
    return value

"""
Quick select method
"""
def QuickSelect(array, k):
    arr = array
    size = len(arr)
    QuickSelectUtil(arr, 0, size-1, k)
    return arr[k-1]

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
    print(KthSmallest(first, 5))
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(KthSmallest2(first, 5))
    first = [1, 7, 5, 4, 8, 3, 9, 2, 6, 10]
    print(QuickSelect(first, 5))

main()