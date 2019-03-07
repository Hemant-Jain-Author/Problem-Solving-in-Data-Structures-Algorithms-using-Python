
def RotationMax(arr):
    size = len(arr)
    return RotationMaxUtil(arr, 0, size - 1)

def RotationMaxUtil(arr, start, end):
    if end <= start:
        return arr[start]

    mid = (start + end) // 2
    if arr[mid] > arr[mid+1]:
        return arr[mid]

    if arr[start] <= arr[mid]: #increasing part.
        return RotationMaxUtil(arr, mid+1, end)
    else:
        return RotationMaxUtil(arr, start, mid-1)


def FindRotationMax(arr):
    size = len(arr)
    return FindRotationMaxUtil(arr, 0, size - 1)

def FindRotationMaxUtil(arr, start, end):
    # single element case.
    if end <= start:
        return start

    mid = (start + end) // 2
    if arr[mid] > arr[mid+1]:
        return mid

    if arr[start] <= arr[mid]: #increasing part.
        return FindRotationMaxUtil(arr, mid+1, end)
    else:
        return FindRotationMaxUtil(arr, start, mid-1)

def CountRotation(arr):
    size = len(arr)
    maxIndex =  FindRotationMaxUtil(arr, 0, size - 1)
    rotations = (maxIndex + 1) % size
    return rotations

def main16():
    first = [34, 56, 1, 1, 5, 6, 6, 6, 6, 6, 6, 7, 8, 10, 13, 20, 30 ]
    second = [1, 5, 6,6,6,6,6,6,7,8,10, 13, 20, 30 ]
    # first = [10, 150, 6,67,61,16,86,6,67,78,150, -3, 28, 143 ]

    print(RotationMax(first))
    print(FindRotationMax(first))
    print(CountRotation(first))
    print(RotationMax(second))
    print(FindRotationMax(second))
    print(CountRotation(second))

main16()