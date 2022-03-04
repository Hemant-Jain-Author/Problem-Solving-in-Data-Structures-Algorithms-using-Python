import heapq

hp = [6,2,3]                # creates heap from list.
heapq.heapify(hp)
print(hp)

heapq.heappush(hp, 1)       # pushes a new item on the heap
heapq.heappush(hp, 5)
print(hp)

print("Length:", len(hp))
print("Top:", hp[0])                # peek the smallest element of the heap.
print("Pop:", heapq.heappop(hp))    # pops the smallest item from the heap
print(hp)

"""
[2, 6, 3]
[1, 2, 3, 6, 5]
Length: 5
Top: 1
Pop: 1
[2, 5, 3, 6]
"""