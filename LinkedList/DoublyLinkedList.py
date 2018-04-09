#!/usr/bin/env python
class DoublyLinkedList(object):
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
        return self.size() == 0

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("EmptyListException")
        return self.head.value

    def addHead(self, value):
        self.count += 1
        if self.head == None:
            self.tail = self.head = self.Node(value, None, None)
        else:
            newNode = self.Node(value, self.head, None)
            self.head.prev = newNode
            self.head = newNode


    def addTail(self, value):
        newNode = self.Node(value, None, None)
        self.count += 1
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def removeHead(self):
        if self.isEmpty():
            raise RuntimeError("EmptyListException")
        self.count -= 1
        value = self.head.value
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    def removeNode(self, key):
        curr = self.head
        if curr == None:
            return False # empty list
        
        if curr.value == key:
            # head is the node with value key.
            self.head = self.head.next
            if self.head != None:
                self.head = None
            else:
                self.tail = None
            #  only one element in list.
            self.count -= 1
            return True
        while curr.next != None:
            if curr.next.value == key:
                curr.next = curr.next.next
                if curr.next == None:
                    self.tail = curr
                else:
                    curr.next = curr
                self.count -= 1
                return True
            curr = curr.next
        return False

    def isPresent(self, key):
        temp = self.head
        while temp != None:
            if temp.value == key:
                return True
            temp = temp.next
        return False

    def freeList(self):
        self.head = None
        self.tail = None
        self.count = 0

    def printList(self):
        temp = self.head
        while temp != None:
            print temp.value,
            temp = temp.next
        print ""

    # SORTED INSERT DECREASING
    def sortedInsert(self, value):
        temp = self.Node(value)
        curr = self.head
        self.count += 1
        if curr == None:
            # first element
            self.head = temp
            self.tail = temp
        if self.head.value <= value: # at the begining  
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        while curr.next != None and curr.next.value > value: # treversal
            curr = curr.next
        
        if curr.next == None: # at the end
            self.tail = temp
            temp.prev = curr
            curr.next = temp
        else:                 # all other
            temp.next = curr.next
            temp.prev = curr
            curr.next = temp
            temp.next.prev = temp


    # Reverse a doubly linked List iteratively
    def reverseList(self):
        curr = self.head
        tempNode = self.Node()
        while curr != None:
            tempNode = curr.next
            curr.next = curr.prev
            curr.prev = tempNode
            if curr.prev == None:
                self.tail = self.head
                self.head = curr
                return
            curr = curr.prev
        return

    #   Remove Duplicate 
    def removeDuplicate(self):
        curr = self.head
        deleteMe = self.Node()
        while curr != None:
            if (curr.next != None) and curr.value == curr.next.value:
                deleteMe = curr.next
                curr.next = deleteMe.next
                curr.next.prev = curr
                if deleteMe == self.tail:
                    self.tail = curr
            else:
                curr = curr.next

    def copyListReversed(self):
        dll = DoublyLinkedList()
        curr = self.head
        while curr != None:
            dll.addHead(curr.value)
            curr = curr.next
        return dll

    def copyList(self):
        dll = DoublyLinkedList()
        curr = self.head
        while curr != None:
            dll.addTail(curr.value)
            curr = curr.next
        return dll



ll = DoublyLinkedList()
#=======================================================================
# ll.addHead(1)
# ll.addHead(2)
# ll.addHead(3)
# ll.addHead(4)
# ll.addHead(5)
# ll.addHead(6)
# ll.printList()
# ll.removeHead()
# ll.removeHead()
# ll.removeHead()
# ll.removeHead()
# ll.removeHead()
# ll.printList()
# ll.freeList()
# ll.printList()
#=======================================================================
ll.addHead(11)
ll.addHead(21)
ll.addHead(31)
ll.addHead(41)
ll.addHead(51)
ll.addHead(61)
ll.printList()
ll2 = ll.copyList()
ll2.printList()
ll3 = ll.copyListReversed()
ll3.printList()
        

