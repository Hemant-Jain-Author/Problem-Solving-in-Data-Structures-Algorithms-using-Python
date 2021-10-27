def selection_sort(arr):
    # reverse array creation
    size = len(arr)
    for i in range(size - 1):
        max_index = 0
        for j in range(1, size - i):
            if arr[j] > arr[max_index]:
                max_index = j
        temp = arr[size - 1 - i]
        arr[size - 1 - i] = arr[max_index]
        arr[max_index] = temp

def selection_sort2(arr):
    # forward array creation
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

array = [4, 5, 3, 2, 6, 7, 1, 8, 9, 10]
selection_sort(array)
print(array)

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""