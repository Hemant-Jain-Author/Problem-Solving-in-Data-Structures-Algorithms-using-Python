import math
def min_stair_cost(cost): 
    n = len(a)
    #  base case
    if (n == 1) :
        return  cost[0]
    
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    i = 2
    for i in range(2, n) :
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    return  min(dp[n - 2], dp[n - 1])

a = [1, 5, 6, 3, 4, 7, 9, 1, 2, 11]
print(min_stair_cost(a))

"""
18
"""