def Partition01(arr):
    size = len(arr)
    left = 0
    right = size - 1
    while left < right:
        while arr[left] == 0 :
            left += 1
        while arr[right] == 1 :
            right -= 1
        if left < right :
            arr[left] = 0
            arr[right] = 1

def Partition012(arr):
    size = len(arr)
    left = 0
    right = size - 1
    i = 0
    while i <= right:
        if arr[i] == 0 :
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left += 1
        elif arr[i] == 2 :
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else :
            i += 1

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Partition012(arr)
print(arr)

arr = [0, 1, 0, 1, 1, 1]
Partition01(arr)
print(arr)
