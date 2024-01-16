def quick_select(array, k):
    arr = array
    size = len(arr)
    quick_select_util(arr, 0, size-1, k-1)
    return arr[k-1]

def quick_select_util(arr, lower, upper, k):
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
            arr[upper], arr[lower] = arr[lower], arr[upper] # swap
    
    # upper is the pivot position
    arr[upper], arr[start] = arr[start], arr[upper] # swap
    
    if k < upper: # pivot -1 is the upper for left sub array.
        quick_select_util(arr, start, upper - 1, k)
    
    if k > upper: #  pivot + 1 is the lower for right sub array.
        quick_select_util(arr, upper + 1, stop, k)   


# Testing Code
array = [3, 4, 2, 1, 6, 5, 7, 8, 10, 9]
value = quick_select(array, 5)
print("value at index 5 is: " , value)

"""
value at index 5 is:  5
"""
