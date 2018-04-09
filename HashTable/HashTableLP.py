#!/usr/bin/env python
class HashTable(object):
    EMPTY_NODE = -1
    LAZY_DELETED = -2
    FILLED_NODE = 0

    def __init__(self, tSize):
        self.tableSize = tSize
        self.Arr = [0] * (tSize + 1)
        self.Flag = [self.EMPTY_NODE] * (tSize + 1)
        i = 0
        while i <= tSize:
            self.Flag[i] = self.EMPTY_NODE
            i += 1

    def ComputeHash(self, key):
        return key % self.tableSize

    def resolverFun(self, index):
        return index

    def InsertNode(self, value):
        hashValue = self.ComputeHash(value)
        i = 0
        while i < self.tableSize:
            if self.Flag[hashValue] == self.EMPTY_NODE or self.Flag[hashValue] == self.LAZY_DELETED:
                self.Arr[hashValue] = value
                self.Flag[hashValue] = self.FILLED_NODE
                return True
            hashValue += self.resolverFun(i)
            hashValue %= self.tableSize
            i += 1
        return False

    def FindNode(self, value):
        hashValue = self.ComputeHash(value)
        i = 0
        while i < self.tableSize:
            if self.Flag[hashValue] == self.EMPTY_NODE:
                return False
            if self.Flag[hashValue] == self.FILLED_NODE and self.Arr[hashValue] == value:
                return True
            hashValue += self.resolverFun(i)
            hashValue %= self.tableSize
            i += 1
        return False

    def DeleteNode(self, value):
        hashValue = self.ComputeHash(value)
        i = 0
        while i < self.tableSize:
            if self.Flag[hashValue] == self.EMPTY_NODE:
                return False
            if self.Flag[hashValue] == self.FILLED_NODE and self.Arr[hashValue] == value:
                self.Flag[hashValue] = self.LAZY_DELETED
                return True
            hashValue += self.resolverFun(i)
            hashValue %= self.tableSize
            i += 1
        return False

    def Print(self):
        i = 0
        while i < self.tableSize:
            if self.Flag[i] == self.FILLED_NODE:
                print("Node at index [" , i , " ] :: " , self.Arr[i])
            i += 1


ht = HashTable(1000)
ht.InsertNode(89)
ht.InsertNode(18)
ht.InsertNode(49)
ht.Print()
ht.DeleteNode(89)
ht.DeleteNode(18)
ht.DeleteNode(49)
ht.Print()

