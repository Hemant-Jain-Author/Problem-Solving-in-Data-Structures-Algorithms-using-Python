#!/usr/bin/env python
def bucket_sort(arr, lower_range, upper_range):
    array = arr
    data_range = upper_range - lower_range
    lower_range = lower_range
    size = len(array)
    count = [0] * data_range
    for i in range(size):
        count[array[i] - lower_range] += 1
    
    j = 0
    for i in range(data_range):
        while count[i] > 0:
            array[j] = i + lower_range
            count[i] -= 1
            j += 1

array = [23, 24, 22, 21, 26, 25, 27, 28, 21, 21]
bucket_sort(array, 20, 30)
print(array)

"""
[21, 21, 21, 22, 23, 24, 25, 26, 27, 28]
"""