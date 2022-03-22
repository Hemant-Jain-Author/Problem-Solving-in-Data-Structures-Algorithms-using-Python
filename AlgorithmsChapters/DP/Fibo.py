def fibonacci(n) :
    if (n < 2) :
        return  n
    return  fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_series(n) :
    for i in range(0, n) :
        print(fibonacci(i), end=" ")

def fibonacci_bu(n) :
    if (n < 2) :
        return n
    
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
      dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

def fibonacci_td_util(n,  dp) :
    if (n < 2) :
        return n

    # Calculate only if not calculated before.
    if (dp[n] == 0) :
        dp[n] = fibonacci_td_util(n - 1, dp) + fibonacci_td_util(n - 2, dp)
    
    return dp[n]

def fibonacci_td(n) :
    dp = [0] * (n+1)
    return fibonacci_td_util(n, dp)




#Testing Code
print("10th fibonacci number :", fibonacci(10)) 
print("10th fibonacci number :", fibonacci_bu(10)) 
print("10th fibonacci number :", fibonacci_td(10)) 
fibonacci_series(5)

"""
10th fibonacci number : 55
10th fibonacci number : 55
10th fibonacci number : 55
0 1 1 2 3 
"""
