#!/usr/bin/env python
class Stack(object):
    def __init__(self):
        self.data = []     

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return (len(self.data) == 0)

    def push(self, value):
        self.data.append(value)

    def top(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.data[len(self.data) - 1]

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.data.pop()

    def printStack(self):
        print((self.data))


s = Stack()
s.push(1)
s.push(2)
s.push(3) 
s.pop()
s.printStack()
