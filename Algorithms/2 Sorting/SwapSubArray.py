"""
Given an array of integers, find if reversing a sub-array makes the array sorted.

In this algorithm start and stop are the boundry of reversed sub-array whose 
revarsal makes the whole array sorted.

"""
def checkReverse(arr):
    size = len(arr)
    start = -1
    stop = -1
    for i in range(size-1):
        if arr[i] > arr[i+1] :
            start = i
            break

    if start == -1:
        return True
 
    for i in range(start, size-1):
        if arr[i] < arr[i+1]:
            stop = i
            break

    if stop == -1:
        return True

    #increasing property
    # after reversal the sub array should fit in the array.
    if arr[start - 1] > arr[stop] or arr[stop + 1] < arr[start]:
        return False
 
    for i in range(stop+1, size-1):
        if arr[i] > arr[i+1]:
            return False

    return True

arr =[1,2,3,6,5,4,7,8,9]
print checkReverse(arr)
arr =[1,2,3,6,5,4]
print checkReverse(arr)
arr =[1,2,3,7,5,4,6,8,9]
print checkReverse(arr)
arr =[1,2,3,4,5,6,7]
print checkReverse(arr)
arr =[7,6,5,4,3,2,1]
print checkReverse(arr)