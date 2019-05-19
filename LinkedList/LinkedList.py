#!/usr/bin/env python
class LinkedList(object):
    # Node class representing elements of linked list.
    class Node:
        def __init__(self, v, n=None):
            self.value = v
            self.next = n
            
    # Constructor of linked list.
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("EmptyListException")
        return self.head.value

    def addHead(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1

    def addTail(self, value):
        newNode = self.Node(value, None)
        curr = self.head
        if self.head == None:
            self.head = newNode
        while curr.next != None:
            curr = curr.next
        curr.next = newNode
        self.size += 1

    def removeHead(self):
        if self.isEmpty():
            raise RuntimeError("EmptyListException")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def isPresent(self, data):
        temp = self.head
        while temp != None:
            if temp.value == data:
                return True
            temp = temp.next
        return False

    def deleteNode(self, delValue):
        temp = self.head
        if self.isEmpty():
            return False
        if delValue == self.head.value:
            self.head = self.head.next
            self.size -= 1
            return True
        while temp.next != None:
            if temp.next.value == delValue:
                temp.next = temp.next.next
                self.size -= 1
                return True
            temp = temp.next
        return False

    def deleteNodes(self, delValue):
        currNode = self.head
        while currNode != None and currNode.value == delValue:
            # first node 
            self.head = currNode.next
            currNode = self.head
            self.size -= 1
        while currNode != None:
            nextNode = currNode.next
            if nextNode != None and nextNode.value == delValue:
                currNode.next = nextNode.next
                self.size -= 1
            else:
                currNode = nextNode

    def reverseRecurseUtil(self, currentNode, nextNode):
        if currentNode == None:
            return None
        if currentNode.next == None:
            currentNode.next = nextNode
            return currentNode
        ret = self.reverseRecurseUtil(currentNode.next, currentNode)
        currentNode.next = nextNode
        return ret

    def reverseRecurse(self):
        self.head = self.reverseRecurseUtil(self.head, None)

    def reverse(self):
        curr = self.head
        prev = None
        while curr != None:
            nextval = curr.next
            curr.next = prev
            prev = curr
            curr = nextval
        self.head = prev

    def CopyListReversed(self):
        tempNode = None
        curr = self.head
        while curr != None:
            tempNode2 = self.Node(curr.value, tempNode)
            curr = curr.next
            tempNode = tempNode2
        ll2 = LinkedList()
        ll2.head = tempNode
        return ll2

    def copyList(self):
        curr = self.head
        if curr == None:
            return None
        tailNode = headNode = self.Node(curr.value, None)
        curr = curr.next
        while curr != None:
            tempNode = self.Node(curr.value, None)
            tailNode.next = tempNode
            tailNode = tempNode
            curr = curr.next
        ll2 = LinkedList()
        ll2.head = headNode
        return ll2


    def compareList(self, ll):
        return self.compareListUtil(self.head, ll.head)

    def compareListUtil(self, head1, head2):
        if head1 == None and head2 == None:
            return True
        elif (head1 == None) or (head2 == None) or (head1.value != head2.value):
            return False
        else:
            return self.compareListUtil(head1.next, head2.next)

    def  compareList2(self, ll2):
        head1 = self.head
        head2 = ll2.head

        while head1 != None and head2 != None:
            if head1.value != head2.value:
                return false;
            head1 = head1.next
            head2 = head2.next

        if head1 == None and head2 == None:
            return True
        return False

    def findLength(self):
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next
        return count

    def nthNodeFromBegining(self, index):
        if index > self.length() or index < 1:
            raise RuntimeError("IndexOutOfRange")
        count = 1
        curr = self.head
        while curr != None and count < index:
            count += 1
            curr = curr.next
        return curr.value


    def nthNodeFromEnd(self, index):
        if self.size != 0 and self.size < index:
            raise RuntimeError("IndexOutOfRange")
        startIndex = self.size - index + 1
        return self.nthNodeFromBegining(startIndex)

    def nthNodeFromEnd2(self, index):
        count = 1
        forward = self.head
        curr = self.head
        while forward != None and count <= index:
            count += 1
            forward = forward.next
        if forward == None:
            raise RuntimeError("IndexOutOfRange")
        while forward != None:
            forward = forward.next
            curr = curr.next
        return curr.value

    def findIntersection(self, head, head2):
        l1 = 0
        l2 = 0
        tempHead = head
        tempHead2 = head2
        while tempHead != None:
            l1 += 1
            tempHead = tempHead.next
        while tempHead2 != None:
            l2 += 1
            tempHead2 = tempHead2.next
        diff = int()
        if l1 < 12:
            temp = head
            head = head2
            head2 = temp
            diff = l2 - l1
        else:
            diff = l1 - l2
        while diff > 0:
            head = head.next
            diff -= 1
        while head != head2:
            head = head.next
            head2 = head2.next
        return head

    def freeList(self):
        self.head = None
        self.size = 0

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next
        print("")

    def sortedInsert(self, value):
        newNode = self.Node(value, None)
        curr = self.head
        if curr == None or curr.value > value:
            newNode.next = self.head
            self.head = newNode
            return
        while curr.next != None and curr.next.value < value:
            curr = curr.next
        newNode.next = curr.next
        curr.next = newNode

    def removeDuplicate(self):
        curr = self.head
        while curr != None:
            if curr.next != None and curr.value == curr.next.value:
                curr.next = curr.next.next
            else:
                curr = curr.next

    def makeLoop(self):
        temp = self.head
        while temp != None:
            if temp.next == None:
                temp.next = self.head
                return
            temp = temp.next

    def loopDetect(self):
        slowPtr = fastPtr = self.head
        while fastPtr.next != None and fastPtr.next.next != None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                print("loop found")
                return True
        print("loop not found")
        return False

    def reverseListLoopDetect(self):
        tempHead = self.head
        self.reverse()
        if tempHead == self.head:
            self.reverse()
            print("loop found")
            return True
        else:
            self.reverse()
            print("loop not found")
            return False

    def loopTypeDetect(self):
        slowPtr = fastPtr = self.head
        while fastPtr.next != None and fastPtr.next.next != None:
            if self.head == fastPtr.next or self.head == fastPtr.next.next:
                print("circular list loop found")
                return 2
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                print("loop found")
                return 1
        print("loop not found")
        return 0

    def loopPointDetect(self):
        slowPtr = fastPtr = self.head
        while fastPtr.next != None and fastPtr.next.next != None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                return slowPtr
        return None

    def removeLoop(self):
        loopPoint = self.loopPointDetect()
        if loopPoint == None:
            raise RuntimeError("LoopNotFound")
        firstPtr = self.head
        if loopPoint == self.head:
            while firstPtr.next != self.head:
                firstPtr = firstPtr.next;
            firstPtr.next = None
            return
        secondPtr = loopPoint
        while firstPtr.next != secondPtr.next:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next
        secondPtr.next = None



ll = LinkedList()
ll.addHead(1)
ll.addHead(2)
ll.addHead(3)
ll.addHead(4)
ll.printList()

print(ll.compareList2(ll))
# ll.sortedInsert(1)
# ll.sortedInsert(2)
# ll.sortedInsert(3)
# ll.sortedInsert(5)
# ll.sortedInsert(0)
# ll.printList()
# ll.makeLoop()
# print(ll.loopDetect())
# print(ll.loopTypeDetect())
# print(ll.loopPointDetect().value)
# print(ll.reverseListLoopDetect())
# print(ll.removeLoop())

#=======================================================================
# print ll.isEmpty()
#=======================================================================
#=======================================================================
# print ll.isEmpty()
# print ll.peek()
# print ll.removeHead()
# ll.printList()
#=======================================================================
#=======================================================================
# print ll.isPresent(5)
# print ll.isPresent(2)
# ll.removeDuplicate()
# print ll.isEmpty()
# ll.deleteNodes(3)
#=======================================================================
#=======================================================================
# ll.reverse()
# ll.printList()
# ll.reverseRecurse()
# ll.printList()
#=======================================================================
#=======================================================================
# ll3 = ll.CopyListReversed()
# ll3.printList()
#  
# ll2 = ll.copyList()
# ll2.printList()
# print ll.findLength()
#=======================================================================
#=======================================================================
# print ll.nthNodeFromBegining(2)
# print ll.nthNodeFromEnd(2)
# print ll.nthNodeFromEnd2(2)
#=======================================================================

      
