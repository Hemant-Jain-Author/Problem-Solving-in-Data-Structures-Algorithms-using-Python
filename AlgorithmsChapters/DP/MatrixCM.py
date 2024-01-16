import math
import sys

def matrix_chain_mul_bruteforce(p,  n) :
    return  matrix_chain_mul_bruteforce_util(p, 1, n-1)

def matrix_chain_mul_bruteforce_util(p, i, j) : # Brute force.
    if (i == j) :
        return  0

    min_val = sys.maxsize
    
    # Place parenthesis at different places between first and last matrix,
    # recursively calculate value of multiplications for each parenthesis 
    # placement and return the minimum value.
    for k in range(i, j) :
        count = matrix_chain_mul_bruteforce_util(p, i, k) + matrix_chain_mul_bruteforce_util(p, k+1, j) + p[i-1]*p[k]*p[j]
        min_val = min(min_val, count)

    return  min_val


def matrix_chain_mul_TD(p,  n) :
    dp = [[sys.maxsize] * n for _ in range(n)]
    return  matrix_chain_mul_TDUtil(dp, p, 1, n-1)

#  Function for matrix chain multiplication
def matrix_chain_mul_TDUtil(dp,  p,  i,  j) :
    #  Base Case
    if (i == j) :
        return  0

    if (dp[i][j] != sys.maxsize) :
        return  dp[i][j]

    for k in range(i, j) :
        dp[i][j] = min(dp[i][j],matrix_chain_mul_TDUtil(dp, p, i, k) + matrix_chain_mul_TDUtil(dp, p, k+1, j) + p[i-1]*p[k]*p[j])

    return  dp[i][j]

def matrix_chain_mul_BU(p,  n) :
    dp = [[sys.maxsize] * n for _ in range(n)]

    for i in range(1, n) :
        dp[i][i] = 0    

    for l in range(1, n) : #  l is length of range.
        i = 1
        j = l + 1
        while j < n :
            for k in range(i, j) :
                dp[i][j] = min(dp[i][j], dp[i][k] + p[i-1]*p[k]*p[j] + dp[k+1][j])
            i += 1
            j += 1
    return  dp[0][n - 1]
    
def matrix_chain_mul_BU(p,  n) :
    dp = [[sys.maxsize] * n for _ in range(n)]
    pos = [[sys.maxsize] * n for _ in range(n)]

    for i in range(0, n) :
        dp[i][i] = 0
        pos[i][i] = i    

    for l in range(1, n) : #  l is length of range.
        i = 1
        j = l + 1
        while j < n :
            for k in range(i, j) :
                new_val = dp[i][k] + p[i-1]*p[k]*p[j] + dp[k+1][j]
                if dp[i][j] > new_val :
                    dp[i][j] = new_val
                    pos[i][j] = k
            i += 1
            j += 1
    
    Print_optimal_parenthesis(pos, 1, n-1)
    print()
    return  dp[1][n - 1]
    
def Print_optimal_parenthesis(pos, i, j) :
    if i == j :
        print ("M"+str(pos[i][i]), end=" ")
    else :
        print("(", end=" ")
        Print_optimal_parenthesis(pos, i, pos[i][j])
        Print_optimal_parenthesis(pos, pos[i][j]+1, j)
        print (")", end=" ")


#  Testing Code.
arr = [40, 10, 50, 20, 15]
n = len(arr)
print("Matrix Chain Multiplication is:", matrix_chain_mul_bruteforce(arr, n))
print("Matrix Chain Multiplication is:", matrix_chain_mul_TD(arr, n))
print("Matrix Chain Multiplication is:", matrix_chain_mul_BU(arr, n))

"""
Matrix Chain Multiplication is: 19000
Matrix Chain Multiplication is: 19000
( M1 ( ( M2 M3 ) M4 ) ) 
Matrix Chain Multiplication is: 19000
"""