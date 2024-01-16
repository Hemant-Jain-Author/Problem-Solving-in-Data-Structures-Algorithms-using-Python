import math

#  Also known as Activity Selection Weighted.

class Job :
    def __init__(self, s,  f,  v) :
        self.start = s
        self.stop = f
        self.value = v

def max_value_jobs_util(arr,  n) :
    #  Base case
    if (n == 1) :
        return  arr[0].value
    #  Find Value when current job is included
    incl = arr[n - 1].value
    for j in range(n-1, -1, -1) : # n-1 to 0
        if (arr[j].stop <= arr[n - 1].start) :
            incl += max_value_jobs_util(arr, j + 1)
            break
    #  Find Value when current job is excluded
    excl = max_value_jobs_util(arr, n - 1)
    return  max(incl,excl)

def max_value_jobs(s,  f,  v,  n) :
    act = [None] * n
    for i in range(0, n) :
        act[i] = Job(s[i], f[i], v[i])    

    act.sort(key = lambda a : a.stop)  #  sort according to finish time.
    return  max_value_jobs_util(act, n)

def max_value_jobs_td_util(dp,  arr,  n) :
    #  Base case
    if (n == 0) :
        return  0

    if (dp[n - 1] != 0) :
        return  dp[n - 1]
        
    #  Find Value when current job is included
    incl = arr[n - 1].value
    for j in range(n-2, -1, -1) : # n-1 to 0
        if (arr[j].stop <= arr[n - 1].start) :
            incl += max_value_jobs_td_util(dp, arr, j + 1)
            break
    #  Find Value when current job is excluded
    excl = max_value_jobs_td_util(dp, arr, n - 1)
    dp[n - 1] = max(incl,excl)
    return  dp[n - 1]

def max_value_jobs_td(s,  f,  v,  n) :
    act = [None] * n
    for i in range(0, n) :
        act[i] = Job(s[i], f[i], v[i])    
    act.sort(key = lambda a : a.stop) #  sort according to finish time.
    dp = [0] * n
    return  max_value_jobs_td_util(dp, act, n)

def max_value_jobs_bu(s,  f,  v,  n) :
    act = [None] * n
    for i in range(0, n) :
        act[i] = Job(s[i], f[i], v[i])    

    act.sort(key = lambda a : a.stop) #  sort according to finish time.
    dp = [0] * n
    dp[0] = act[0].value
    for i in range(1, n) :
        incl = act[i].value
        for j in range(i - 1, -1, -1) : # i-1 to 0
            if (act[j].stop <= act[i].start) :
                incl += dp[j]
                break
        dp[i] = max(incl,dp[i - 1])
    return  dp[n - 1]

#  Testing code
start = [1, 5, 0, 3, 5, 6, 8]
finish = [2, 6, 5, 4, 9, 7, 9]
value = [2, 2, 4, 3, 10, 2, 8]
n = len(start)
print(max_value_jobs(start, finish, value, n))
print(max_value_jobs_td(start, finish, value, n))
print(max_value_jobs_bu(start, finish, value, n))

"""
17
17
17
"""