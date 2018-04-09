#!/usr/bin/env python
class Stack(object):
    class Node(object):
        def __init__(self, v, n):
            self.value = v
            self.next = n

    def __init__(self):
        self.head = None
        self.stacksize = 0

    def size(self):
        return self.stacksize

    def isEmpty(self):
        return self.stacksize == 0

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.head.value

    def push(self, value):
        self.head = self.Node(value, self.head)
        self.stacksize += 1

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        value = self.head.value
        self.head = self.head.next
        self.stacksize -= 1
        return value


    def printStack(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next


s = Stack()
s.push(1)
s.push(2)
s.push(3) 
s.pop()
s.printStack()

