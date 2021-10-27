import heapq

def optimal_merge_pattern(arr,  size) :
    hp =  []
    for i in range(size) :
        heapq.heappush(hp, arr[i])

    total = 0
    while (len(hp) > 1) :
        value = heapq.heappop(hp)
        value += heapq.heappop(hp)
        heapq.heappush(hp, value)
        total += value
    return  total

arr = [4, 3, 2, 6]
print("Total :", optimal_merge_pattern(arr, len(arr)))

"""
Total : 29
"""