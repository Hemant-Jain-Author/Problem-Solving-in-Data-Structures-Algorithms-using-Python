"""
Largest Increasing subsequence
"""
def LIS(arr ):
    maxValue = 0
    size = len(arr)
    lis = [1]*size
    for i in range(size):
        for j in range(i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

        if maxValue < lis[i]:
            maxValue = lis[i]

    return maxValue
 
arr = [10 , 12 , 9 , 23 , 25 , 55 , 49 , 70]
print(LIS(arr))

"""
Longest Bitonic Subsequence
"""
def LBS(arr ):
    maxValue = 0
    size = len(arr)
    lis = [1]*size
    lds = [1]*size
    for i in range(size):
        for j in range(i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    for i in reversed(list(range(size))):
        for j in reversed(list(range(i, size))):
            if arr[j] < arr[i] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    for i in range(size):
        maxValue = max((lis[i] + lds[i] - 1), maxValue)
    return maxValue

arr = [1 , 6 , 3, 11, 1, 9 , 5 , 12 , 3 , 14 , 6 , 17, 3, 19 , 2 , 19]
print(LBS(arr))
