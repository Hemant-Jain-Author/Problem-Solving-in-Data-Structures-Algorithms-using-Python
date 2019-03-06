"""
Minimum swaps required to sort a binary array with 0 and 1 as elements.
"""

def MinSwaps(arr):
    size = len(arr)
    start = 0
    end = size -1
    count = 0
    while start < end:
        if arr[start] == 0:
            start += 1
        elif arr[end] == 1:
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            count += 1
    print arr
    print count

arr = [0, 0, 1, 0, 1, 0, 1, 1]
arr = [0, 1, 0, 1, 0]
MinSwaps(arr)