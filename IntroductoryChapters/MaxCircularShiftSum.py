def maxCircularSum(arr):
    sumAll = 0
    currVal = 0
    n = len(arr)
 
    for i in range(n):
        sumAll += arr[i]
        currVal += (i*arr[i])
 
    maxVal = currVal
    for i in range(1, n, 1):
        currVal = ( currVal + sumAll ) - ( n * arr[n-i] )
        #print currVal
        if currVal > maxVal:
            maxVal = currVal
            
    return maxVal
 
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(maxCircularSum(arr))