def count_sort(arr,  lower_range,  upper_range) :
    size = len(arr)
    rangeval = upper_range - lower_range
    count = [0] * rangeval
    for i in range(size) :
        count[arr[i] - lower_range] += 1
    
    j = 0
    for i in range(rangeval) :
        while (count[i] > 0) :
            arr[j] = i + lower_range
            count[i] -= 1
            j += 1       

array = [23, 24, 22, 21, 26, 25, 27, 28, 21, 21]
count_sort(array, 20, 30)
print(array)

"""
[21, 21, 21, 22, 23, 24, 25, 26, 27, 28]
"""