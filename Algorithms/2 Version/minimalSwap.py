"""
Minimum swaps required to bring all elements less than given value together at the start of array. 

Use quick sort kind of technique by taking two index from both end 
and try to use the given value as key.

Count the number of swaps that is answer.
"""

def minSwaps(arr, val):
    swapCount = 0
    first = 0
    second = len(arr) - 1
    while first < second:
        if arr[first] <= val:
            first += 1
        elif arr[second] > val:
            second -= 1
        else:
            arr[first], arr[second] = arr[second], arr[first]
            swapCount += 1
    return swapCount

def main():
    arr = [2, 1, 5, 6, 3]
    k = 3
    print minSwaps(arr, k)
    
    arr1 = [2, 7, 9, 5, 8, 7, 4]
    k = 5
    print minSwaps(arr1, k)

"""
Now in the above problem we dont want all the elements in start of array.
We want to find a window for which minimum number of swaps are requered to 
bring all the elements less then the than given value together.
"""
def minSwapsWin(arr, val):
    count = 0
    size = len(arr)
    for i in range(size):
        if arr[i] <= val:
            count += 1

    currCount = 0
    for i in range(count):
        if arr[i] <= val:
            currCount += 1
    
    maxCount = currCount
    first = 0
    while first < size - count:
        if arr[first] < val:
            currCount -= 1
        
        if arr[first + count] < val:
            currCount += 1

        if currCount > maxCount:
            maxCount = currCount
        first += 1
    return count - maxCount

def main2():
    arr = [2, 1, 5, 6, 3]
    k = 3
    print minSwapsWin(arr, k)
    
    arr1 = [2, 7, 9, 5, 8, 7, 4]
    k = 5
    print minSwapsWin(arr1, k)

main2()

"""
find product of first k elements.
Use quick select to find kth element the elements which are at the left of 
kth index will be the elements less then it.
"""