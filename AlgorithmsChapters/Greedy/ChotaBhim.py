import heapq
import math

def chota_bhim_max_drink(cups, attempts) :
    size = len(cups)
    cups.sort(key = lambda a : -a) # sort decreasing order.
    total = 0
    for _ in range(attempts): 
        total += cups[0]
        cups[0] = cups[0] // 2
        index = 0
        temp = cups[0]
        while (index < size - 1 and temp < cups[index + 1]) :
            cups[index] = cups[index + 1]
            index += 1
        cups[index] = temp

    print("Total : " + str(total))
    return  total

def max_heap_push(hp, value):
    heapq.heappush(hp, -1 * value)

def max_heap_pop(hp):
    return -1 * heapq.heappop(hp)

def chota_bhim_max_drink2(cups, attempts) :
    size = len(cups)
    hp = []
    for i in range(size) :
        max_heap_push(hp, cups[i])

    total = 0
    for _ in range(attempts):
        value = max_heap_pop(hp)
        total += value
        value = value // 2
        max_heap_push(hp, value)
    print("Total : " + str(total))
    return  total


cups = [20, 10, 70, 40, 20]
chota_bhim_max_drink(cups, 5)
cups2 = [20, 10, 70, 40, 20]
chota_bhim_max_drink2(cups2, 5)

"""
Total : 76
Total : 76
"""