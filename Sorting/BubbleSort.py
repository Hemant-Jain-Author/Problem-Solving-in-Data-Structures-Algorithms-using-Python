def less(value1, value2):
    return value1 < value2

def more(value1, value2):
    return value1 > value2

def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if more(arr[j], arr[j + 1]):
                #  Swapping 
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort2(arr):
    size = len(arr)
    swapped = 1
    for i in range(size - 1):
        swapped = 0
        for j in range(size - i - 1):
            if more(arr[j], arr[j + 1]):
                #  Swapping
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]
                swapped = 1
        if swapped == 0:
            break


array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
bubble_sort(array)
print(array)

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
bubble_sort2(array)
print(array)

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
