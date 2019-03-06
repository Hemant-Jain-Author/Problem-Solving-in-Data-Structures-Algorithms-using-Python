def RangePartition(arr, lower, higher):
    size = len(arr)
    left = 0
    right = size - 1
    i = 0
    while i <= right:
        print arr , i
        if arr[i] < lower :
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1
        elif arr[i] > higher :
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else :
            i += 1

arr = [1,21,2,20,3,19,4,18,5,17,6,16,7,15,8,14,9,13,10,12,11]
RangePartition(arr, 8, 12)
print arr


