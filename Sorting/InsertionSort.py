def more(value1, value2):
    return value1 > value2

def insertion_sort(arr):
    size = len(arr)
    i = 1
    for i in range(1, size):
        temp = arr[i]
        j = i
        while j > 0 and more(arr[j - 1], temp):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
insertion_sort(array)
print(array)

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
