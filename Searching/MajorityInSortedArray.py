"""
Given a sorted array find if their is a majority and find the majority element.
"""

def isMajority(arr):
    size = len(arr)
    majority = arr[size/2]
    i = FirstIndex(arr, 0, size - 1, majority)
    # we are using majority element form array so 
    # we will get some valid index always.

    if ((i + size/2) <= (size - 1)) and arr[i + size/2] == majority:
        return True
    else:
        return False

# Using binary search method. 
def FirstIndex(arr, low, high, value):
    if high >= low:
        mid = (low + high)/2 

        """ 
        Find first occurance of value, either it should be the first element of the array or 
        the value before it is smaller then it.
        """ 
        if (mid == 0 or arr[mid-1] < value ) and (arr[mid] == value):
            return mid
        elif arr[mid] < value:
            return FirstIndex(arr, mid + 1, high, value)
        else:
            return FirstIndex(arr, low, mid -1, value)
    return -1

arr = [3, 3, 3, 3, 4, 5, 10]
if (isMajority(arr)):
    print ("Majority found ", arr[len(arr)/2])
else:
    print ("Majority not found")