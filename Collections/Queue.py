from collections import deque

que = deque([])
que.append(4)
que.append(3)
que.append(2)
que.append(1)
print(que)

print(que.popleft())
print(que)

"""
deque([4, 3, 2, 1])
4
deque([3, 2, 1])
"""