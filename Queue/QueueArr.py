from collections import deque

class Queue(object):
    def __init__(self):
        self.data = deque([])

    def add(self, value):
        self.data.append(value)

    def remove(self):
        value = self.data.popleft()
        return value
    
    def is_empty(self):
        return (len(self.data) == 0)

    def length(self):
        return len(self.data)
    
    def print(self):
        print(self.data)


que = Queue()
que.add(1)
que.add(2)
que.add(3)
print(que.length())
print(que.is_empty())
print(que.remove())
print(que.remove())
print(que.remove())
print(que.length())
print(que.is_empty())
"""
3
False
1
2
3
0
True
"""