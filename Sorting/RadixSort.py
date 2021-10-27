def get_max(arr,  n) :
    mx = arr[0]
    for i in range(1, n) :
        mx = max(mx, arr[i])    
    return  mx

def count_sort(arr,  n,  dividend) :
    temp = arr.copy()
    count = [0] * 10

    #  Store count of occurrences in count array.
    #  (number / dividend) % 10 is used to find the working digit.
    for i in range(n) :
        count[(int(temp[i] / dividend)) % 10] += 1    

    #  Change count[i] so that count[i] contains 
    #  number of elements till index i in output.
    for i in range(1, 10) :
        count[i] += count[i - 1]    
    
    #  Copy content to input arr.
    for i in range(n-1, -1, -1) :
        arr[count[(int(temp[i] / dividend)) % 10] - 1] = temp[i]
        count[(int(temp[i] / dividend)) % 10] -= 1

def radix_sort(arr) :
    n = len(arr)
    m = get_max(arr, n)
    #  Counting sort for every digit.
    #  The dividend passed is used to calculate current working digit.
    div = 1
    while ((m // div) > 0) :
        count_sort(arr, n, div)
        div *= 10

# Testing Code
array = [100, 49, 65, 91, 702, 29, 4, 55]
radix_sort(array)
print(array)

"""
[4, 29, 49, 55, 65, 91, 100, 702]
"""