
def stair_unique_ways_bu(n) :
    if (n <= 2) :
        return  n

    first = 1
    second = 2
    temp = 0
    for _ in range(2, n) :
        temp = first + second
        first = second
        second = temp
    return  temp

def stair_unique_ways_bu2(n) :
    if (n < 2) :
        return  n
    
    ways = [0] * n
    ways[0] = 1
    ways[1] = 2
    for i in range(2, n) :
        ways[i] = ways[i - 1] + ways[i - 2]    

    return  ways[n - 1]

print("Unique way to reach top:: ", stair_unique_ways_bu(4))
print("Unique way to reach top:: ", stair_unique_ways_bu2(4))

"""
Unique way to reach top:: 5
Unique way to reach top:: 5
"""