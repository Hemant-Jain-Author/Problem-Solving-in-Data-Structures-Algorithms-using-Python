def Feasible(Q, k):
    i = 0
    while i < k:
        if Q[k] == Q[i] or abs(Q[i] - Q[k]) == abs(i - k):
            return False
        i += 1
    return True

def NQueens(Q, k, n):
    if k == n:
        print (Q)
        return
    i = 0
    while i < n:
        Q[k] = i
        if Feasible(Q, k):
            NQueens(Q, k + 1, n)
        i += 1


Q = [0] * 8
NQueens(Q, 0, 8)