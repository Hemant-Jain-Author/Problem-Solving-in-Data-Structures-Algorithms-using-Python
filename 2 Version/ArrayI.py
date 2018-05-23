"""
Given array of size N, containing elements from 0 to N-1. 
All values from O to N-1 are present in array and if they 
are not there then -1 is there to take its place.
Arrange values of array so that value i is stored at arr[i].
"""
def indexArray( arr):
    size = len(arr)
    for i in range(size):
        curr = i
        value = -1

        # swaps to move elements in proper possition.
        while arr[curr] != -1 and arr[curr] != curr:
            temp = arr[curr]
            arr[curr] = value
            value = curr = temp

        # if some swaps happened.
        if value != -1: 
            arr[curr] = value

arr = [ 8, -1, 6, 1, 9, 3, 2, 7, 4, -1 ]
indexArray( arr)
print arr

arr = [20, 11, 10, 9, 5, 13, 16, 2, 14, 17,19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 4]
indexArray( arr)
print arr