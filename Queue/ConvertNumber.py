import sys
from collections import deque

def convertXY(src, dst):
    que = deque([])
    visited = {}
    que.append((src, 0))
    while len(que) != 0:
        node = que.popleft()
        visited[node[0]] = 1
        value = node[0]
        steps = node[1]
        if value == dst:
            return steps
        if value < dst and (value*2) not in visited:
            que.append((value*2, steps+1))
        if value > 0 and (value - 1) not in visited:
            que.append((value-1, steps+1))
    return -1
    
for i in range(20):
    print("3 to ", i ," : ", convertXY(3, i))