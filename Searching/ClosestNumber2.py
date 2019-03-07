"""
Given a sorted array and a number. 
You need to find the element in array which is closest to the given number.
"""
def ClosestNumber(arr, num):
    size = len(arr)
    start = 0
    stop = size - 1
    output = -1
    minDist = 9999
    while start <= stop:
        mid = (start + stop )//2
        if minDist > abs(arr[mid] - num):
            minDist = abs(arr[mid] - num)
            output = arr[mid]
        
        if arr[mid] == num:
            break
        elif arr[mid] > num:
            stop = mid - 1
        else:
            start = mid + 1

    return output


arr = [2, 5, 6, 7, 8, 8, 9]
for i in range(10):
    print(ClosestNumber(arr, i))

