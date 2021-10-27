import math

def min_cost(cost,  m,  n) :
    if (m == 0 and n == 0) :
        return  0
    if (m == 0) :
        return  cost[0][n - 1] + min_cost(cost, 0, n - 1)
    if (n == 0) :
        return  cost[m - 1][0] + min_cost(cost, m - 1, 0)
    return  cost[m - 1][n - 1] + min(min_cost(cost, m - 1, n - 1), 
                                    min_cost(cost, m - 1, n), 
                                    min_cost(cost, m, n - 1))

def min_cost_bu(cost,  m,  n) :
    tc = [[0] * n for _ in range(m)]
    tc[0][0] = cost[0][0]
    #  Initialize first column.
    for i in range(1, m) :
        tc[i][0] = tc[i - 1][0] + cost[i][0]

    #  Initialize first row.
    for j in range(1, n) :
        tc[0][j] = tc[0][j - 1] + cost[0][j]

    for i in range(1, m) :
        for j in range(1, n) :
            tc[i][j] = cost[i][j] + min(tc[i - 1][j - 1], tc[i - 1][j], tc[i][j - 1])

    return  tc[m - 1][n - 1]

#  Testing code
cost = [[1, 3, 4], [4, 7, 5], [1, 5, 3]]
print(min_cost(cost, 3, 3))
print(min_cost_bu(cost, 3, 3))

"""
11
11
"""