
import sys

def SumPairRestArray(arr):
    size = len(arr)
    arr.sort()
    total = 0
    for i in range(size):
        total += arr[i]
    value = total / 2

    low = 0
    high = size - 1
    while low < high:
        curr = arr[low] + arr[high]
        if curr == value:
            print(arr[low] , arr[high], end=' ')
            return True
        elif curr < value:
            low += 1
        else :
            high -= 1
    return False
    
arr = [1, 2, 4, 8, 16, 15]
print(SumPairRestArray(arr))