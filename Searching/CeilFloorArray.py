"""
Given a sorted array you need to find ceil or floor of an input value. 
A ceil is the value in array which is just grater then the given input value.
A floor is a value in array which is just smaller then the given input value.
"""

def findFloor(arr, value):
    size = len(arr)
    start = 0
    stop = size -1
    while start <= stop:
        mid = (start + stop)//2
        # search value is equal to arr[mid] value..
        # search value is grater then mid index value and less then mid+1 index value.
        # value is grater then arr[size-1] then floor is arr[size-1]
        if arr[mid] == value or ( arr[mid] < value and (mid == size-1 or arr[mid + 1] > value)):
            return mid
        elif arr[mid] < value:
            start = mid+1
        else:
            stop = mid-1
    return -1

def findCeil(arr, value):
    size = len(arr)
    start = 0
    stop = size -1
    
    while start <= stop:
        mid = (start + stop)//2
        # search value is equal to arr[mid] value..
        # search value is less then mid index value and grater then mid-1 index value.
        # value is less then arr[0] then ceil is arr[0]
        if arr[mid] == value or ( arr[mid] > value and (mid == 0 or arr[mid - 1] < value)):
            return mid
        elif arr[mid] < value:
            start = mid+1
        else:
            stop = mid-1
    return -1

arr = [2, 4, 6, 8, 10, 12, 14]
for i in range(20):
    print(i , findCeil(arr, i), findFloor(arr, i))