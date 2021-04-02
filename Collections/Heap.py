import heapq

hp = [3,1,2]                # creates heap from list.
heapq.heapify(hp)
print(hp)

heapq.heappush(hp, 6)       # pushes a new item on the heap
heapq.heappush(hp, 4)
heapq.heappush(hp, 5)
heapq.heappush(hp, 7)
print(hp)

print(len(hp))
print(hp[0])                # peek the smallest element of the heap.
print(heapq.heappop(hp))    # pops the smallest item from the heap
print(hp)

"""
[1, 3, 2]
[1, 3, 2, 6, 4, 5, 7]
7
1
1
[2, 3, 5, 6, 4, 7]
"""