def SubArrayZeroSum(arr):
    size = len(arr)
    maxLength = -1
    start, stop = -1, -1
    hs = {}
    hs[0] = -1
    sum = 0
    for i in range(size):
        sum += arr[i]
        if sum in hs:
            currLength = i - hs[sum]
            if currLength > maxLength :
                maxLength = currLength
                start = hs[sum]
                stop = i
        else :
            hs[sum] = i
    print(start+1, stop, maxLength)

arr = [4, 1, 2, -5, 1, 3, 0, -2, 6]
SubArrayZeroSum(arr)

def SubArrayZeroOneEqual(arr):
    size = len(arr)
    maxLength = -1
    start, stop = -1, -1
    hs = {}
    hs[0] = -1
    sum = 0
    for i in range(size):
        if arr[i] == 1:
            sum += 1
        else :
            sum -= 1
        
        if sum in hs:
            currLength = i - hs[sum]
            if currLength > maxLength :
                maxLength = currLength
                start = hs[sum]
                stop = i
        else :
            hs[sum] = i
    print(start+1, stop, maxLength)

arr = [0, 0, 0, 1, 0, 1, 0]
SubArrayZeroOneEqual(arr)
