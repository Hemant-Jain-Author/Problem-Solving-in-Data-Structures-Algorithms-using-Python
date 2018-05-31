def smallestSubGraterSum(arr, x):
    size = len(arr)
    currSum = 0
    minLen = size + 1
    start = 0
    end = 0
    while end < size:
        if (currSum <= x and end < size):
            currSum += arr[end]
            end += 1
 
        if (currSum > x and start < size):
            if minLen > (end - start):
                minLen = end - start
            currSum -= arr[start]
            start += 1
    return minLen 

arr = [1, 4, 45, 6, 10, 19] 
x = 51
print smallestSubGraterSum(arr, x) 