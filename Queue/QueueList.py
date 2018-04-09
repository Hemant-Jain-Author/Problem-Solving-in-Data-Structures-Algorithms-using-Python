#!/usr/bin/env python
""" generated source for module Queue """
class Queue(object):
    class Node(object):
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def size(self):
        return self.count
    
    def isEmpty(self):
        return (self.head == None)

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.head.value

    def add(self, value):
        temp = self.Node(value, None)
        self.count += 1
        if self.head == None:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def remove(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        self.count -= 1
        value = self.head.value
        self.head = self.head.next
        return value

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next

 
q = Queue()
i = 1
while i <= 100:
    q.add(i)
    i += 1
i = 1
while i <= 50:
    q.remove()
    i += 1
q.printList()
