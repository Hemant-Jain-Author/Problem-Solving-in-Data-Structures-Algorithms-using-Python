def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def WaveArray(arr):
    size = len(arr)
    arr.sort()
    # Swap adjacent elements in array
    for i in range(0, size - 1, 2):
        swap(arr, i, i+1)


def WaveArray2(arr):
    size = len(arr)
    
    # Odd elements are lesser then even elements.
    for i in range(1, size , 2):
        if (i - 1) >= 0 and arr[i] > arr[i - 1]:
            swap(arr, i, i-1)
        if (i + 1) < size and arr[i] > arr[i + 1]:
            swap(arr, i, i+1)

arr = [8, 1, 2, 3, 4, 5, 6, 4, 2]
WaveArray2(arr)
print(arr)