
def more(value1,  value2) :
    return  value1 > value2

def shell_sort(arr) :
    n = len(arr)
    gap = n // 2 #  Gap starts with n/2 and half in each iteration.
    while (gap > 0) :
        i = gap  #  Do a gapped insertion sort.
        while (i < n) :
            curr = arr[i]
            #  Shift elements of already sorted list
            #  to find right position for curr value.
            j = i
            while (j >= gap and more(arr[j - gap], curr)) :
                arr[j] = arr[j - gap]    
                j -= gap
            
            #  Put current value in its correct location
            arr[j] = curr
            i += 1
        gap //= 2
    
array = [36, 32, 11, 6, 19, 31, 17, 3]
shell_sort(array)
print(array)

"""
[3, 6, 11, 17, 19, 31, 32, 36]
"""