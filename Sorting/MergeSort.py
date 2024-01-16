import math

def merge_sort(array):
    arr = array
    size = len(arr)
    temp_array = [0] * size
    merge_sort_util(arr, temp_array, 0, size - 1)
    
def merge_sort_util(arr, temp_array, lower, upper):
    if lower >= upper:
        return
    middle = (lower + upper) // 2
    merge_sort_util(arr, temp_array, lower, middle)
    merge_sort_util(arr, temp_array, middle + 1, upper)
    merge(arr, temp_array, lower, middle, upper)

def merge(arr, temp_array, lower, middle, upper):
    lower_start = lower
    lower_stop = middle
    upper_start = middle + 1
    upper_stop = upper
    count = lower
    
    while lower_start <= lower_stop and upper_start <= upper_stop:
        if arr[lower_start] < arr[upper_start]:
            temp_array[count] = arr[lower_start]
            count += 1
            lower_start += 1
        else:
            temp_array[count] = arr[upper_start]
            count += 1
            upper_start += 1
            
    while lower_start <= lower_stop:
        temp_array[count] = arr[lower_start]
        count += 1
        lower_start += 1
        
    while upper_start <= upper_stop:
        temp_array[count] = arr[upper_start]
        count += 1
        upper_start += 1
    
    i = lower
    while i <= upper:
        arr[i] = temp_array[i]
        i += 1


array = [3, 4, 2, 1, 6, 5, 7, 8, 1, 1]
merge_sort(array)
print(array)

"""
[1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
"""