import math
import sys

def optimal_bst_cost_util(freq,  i,  j) :
    if (i > j) :
        return  0
    if (j == i) : #  one element in this subarray
        return  freq[i]
    
    minVal = sys.maxsize

    for r in range(i, j+1) :
        minVal = min(minVal,optimal_bst_cost_util(freq, i, r - 1) + optimal_bst_cost_util(freq, r + 1, j))

    return  minVal + sum(freq, i, j)

def optimal_bst_cost(keys,  freq) :
    return  optimal_bst_cost_util(freq, 0, len(freq) - 1)

def optimal_bst_cost_td(keys,  freq) :
    n = len(freq)
    cost = [[sys.maxsize] * n for _ in range(n)]

    for i in range(n) :
        cost[i][i] = freq[i]

    return  optimal_bst_cost_td_util(freq, cost, 0, n - 1)

def optimal_bst_cost_td_util(freq,  cost,  i,  j) :
    if (i > j) :
        return  0

    if (cost[i][j] != sys.maxsize) :
        return  cost[i][j]

    s = sum(freq, i, j)
    for r in range(i, j+1) :
        cost[i][j] = min(cost[i][j],optimal_bst_cost_td_util(freq, cost, i, r - 1) + optimal_bst_cost_td_util(freq, cost, r + 1, j) + s)

    return  cost[i][j]

def sum(freq,  i,  j) :
    s = 0
    for k in range(i, j+1) :
        s += freq[k]    
    return  s

def sum_init(freq,  n) :
    sum = [0] * n
    sum[0] = freq[0]

    for i in range(1, n) :
        sum[i] = sum[i - 1] + freq[i]    
    return  sum

def sum_range(sum,  i,  j) :
    if (i == 0) :
        return  sum[j]
    return  sum[j] - sum[i - 1]

def optimal_bst_cost_bu(keys,  freq) :
    n = len(freq)
    cost = [[sys.maxsize] * n for _ in range(n)]

    for i in range(n) :
        cost[i][i] = freq[i]    

    for l in range(1, n) : #  l is length of range.
        i = 0
        j = l
        for j in range(l, n) :
            sm = sum(freq, i, j)
            for r in range(i, j+1) :
                cost[i][j] = min(cost[i][j],sm + 
                                (cost[i][r - 1] if (r - 1 >= i) else 0) + 
                                (cost[r + 1][j] if (r + 1 <= j) else 0))
            i += 1
    return  cost[0][n - 1]

def optimal_bst_cost_bu2(keys,  freq) :
    n = len(freq)
    cost = [[sys.maxsize] * n for _ in range(n)]
    sumArr = sum_init(freq, n)
    for i in range(0, n) :
        cost[i][i] = freq[i]    

    sm = 0
    for l in range(1, n) : #  l is length of range.
        i = 0
        for j in range(l, n) :
            sm = sum_range(sumArr, i, j)
            r = i
            for r in range(i, j+1) :
                cost[i][j] = min(cost[i][j],sm + 
                                (cost[i][r - 1] if (r - 1 >= i) else 0) + 
                                (cost[r + 1][j] if (r + 1 <= j) else 0))
            i += 1
    return  cost[0][n - 1]

keys = [9, 15, 25]
freq = [30, 10, 40]
print("OBST cost:", optimal_bst_cost(keys, freq))
print("OBST cost:", optimal_bst_cost_td(keys, freq))
print("OBST cost:", optimal_bst_cost_bu(keys, freq))
print("OBST cost:", optimal_bst_cost_bu2(keys, freq))

"""
OBST cost: 130
OBST cost: 130
OBST cost: 130
OBST cost: 130
"""