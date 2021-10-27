import math

def feasible(Q,  k) :
    for i in range(k) :
        if (Q[k] == Q[i] or abs(Q[i] - Q[k]) == abs(i - k)) :
            return  False
    return  True

def nqueens(Q,  k,  n) :
    if (k == n) :
        print(Q)
        return
    for i in range(n) :
        Q[k] = i
        if (feasible(Q, k)) :
            nqueens(Q, k + 1, n)

# Testing Code.
Q = [0] * (8)
nqueens(Q, 0, 8)

"""
[0, 4, 7, 5, 2, 6, 1, 3]
[0, 5, 7, 2, 6, 3, 1, 4]
.
.
.
[7, 2, 0, 5, 1, 4, 6, 3]
[7, 3, 0, 2, 5, 1, 6, 4]
"""