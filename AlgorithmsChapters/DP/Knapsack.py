import math

def get_max_cost01(wt,  cost,  capacity) :
    return  get_max_cost01_util(wt, cost, len(wt), capacity)

def get_max_cost01_util(wt,  cost,  n,  capacity) :
    #  Base Case
    if (n == 0 or capacity == 0) :
        return  0
    #  Return the maximum of two cases:
    #  (1) nth item is included
    #  (2) nth item is not included
    first = 0
    if (wt[n - 1] <= capacity) : 
        first = cost[n - 1] + get_max_cost01_util(wt, cost, n - 1, capacity - wt[n - 1])
    second = get_max_cost01_util(wt, cost, n - 1, capacity)
    return  max(first, second)

def get_max_cost01_td(wt,  cost,  capacity) :
    n = len(wt)
    dp = [[0] * (n + 1) for _ in range(capacity + 1)]
    return  get_max_cost01_td_util(dp, wt, cost, n, capacity)

def get_max_cost01_td_util(dp,  wt,  cost,  i,  w) :
    if (w == 0 or i == 0) :
        return  0
    if (dp[w][i] != 0) :
        return  dp[w][i]
    #  Their are two cases:
    #  (1) ith item is included
    #  (2) ith item is not included
    first = 0
    if (wt[i - 1] <= w) : 
        first = get_max_cost01_td_util(dp, wt, cost, i - 1, w - wt[i - 1]) + cost[i - 1]
    second = get_max_cost01_td_util(dp, wt, cost, i - 1, w)
    dp[w][i] = max(first, second)
    return dp[w][i]

def get_max_cost01_bu(wt,  cost,  capacity) :
    n = len(wt)
    dp = [[0] * (n + 1) for _ in range(capacity + 1)]
    #  Build table dp[][] in bottom up approach.
    #  Weights considered against capacity.
    for w in range(1, capacity+1) :
        for i in range (1, n+1) :
            #  Their are two cases:
            #  (1) ith item is included
            #  (2) ith item is not included
            first = 0
            if (wt[i - 1] <= w) : 
                first = dp[w - wt[i - 1]][i - 1] + cost[i - 1]
            second = dp[w][i - 1]
            dp[w][i] = max(first,second)

    # print_items(dp, wt, cost, n, capacity);
    return  dp[capacity][n]

def print_items(dp,  wt,  cost,  n,  capacity) :
    totalCost = dp[capacity][n]
    print("Selected items are:", end =" ")
    for i in range(n-1, -1, -1) :
        if (totalCost != dp[capacity][i - 1]) :
            print("(" + str(wt[i]) + "," + str(cost[i]) + ")", end ="")
            capacity -= wt[i]
            totalCost -= cost[i]

def knapsack01_unbound_bu(wt,  cost,  capacity) :
    n = len(wt)
    dp = [0] * (capacity + 1)
    #  Build table dp[] in bottom up approach.
    #  Weights considered against capacity.
    for w in range(1, capacity+1) :
        for i in range(1, n + 1) :
            #  Their are two cases:
            #  (1) ith item is included 
            #  (2) ith item is not included
            if (wt[i - 1] <= w) : 
                dp[w] = max(dp[w],dp[w - wt[i - 1]] + cost[i - 1])
    
    # print_items(dp, wt, cost, n, capacity);
    return  dp[capacity]

# Testing code.
wt = [10, 40, 20, 30]
cost = [60, 40, 90, 120]
capacity = 50
print("Maximum cost obtained = ", get_max_cost01(wt, cost, capacity))
print("Maximum cost obtained = ", get_max_cost01_bu(wt, cost, capacity))
print("Maximum cost obtained = ", get_max_cost01_td(wt, cost, capacity))

"""
Maximum cost obtained = 210
Maximum cost obtained = 210
Maximum cost obtained = 210
"""