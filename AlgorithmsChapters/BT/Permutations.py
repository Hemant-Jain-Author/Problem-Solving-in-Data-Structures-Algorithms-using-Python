import math

def permutation(arr,  i,  length) :
    if (length == i) :
        print(arr)
        return

    for j in range(i, length) :
        arr[i], arr[j] = arr[j], arr[i] # Swap 
        permutation(arr, i + 1, length)
        arr[i], arr[j] = arr[j], arr[i] # Swap 
    return

def isValid(arr,  n) :
    for j in range(1, n) :
        if (abs(arr[j] - arr[j - 1]) < 2) :
            return  False
    return  True

def permutation2(arr,  i,  length) :
    if (length == i) :
        if (isValid(arr, length)) : 
            print(arr)
        return

    for j in range(i, length) :
        arr[i], arr[j] = arr[j], arr[i] # Swap
        permutation2(arr, i + 1, length)
        arr[i], arr[j] = arr[j], arr[i] # Swap
    return

def isValid2(arr,  i) :
    if (i < 1 or abs(arr[i] - arr[i - 1]) >= 2) :
        return  True
    return  False

def permutation3(arr,  i,  length) :
    if (length == i) :
        print(arr)
        return

    for j in range(i, length) :
        arr[i], arr[j] = arr[j], arr[i] # Swap
        if (isValid2(arr, i)) : 
            permutation3(arr, i + 1, length)
        arr[i], arr[j] = arr[j], arr[i] # Swap
    return
    
# Testing code
arr = list(range(1, 5))
permutation(arr, 0, 4)
print()
permutation2(arr, 0, 4)
print()
permutation3(arr, 0, 4)

"""
[1, 2, 3, 4]
[1, 2, 4, 3] 
.....
[4, 1, 3, 2]
[4, 1, 2, 3]
"""
"""
[2, 4, 1, 3]
[3, 1, 4, 2]

[2, 4, 1, 3]
[3, 1, 4, 2]
"""
