def largest_increasing_subseq(arr) :
    n = len(arr)
    lis = [0] * n
    mx = 0
    #  Populating LIS values in bottom up manner.
    for i in range(n) :
        lis[i] = 1
        #  Initialize LIS values for all indexes as 1.
        for j in range(i) :
            if (arr[j] < arr[i] and lis[i] < lis[j] + 1) : 
                lis[i] = lis[j] + 1
        if (mx < lis[i]) : #  mx LIS values.
            mx = lis[i]
    return  mx

arr = [10, 12, 9, 23, 25, 55, 49, 70]
print("Length of lis is ", str(largest_increasing_subseq(arr)))

"""
Length of lis is 6
"""