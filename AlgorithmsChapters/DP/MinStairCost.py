import math

def min_stair_cost(costs): 
    n = len(costs)
    #  base case
    if (n == 1) :
        return  costs[0]
    
    dp = [0] * n
    dp[0] = costs[0]
    dp[1] = costs[1]

    for i in range(2, n) :
        dp[i] = min(dp[i - 1], dp[i - 2]) + costs[i]

    return  min(dp[n - 2], dp[n - 1])

# Testing Code
costs = [1, 5, 6, 3, 4, 7, 9, 1, 2, 11]
print("Min stair cost :", min_stair_cost(costs))

"""
Min stair cost : 18
"""