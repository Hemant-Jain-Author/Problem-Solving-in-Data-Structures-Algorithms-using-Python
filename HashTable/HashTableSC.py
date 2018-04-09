#!/usr/bin/env python
class HashTableSC(object):
    class Node(object):
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    def __init__(self):
        self.tableSize = 512
        self.listArray = [None] * self.tableSize


    def ComputeHash(self, key):
        #  division method
        hashValue = key
        return hashValue % self.tableSize

    def resolverFun(self, i):
        return i

    def resolverFun2(self, i):
        return i * i

    def insert(self, value):
        index = self.ComputeHash(value)
        self.listArray[index] = self.Node(value, self.listArray[index])

    def delete(self, value):
        index = self.ComputeHash(value)
        head = self.listArray[index]
        if head != None and head.value == value:
            self.listArray[index] = head.next
            return True
        while head != None:
            nextNode = head.next
            if nextNode != None and nextNode.value == value:
                head.next = nextNode.next
                return True
            else:
                head = nextNode
        return False

    def printHashTable(self):
        i = 0
        while i < self.tableSize:
            print("Printing for index value :: " , i , "List of value printing :: ")
            head = self.listArray[i]
            while head != None:
                print(head.value, end=' ')
                head = head.next
            print("")
            i += 1

    def find(self, value):
        index = self.ComputeHash(value)
        head = self.listArray[index]
        while head != None:
            if head.value == value:
                return True
            head = head.next
        return False


ht = HashTableSC()
i = 100
while i < 110:
    ht.insert(i)
    i += 1
print("search 100 :: " , ht.find(100))
print("remove 100 :: " , ht.delete(100))
print("search 100 :: " , ht.find(100))
print("remove 100 :: " , ht.delete(100))
