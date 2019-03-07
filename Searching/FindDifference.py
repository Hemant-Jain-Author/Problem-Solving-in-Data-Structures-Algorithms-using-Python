"""
In an array of possitive integers find a pair whose difference is equal to a given value.
"""
def FindDifference(arr, value):
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if abs(arr[i] - arr[j]) == value:
                print("The pair is::", arr[i], "&" , arr[j])
                return True
    return False


def FindDifference2(arr, value):
    size = len(arr)
    first = 0
    second = 0
    arr.sort()
    print(arr)
    while first < size and second < size:
        curr = abs(arr[first] - arr[second])
        if curr == value:
            print("The pair is::", arr[first], "&", arr[second])
            return True
        elif curr > value:
            first += 1
        else:
            second += 1
    return False

first = [10, 20, 3, 4, 50, 80]
print((FindDifference(first, 70)))
first = [10, 20, 3, 4, 50, 80]

print(FindDifference2(first, 47))
print(FindDifference2(first, 17))
print(FindDifference2(first, 30))
print(FindDifference2(first, 46))


"""
Given an array of possitive integers and a number. 
You need to find a pair in array which is closest to given number.
"""
import sys
def ClosestPair(arr, value):
    size = len(arr)
    diff = sys.maxsize
    first = -1
    second = -1
    for i in range(size):
        for j in range(i+1, size):
            curr = abs(value - (arr[i] + arr[j]))
            if curr < diff:
                diff = curr
                first = arr[i]
                second = arr[j]
    print("closest pair is ::", first, second)

def ClosestPair2(arr, value):
    size = len(arr)
    first, second = 0, 0
    start = 0
    stop = size - 1
    arr.sort()
    diff = sys.maxsize
    while start < stop:
        curr = (value - (arr[start] + arr[stop]))
        if abs(curr) < diff:
                diff = abs(curr)
                first = arr[start]
                second = arr[stop]
        
        if curr == 0:
            break 
        elif curr > 0:
            start += 1
        else:
            stop -= 1
    print("closest pair is ::", first, second)

first = [10, 20, 3, 4, 50, 80]
ClosestPair(first, 70)

first = [10, 20, 3, 4, 50, 80]
ClosestPair2(first, 47)
ClosestPair2(first, 17)
ClosestPair2(first, 30)
ClosestPair2(first, 46)