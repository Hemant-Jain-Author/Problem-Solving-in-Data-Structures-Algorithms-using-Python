import math

#  days are must travel days, costs are cost of tickets.
def vacation_min_cost(days,  costs) :
    n = len(days)
    mx = days[n - 1]
    dp = [0] * (mx + 1)
    j = 0
    for i in range (1, mx+1) :
        if (days[j] == i) :
            #  That days is definitely travelled.
            j += 1
            dp[i] = dp[i - 1] + costs[0]
            dp[i] = min(dp[i], dp[max(0, i - 7)] + costs[1])
            dp[i] = min(dp[i], dp[max(0, i - 30)] + costs[2])
        else :
            dp[i] = dp[i - 1]
    return  dp[mx]

days = [1, 3, 5, 7, 12, 20, 30]
costs = [2, 7, 20]
print("Min cost is:" , vacation_min_cost(days, costs))

"""
Min cost is: 13
"""