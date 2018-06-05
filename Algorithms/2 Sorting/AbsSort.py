"""
Sort array according to the absolute difference from the given value.
"""
def more(value1, value2, ref):
    return abs(value1 - ref) > abs(value2 - ref)

def AbsSort(arr, ref):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if more(arr[j], arr[j + 1], ref):
                #  Swapping
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
"""
array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
ref = 5
AbsSort(array, ref)
print(array)
"""

def cmp(value1, value2, A):
    value1 = A*value1*value1
    value2 = A*value2*value2
    return value1 > value2

def EquationSort(arr, A):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if cmp(arr[j], arr[j + 1], A):
                #  Swapping
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
array = [-1, 0, 1, 2, 3, 4]
A = 1
EquationSort(array, A)
print(array)