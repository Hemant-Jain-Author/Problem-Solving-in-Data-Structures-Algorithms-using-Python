#!/usr/bin/env python
import math

def MergeSort(array):
    arr = array
    size = len(arr)
    tempArray = [0] * size
    mergeSrt(arr, tempArray, 0, size - 1)
    
def mergeSrt(arr, tempArray, lowerIndex, upperIndex):
    if lowerIndex >= upperIndex:
        return
    middleIndex = math.floor((lowerIndex + upperIndex) / 2)
    mergeSrt(arr, tempArray, lowerIndex, middleIndex)
    mergeSrt(arr, tempArray, middleIndex + 1, upperIndex)
    merge(arr, tempArray, lowerIndex, middleIndex, upperIndex)

def merge(arr, tempArray, lowerIndex, middleIndex, upperIndex):
    lowerStart = lowerIndex
    lowerStop = middleIndex
    upperStart = middleIndex + 1
    upperStop = upperIndex
    count = lowerIndex
    
    while lowerStart <= lowerStop and upperStart <= upperStop:
        if arr[lowerStart] < arr[upperStart]:
            tempArray[count] = arr[lowerStart]
            count += 1
            lowerStart += 1
        else:
            tempArray[count] = arr[upperStart]
            count += 1
            upperStart += 1
            
    while lowerStart <= lowerStop:
        tempArray[count] = arr[lowerStart]
        count += 1
        lowerStart += 1
        
    while upperStart <= upperStop:
        tempArray[count] = arr[upperStart]
        count += 1
        upperStart += 1
    
    i = lowerIndex
    while i <= upperIndex:
        arr[i] = tempArray[i]
        i += 1


array = [3, 4, 2, 1, 6, 5, 7, 8, 1, 1]
MergeSort(array)
print(array)
