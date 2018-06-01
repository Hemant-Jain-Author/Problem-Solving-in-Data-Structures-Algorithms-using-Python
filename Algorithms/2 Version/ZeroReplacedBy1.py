def ZeroReplace(arr):
    prev = 0
    curr = 0
    size = len(arr)
    index = -1
    maximum = 0
    zeroIndex = -1
    for i in range(size):
        if arr[i] == 1:
            curr += 1
        elif arr[i] == 0:
            if maximum < (prev + curr + 1):
                maximum = prev + curr + 1
                if prev > 0:
                    index = zeroIndex
                else:
                    index = i
                zeroIndex = i
            prev = curr
            curr = 0
    if maximum < (prev + curr + 1):
        maximum = prev + curr + 1
        index = zeroIndex
    print index , maximum
    return maximum

arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
print ZeroReplace(arr)