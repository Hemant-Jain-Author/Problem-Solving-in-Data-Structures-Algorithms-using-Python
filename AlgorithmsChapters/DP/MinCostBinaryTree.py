import math
import sys

def maxVal(mx,  i,  j) :
    if (mx[i][j] != -sys.maxsize) :
        return  mx[i][j]
    for k in range(i, j) :
        mx[i][j] = max(mx[i][j], maxVal(mx, i, k), maxVal(mx, k + 1, j))
    return  mx[i][j]

def min_cost_binary_tree_td_util(dp,  mx,  i,  j,  arr) :
    if (j <= i) :
        return  0
    
    if (dp[i][j] != sys.maxsize) :
        return  dp[i][j]

    for k in range(i, j) :
        dp[i][j] = min(dp[i][j], 
        min_cost_binary_tree_td_util(dp, mx, i, k, arr) + 
        min_cost_binary_tree_td_util(dp, mx, k + 1, j, arr) + 
        maxVal(mx, i, k) * maxVal(mx, k + 1, j))
    return  dp[i][j]

def min_cost_binary_tree_td(arr) :
    n = len(arr)
    dp = [[sys.maxsize] * n for _ in range(n)]
    mx = [[-sys.maxsize] * n for _ in range(n)]

    for i in range(n) :
        mx[i][i] = arr[i]

    return  min_cost_binary_tree_td_util(dp, mx, 0, n - 1, arr)

def min_cost_binary_tree_bu(arr) :
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    mx = [[0] * n for _ in range(n)]
    for i in range(n) :
        mx[i][i] = arr[i]

    l = 1
    for l in range(1, n) : #  l is length of range.
        i = 0
        j = l
        for j in range(l, n) :
            dp[i][j] = sys.maxsize
            for k in range(i, j) :
                dp[i][j] = min(dp[i][j],dp[i][k] + dp[k + 1][j] + mx[i][k] * mx[k + 1][j])
                mx[i][j] = max(mx[i][k],mx[k + 1][j])
            i += 1
    return  dp[0][n - 1]


arr = [6, 2, 4]
print("Total cost: ", min_cost_binary_tree_td(arr))
print("Total cost: ", min_cost_binary_tree_bu(arr))

"""
Total cost:  32
Total cost:  32
"""