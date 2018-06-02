#!/usr/bin/env python
def BucketSort(arr, lowerRange, upperRange):
    array = arr
    dataRange = upperRange - lowerRange
    lowerRange = lowerRange
    size = len(array)
    count = [0] * dataRange
    for i in range(size):
        count[array[i] - lowerRange] += 1
    
    j = 0
    for i in range(dataRange):
        while count[i] > 0:
            array[j] = i + lowerRange
            count[i] -= 1
            j += 1

array = [23, 24, 22, 21, 26, 25, 27, 28, 21, 21]
BucketSort(array, 20, 30)
print(array)
