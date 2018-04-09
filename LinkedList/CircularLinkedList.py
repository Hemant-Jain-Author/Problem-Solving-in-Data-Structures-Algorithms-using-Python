#!/usr/bin/env python
class CircularLinkedList(object):
    class Node(object):
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    def __init__(self):
        self.tail = None
        self.count = 0
    
    def size(self):
        return self.count

    def isEmpty(self):
        return self.tail == None

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("EmptyListException")
        return self.tail.next.value

    def addTail(self, value):
        temp = self.Node(value, None)
        self.count += 1
        if self.tail == None:
            self.tail = temp
            temp.next = temp
        else:
            temp.next = self.tail.next
            self.tail.next = temp
            self.tail = temp
        

    def addHead(self, value):
        temp = self.Node(value, None)
        self.count += 1
        if self.tail == None:
            self.tail = temp
            temp.next = temp
        else:
            temp.next = self.tail.next
            self.tail.next = temp

    def removeHead(self):
        if self.isEmpty():
            raise RuntimeError("EmptyListException")
        self.count -= 1
        value = self.tail.next.value
        if self.tail == self.tail.next:
            self.tail = None
        else:
            self.tail.next = self.tail.next.next
        return value

    def removeNode(self, key):
        if self.isEmpty():
            return False
        self.count -= 1
        curr = self.tail.next
        head = self.tail.next
        if curr.value == key:
            #  head and single node case.
            if curr == curr.next:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next
            return True
        prev = curr
        curr = curr.next
        while curr != head:
            if curr.value == key:
                if curr == self.tail:
                    self.tail = prev
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def copyListReversed(self):
        cl = CircularLinkedList()
        curr = self.tail.next
        head = curr
        if curr != None:
            cl.addHead(curr.value)
            curr = curr.next
        while curr != head:
            cl.addHead(curr.value)
            curr = curr.next
        return cl

    def copyList(self):
        cl = CircularLinkedList()
        curr = self.tail.next
        head = curr
        if curr != None:
            cl.addTail(curr.value)
            curr = curr.next
        while curr != head:
            cl.addTail(curr.value)
            curr = curr.next
        return cl

    def isPresent(self, data):
        temp = self.tail
        i = 0
        while i < self.size():
            if temp.value == data:
                return True
            temp = temp.next
            i += 1
        return False

    def freeList(self):
        self.tail = None
        self.count = 0

    def printList(self):
        if self.isEmpty():
            return
        temp = self.tail.next
        while temp != self.tail:
            print temp.value,
            temp = temp.next
        print temp.value,


ll = CircularLinkedList()
ll.addHead(1)
ll.addHead(2)
ll.addHead(3)
ll.addHead(1)
ll.addHead(2)
ll.addHead(3)
print ll.size()
ll.printList()
print()
ll2 = ll.copyList()
ll2.printList()
print()
ll3 = ll.copyListReversed()
ll3.printList()

