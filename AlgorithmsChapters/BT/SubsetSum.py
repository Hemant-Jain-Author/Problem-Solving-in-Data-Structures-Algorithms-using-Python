
def print_subset(flags,  arr,  size) :
    for i in range (0, size) :
        if (flags[i]) : 
            print(str(arr[i]), end =" ")
    print()


def subset_sum(arr,  n,  target) :
    flags = [False] * n
    subset_sum_util(arr, n, flags, 0, 0, target)


def subset_sum_util(arr,  n,  flags,  sum,  curr,  target) :
    if (target == sum) : #  Solution found.
        print_subset(flags, arr, n)
        return

    if (curr >= n or sum > target) : #  constraint check
        return #  Backtracking.
    
    
    flags[curr] = True  #  Current element included.
    subset_sum_util(arr, n, flags, sum + arr[curr], curr + 1, target)
    flags[curr] = False #  Current element excluded.
    subset_sum_util(arr, n, flags, sum, curr + 1, target)

# Testing code
arr = [15, 22, 14, 26, 32, 9, 16, 8]
target = 53
subset_sum(arr, len(arr), target)

"""
15 22 16 
15 14 16 8 
22 14 9 8 
"""
