def SortedInsert(arr, value):
    arr.append(value)
    size = len(arr)
    while size > 0:
        if arr[size - 1] >= arr[size - 2]:
            break
        arr[size -1], arr[size - 2] = arr[size - 2], arr[size - 1] 
        size -= 1

def BinarySearch(arr, value):
    size = len(arr)
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False

arr = [1, 9, 2, 8, 3, 7, 4, 6, 5]
arr.sort()
print BinarySearch(arr, 4)
print BinarySearch(arr, 10)
SortedInsert(arr, 11)
SortedInsert(arr, 7)
print arr

#linear search method
def FixPoint(arr):
    size = len(arr)
    for i in range(size):
        if arr[i] == i:
            return i
    # fix point not found so return invalid index
    return -1

# Binary search method
def FixPoint2(arr):
    size = len(arr)
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    # fix point not found so return invalid index
    return -1
"""
arr = [-10, -2, 0, 3, 11, 12, 35, 51, 200]
print FixPoint(arr)
print FixPoint2(arr)
"""


def findMaxima(arr):
    size = len(arr)
    for i in range(size):
        if ((i == 0) or arr[i-1] < arr[i]) and ((i == size -1 ) or arr[i] > arr[i+1]):
            print arr[i],
    print ""

arr = [10, 20, 30, 40, 50]
findMaxima(arr)
arr = [50, 40, 30, 20, 10]
findMaxima(arr)
arr = [10, 30, 20, 1, 25, 90, 60]
findMaxima(arr)
arr = [10, 20, 40, 30]
findMaxima(arr)