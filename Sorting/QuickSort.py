def quick_sort(array):
    arr = array
    size = len(arr)
    quick_sort_util(arr, 0, size - 1)

def quick_sort_util(arr, lower, upper):
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
    swap(arr, upper, start)
    # upper is the pivot position
    quick_sort_util(arr, start, upper - 1) # pivot -1 is the upper for left sub array.
    quick_sort_util(arr, upper + 1, stop) #  pivot + 1 is the lower for right sub array.

def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]

array = [3, 4, 2, 1, 6, 5, 7, 8, 1, 1]
quick_sort(array)
print(array)

"""
[1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
"""

