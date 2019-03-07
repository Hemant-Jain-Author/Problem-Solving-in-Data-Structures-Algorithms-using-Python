"""
Their are N number of petrol pumps. Each petrol pump have 
some limited amount of petrol and they also their distance from each other is provided.
Find if their is a circular tour possible to visit all the petrol pumps.
"""
from collections import deque

def CircularTour(arr, n):
    que = deque([])
    nextPump = 0
    count = 0
    petrol = 0

    while len(que) != n:
        while petrol >= 0 and len(que) != n :
            que.append(nextPump)
            petrol += (arr[nextPump][0] - arr[nextPump][1])
            nextPump = (nextPump + 1) % n
            
        while petrol < 0 and len(que) > 0:
            prevPump = que.popleft()
            petrol -= (arr[prevPump][0] - arr[prevPump][1])
        
        count += 1
        if count == n:
            return -1

    if petrol >= 0:
        return que.popleft()
    else:
        return -1

tour = [[8, 6], 
[1, 4], 
[7, 6]]

print(CircularTour(tour, 3))