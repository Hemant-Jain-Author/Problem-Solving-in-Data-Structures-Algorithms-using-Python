import math

def largest_bitonic_subseq(self, arr) :
    n = len(arr)
    lis = [1] * n #  Initialize LIS values for all indexes as 1.
    lds = [1] * n #  Initialize LDS values for all indexes as 1.
    #  Populating LIS values in bottom up manner.
    for i in range(0, n) :
        for j in range(0, i) :
            if (arr[j] < arr[i] and lis[i] < lis[j] + 1) : 
                lis[i] = lis[j] + 1

    #  Populating LDS values in bottom up manner.
    for i in range(n-1, 0, -1) :
        for j in range(n-1, i, -1) :
            if (arr[j] < arr[i] and lds[i] < lds[j] + 1) : 
                lds[i] = lds[j] + 1
    mx = 0
    for i in range(0, n) :
        mx = max(mx, lis[i] + lds[i] - 1)
    return  mx

arr = [1, 6, 3, 11, 1, 9, 5, 12, 3, 14, 6, 17, 3, 19, 2, 19]
print("Length of largest bitonic subseq is " + str(largest_bitonic_subseq(arr)))

"""
Length of lis is 8
"""
