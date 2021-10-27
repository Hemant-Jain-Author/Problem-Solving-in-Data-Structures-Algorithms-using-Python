import math

def als_fastest_way_bu2(a,  t,  e,  x,  n) :
    f1 = [0] * n
    f2 = [0] * n
    #  Time taken to leave first station.
    f1[0] = e[0] + a[0][0]
    f2[0] = e[1] + a[1][0]

    #  Fill the tables f1[] and f2[] using bottom up approach.
    for i in range(1, n) :
        f1[i] = min(f1[i - 1] + a[0][i],f2[i - 1] + t[1][i - 1] + a[0][i])
        f2[i] = min(f2[i - 1] + a[1][i],f1[i - 1] + t[0][i - 1] + a[1][i])

    #  Consider exit times and return minimum.
    return  min(f1[n - 1] + x[0],f2[n - 1] + x[1])

def als_fastest_way_bu(a,  t,  e,  x,  n) :
    f = [[0] * n for _ in range(2)]

    #  Time taken to leave first station.
    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]

    #  Fill the tables f1[] and f2[] using bottom up approach.
    for i in range(1, n) :
        f[0][i] = min(f[0][i - 1] + a[0][i],f[1][i - 1] + t[1][i - 1] + a[0][i])
        f[1][i] = min(f[1][i - 1] + a[1][i],f[0][i - 1] + t[0][i - 1] + a[1][i])

    #  Consider exit times and return minimum.
    return  min(f[0][n - 1] + x[0],f[1][n - 1] + x[1])
    
def als_fastest_way_td(a,  t,  e,  x,  n) :
    f = [[0] * n for _ in range(2)]

    #  Time taken to leave first station.
    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]

    als_fastest_way_td_util(f, a, t, n - 1)
    return  min(f[0][n - 1] + x[0],f[1][n - 1] + x[1])

def als_fastest_way_td_util(f,  a,  t,  i) :
    if (i == 0) :
        return
    als_fastest_way_td_util(f, a, t, i - 1)
    #  Fill the tables f1[] and f2[] using top-down approach.
    f[0][i] = min(f[0][i - 1] + a[0][i],f[1][i - 1] + t[1][i - 1] + a[0][i])
    f[1][i] = min(f[1][i - 1] + a[1][i],f[0][i - 1] + t[0][i - 1] + a[1][i])

#  Testing code
a = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
t = [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
e = [2, 4]
x = [3, 2]
n = 6
print("ALS fastest way cost:", als_fastest_way_bu2(a, t, e, x, n))
print("ALS fastest way cost:", als_fastest_way_bu(a, t, e, x, n))
print("ALS fastest way cost:", als_fastest_way_td(a, t, e, x, n))

"""
ALS fastest way cost: 38
ALS fastest way cost: 38
ALS fastest way cost: 38
"""