#!/usr/bin/env python
from collections import deque

class Queue(object):
    
    def __init__(self):
        self.data = deque([])

    def add(self, value):
        self.data.append(value)

    def remove(self):
        value = self.data.popleft()
        return value
    
    def isEmpty(self):
        return (len(self.data) == 0)

    def size(self):
        return len(self.data)
    
    def printQueue(self):
        print self.data


que = Queue()
i = 0
while i < 20:
    que.add(i)
    i += 1
i = 0
while i < 22:
    print que.remove()
    i += 1
