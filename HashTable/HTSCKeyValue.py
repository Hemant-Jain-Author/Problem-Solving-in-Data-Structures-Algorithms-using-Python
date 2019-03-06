#!/usr/bin/env python
import sys
class HashTableSC(object):
    def __init__(self):
        self.tableSize = 512
        self.listArray = [[] for _ in range(self.tableSize)]

    def ComputeHash(self, key):
        #  division method
        hashValue = key
        return hashValue % self.tableSize

    def resolverFun(self, i):
        return i

    def resolverFun2(self, i):
        return i * i

    def insert(self, key, value):
        index = self.ComputeHash(key)
        self.listArray[index].append((key, value))

    def get(self, key):
        index = self.ComputeHash(key)
        for pair in self.listArray[index]:
            if pair[0] == key:
                return pair[1]
        return sys.maxint
        
    def delete(self, key):
        index = self.ComputeHash(key)
        for pair in self.listArray[index]:
            if pair[0] == key:
                self.listArray[index].remove(pair)
            return True
        return False

    def printHashTable(self):
        for i in range(self.tableSize):
            print("Printing for index value :: " , i , "List of value printing :: ")
            for keyvalue in self.listArray[i]:
                print keyvalue,
            print("")

    def find(self, key):
        index = self.ComputeHash(key)
        for pair in self.listArray[index]:
            if pair[0] == key:
                return True
        return False

ht = HashTableSC()
for i in range(1, 110):
    ht.insert(i,i+1)
print "get 100 :: " , ht.get(100)
print "search 100 :: " , ht.find(100)
print "remove 100 :: " , ht.delete(100)
print "search 100 :: " , ht.find(100)
print "remove 100 :: " , ht.delete(100)