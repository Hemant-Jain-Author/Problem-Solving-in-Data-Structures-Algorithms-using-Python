#!/usr/bin/env python

class QueueUsingStack(object):
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def add(self, value):
        self.stk1.append(value)

    def remove(self):
        if len(self.stk2) != 0:
            return self.stk2.pop()
        while len(self.stk1) != 0:
            value = self.stk1.pop()
            self.stk2.append(value)
        return self.stk2.pop()

que = QueueUsingStack()
que.add(1)
print que.remove()

que.add(11)
que.add(111)
print que.remove()
que.add(2)
que.add(21)
que.add(211)
print que.remove()
print que.remove()
print que.remove()
print que.remove()
print que.remove()
