import math
import sys

def MatrixChainMulBruteForceUtil(p,  i,  j) :
    if (i == j) :
        return  0
    min = sys.maxsize
    #  place parenthesis at different places between
    #  first and last matrix, recursively calculate
    #  count of multiplications for each parenthesis
    #  placement and return the minimum count
    k = i
    for k in range(i, j) :
        count = MatrixChainMulBruteForceUtil(p, i, k) + MatrixChainMulBruteForceUtil(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        if (count < min) : 
            min = count
    #  Return minimum count
    return  min

def MatrixChainMulBruteForce(p,  n) :
    return  MatrixChainMulBruteForceUtil(p, 1, n-1)

def MatrixChainMulTD(p,  n) :
    dp = [[sys.maxsize] * n for _ in range(n)]
    return  MatrixChainMulTDUtil(dp, p, 1, n - 1)

#  Function for matrix chain multiplication
def MatrixChainMulTDUtil(dp,  p,  i,  j) :
    #  Base Case
    if (i == j) :
        return  0

    if (dp[i][j] != sys.maxsize) :
        return  dp[i][j]

    for k in range(i, j) :
        dp[i][j] = min(dp[i][j],MatrixChainMulTDUtil(dp, p, i, k) + MatrixChainMulTDUtil(dp, p, k + 1, j) + p[i - 1] * p[k] * p[j])

    return  dp[i][j]

def MatrixChainMulBU(p,  n) :
    dp = [[sys.maxsize] * n for _ in range(n)]
    for i in range(1, n) :
        dp[i][i] = 0    

    for l in range(1, n) : #  l is length of range.
        i = 1
        for j in range(l+1, n) :
            for k in range(i, j) :
                dp[i][j] = min(dp[i][j],dp[i][k] + p[i - 1] * p[k] * p[j] + dp[k + 1][j])
            i += 1
    return  dp[1][n - 1]
    
#  Testing Code.
arr = [1, 2, 3, 4]
n = len(arr)
print("Matrix Chain Multiplication is: ", MatrixChainMulBruteForce(arr, n))
print("Matrix Chain Multiplication is: ", MatrixChainMulTD(arr, n))
print("Matrix Chain Multiplication is: ", MatrixChainMulBU(arr, n))

"""
Matrix Chain Multiplication is:  18
Matrix Chain Multiplication is:  18
Matrix Chain Multiplication is:  18
"""