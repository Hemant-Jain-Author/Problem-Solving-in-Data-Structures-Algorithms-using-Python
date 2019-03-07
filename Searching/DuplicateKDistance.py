def DuplicateKDistance(arr, k):
    size = len(arr)
    hs = {}
    for i in range(size):
        if arr[i] in hs and i - hs[arr[i]] <= k:
            print(arr[i], hs[arr[i]], i, end=' ')
            return True
        else :
            hs[arr[i]] = i
    return False

arr = [1, 2, 3, 1, 4, 5]
DuplicateKDistance(arr, 3)