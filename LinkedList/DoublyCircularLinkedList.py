#!/usr/bin/env python
class DoublyCircularLinkedList(object):
    class Node(object):
        def __init__(self, v, nxt=None, prv=None):
            self.value = v
            self.next = nxt
            self.prev = prv
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.head == None

    def peekHead(self):
        if self.isEmpty():
            raise RuntimeError("EmptyListException")
        return self.head.value

    def addHead(self, value):
        newNode = self.Node(value, None, None)
        self.count += 1
        if self.head == None:
            self.tail = self.head = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.next = self.head
            newNode.prev = self.head.prev
            self.head.prev = newNode
            newNode.prev.next = newNode
            self.head = newNode


    def addTail(self, value):
        newNode = self.Node(value, None, None)
        self.count += 1
        if self.head == None:
            self.head = self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.next = self.tail.next
            newNode.prev = self.tail
            self.tail.next = newNode
            newNode.next.prev = newNode
            self.tail = newNode


    def removeHead(self):
        if self.head == None:
            raise RuntimeError("EmptyListException")
        self.count -= 1
        value = self.head.value
        if self.head == self.head.next:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        nextNode = self.head.next
        nextNode.prev = self.tail
        self.tail.next = nextNode
        self.head = nextNode
        return value

    def removeTail(self):
        if self.size == 0:
            raise RuntimeError("EmptyListException")
        self.count -= 1
        value = self.tail.value
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
            return value
        prev = self.tail.prev
        prev.next = self.head
        self.head.prev = prev
        self.tail = prev
        return value

    def isPresent(self, key):
        temp = self.head
        if self.head == None:
            return False
        i = 0
        while i < self.size():
            if temp.value == key:
                return True
            temp = temp.next
            i += 1
        return False

    def freeList(self):
        self.head = None
        self.tail = None
        self.count = 0

    
    def printList(self):
        if self.isEmpty():
            return
        temp = self.tail.next
        while temp != self.tail:
            print temp.value ,
            temp = temp.next
        print temp.value,
            
            

ll = DoublyCircularLinkedList()
ll.addHead(1)
ll.addHead(2)
ll.addHead(3)
ll.addHead(1)
ll.addHead(2)
ll.addHead(3)
print ll.size()
ll.printList()
