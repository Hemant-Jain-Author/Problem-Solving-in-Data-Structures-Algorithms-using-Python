from collections import deque

a = deque([])
a.append(5)
a.append(4)
a.append(3)
a.append(2)
a.append(1)
a.append(0)
print(a)
print((a.popleft()))
print(a)
