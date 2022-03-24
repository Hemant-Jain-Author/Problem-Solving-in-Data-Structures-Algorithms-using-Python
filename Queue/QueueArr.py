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

# Testing Code
que = Queue()
que.add(1)
que.add(2)
que.add(3)
que.print()
print("Queue length:", que.length())
print("Queue is empty:", que.is_empty())
print("Queue remove:", que.remove())
que.print()

"""
deque([1, 2, 3])
Queue length: 3
Queue is empty: False
Queue remove: 1
deque([2, 3])
"""