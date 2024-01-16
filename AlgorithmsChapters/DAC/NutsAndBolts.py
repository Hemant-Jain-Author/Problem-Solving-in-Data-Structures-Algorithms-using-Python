def make_pairs(nuts,  bolts) :
    make_pairs_util(nuts, bolts, 0, len(nuts) - 1)
    print("Matched nuts and bolts are : ", nuts, "&",  bolts)

#  Quick sort kind of approach.
def make_pairs_util(nuts,  bolts,  low,  high) :
    if (low < high) :
        #  Choose first element of bolts list as pivot to partition nuts.
        pivot = partition(nuts, low, high, bolts[low])
        #  Using nuts[pivot] as pivot to partition bolts.
        partition(bolts, low, high, nuts[pivot])
        #  Recursively lower and upper half of nuts and bolts are matched.
        make_pairs_util(nuts, bolts, low, pivot - 1)
        make_pairs_util(nuts, bolts, pivot + 1, high)

#  Partition method similar to quick sort algorithm.
def partition(arr,  low,  high,  pivot) :
    i, j = low, low
    while (j < high) :
        if (arr[j] < pivot) :
            arr[i], arr[j] = arr[j], arr[i] # Swap 
            i += 1
        elif(arr[j] == pivot) :
            arr[high], arr[j] = arr[j], arr[high] # Swap
            j -= 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i] # Swap
    return  i

# Testing Code
nuts = [1, 2, 6, 5, 4, 3]
bolts = [6, 4, 5, 1, 3, 2]
make_pairs(nuts, bolts)

"""
Matched nuts and bolts are :  [1, 2, 3, 4, 5, 6] & [1, 2, 3, 4, 5, 6]
"""