import math

def max_robbery(house) :
    n = len(house)
    dp = [0] * n
    dp[0] = house[0]
    dp[1] = house[1]
    dp[2] = dp[0] + house[2]
    i = 3
    while (i < n) :
        dp[i] = max(dp[i - 2],dp[i - 3]) + house[i]
        i += 1
    return  max(dp[n - 1],dp[n - 2])


def max_robbery2(house) :
    n = len(house)
    dp = [[0] * (2) for _ in range(n)]
    dp[0][1] = house[0]
    dp[0][0] = 0
    i = 1
    while (i < n) :
        dp[i][1] = max(dp[i - 1][0] + house[i],dp[i - 1][1])
        dp[i][0] = dp[i - 1][1]
        i += 1
    return  max(dp[n - 1][1],dp[n - 1][0])

#  Testing code
arr = [10, 12, 9, 23, 25, 55, 49, 70]
print("Total cash: " + str(max_robbery(arr)))
print("Total cash: " + str(max_robbery2(arr)))

"""
Total cash: 160
Total cash: 160
"""
