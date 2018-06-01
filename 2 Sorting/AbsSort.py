"""
Sort array according to the absolute difference from the given value.
"""
def more(value1, value2, ref):
    return abs(value1 - ref) > abs(value2 - ref)

def AbsSort(arr, ref):
    size = len(arr)
    i = 0
    while i < (size - 1):
        j = 0
        while j < size - i - 1:
            if more(arr[j], arr[j + 1], ref):
                #  Swapping 
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
        i += 1


array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
ref = 5
AbsSort(array, ref)
print(array)
