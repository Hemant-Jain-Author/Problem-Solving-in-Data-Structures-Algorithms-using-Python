import heapq

def join_ropes(ropes,  size) :
    ropes.sort(key = lambda x: -x)
    total = 0
    while (size > 1) :
        value = ropes[size - 1] + ropes[size - 2]
        total += value
        index = size - 2
        while (index > 0 and ropes[index - 1] < value) :
            ropes[index] = ropes[index - 1]
            index -= 1
        ropes[index] = value
        size -= 1
    print("Total : ", total)
    return  total

def join_ropes2(ropes,  size) :
    hp =  []
    for i in range(size) :
        heapq.heappush(hp, ropes[i])

    total = 0
    while (len(hp) > 1) :
        value = heapq.heappop(hp)
        value += heapq.heappop(hp)
        heapq.heappush(hp, value)
        total += value
    print("Total : ", total)
    return  total

ropes = [4, 3, 2, 6]
join_ropes(ropes, len(ropes))
rope2 = [4, 3, 2, 6]
join_ropes2(rope2, len(rope2))

"""
Total : 29
Total : 29
"""