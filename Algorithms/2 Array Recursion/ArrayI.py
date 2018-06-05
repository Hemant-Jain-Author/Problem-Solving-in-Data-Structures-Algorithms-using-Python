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


def indexArray2(arr):
    size = len(arr)
    for i in range(size):
        while arr[i] != -1 and arr[i] != i:
            # swap arr[i] and arr[arr[i]]
            temp = arr[i]
            arr[i] = arr[temp]
            arr[temp] = temp


arr = [ 8, -1, 6, 1, 9, 3, 2, 7, 4, -1 ]
indexArray2( arr)
print arr

arr = [20, 11, 10, 9, 5, 13, 16, 2, 14, 17,19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 4]
indexArray2( arr)
print arr


"""
Given an unsorted array , find smallest possitive number missing in the array.
"""
def SmallestPossitiveMissingNumber(arr):
    size = len(arr)
    for i in range(1, size+1, 1):
        found = False
        for j in range(size):
            if arr[j] == i:
                found = True
                break
        if found == False:
            return i
    return -1

def SmallestPossitiveMissingNumber2(arr):
    size = len(arr)
    hs = {}
    for i in range(size):
        hs[arr[i]] = 1
    
    for i in range(1, size+1, 1):
        if i not in hs:
            return i
    return -1


def SmallestPossitiveMissingNumber3(arr):
    size = len(arr)
    aux = [-1]*size
    for i in range(size):
        if arr[i] > 0 and arr[i] <= size:
            aux[arr[i] - 1] = arr[i]

    for i in range(size):
        if aux[i] != i+1 :
            return i+1
    return -1

def SmallestPossitiveMissingNumber4(arr):
    size = len(arr)
    for i in range(size):
        curr = i
        value = -1
        if arr[curr] > 0 :
            # swaps to move elements in proper possition.
            while curr >= 0 and curr < size and arr[curr] != curr+1 :
                next = arr[curr]
                arr[curr] = value
                value = next
                curr = next - 1

    for i in range(size):
        if arr[i] != i+1 :
            return i+1
    return -1

def SmallestPossitiveMissingNumber5(arr):
    size = len(arr)
    for i in range(size):
        while arr[i] != i+1 and arr[i] > 0 and arr[i] <= size:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp

    for i in range(size):
        if arr[i] != i+1 :
            return i+1
    return -1
"""
arr = [2, 3, 7, 6, 8, -1, -10, 15]
print SmallestPossitiveMissingNumber5(arr)
arr = [2, 3, 7, 6, 8, 1, 4, 5]
print SmallestPossitiveMissingNumber5(arr)
"""
"""
Given an array of length N. It contains unique elements from 1 to N. 
Sort the elements of the array.
"""

def Sort1toN(arr):
    size = len(arr)
    for i in range(size):
        curr = i
        value = -1
        # swaps to move elements in proper possition.
        while curr >= 0 and curr < size and arr[curr] != curr+1 :
            next = arr[curr]
            arr[curr] = value
            value = next
            curr = next - 1

def Sort1toN2(arr):
    size = len(arr)
    for i in range(size):
        while arr[i] != i+1 and arr[i] > 1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] =  temp
"""
arr = [10, 7, 9, 2, 8, 3, 5, 4, 6, 1]
print arr
print Sort1toN2(arr)
print arr
"""