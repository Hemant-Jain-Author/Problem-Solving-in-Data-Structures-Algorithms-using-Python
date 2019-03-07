#!/usr/bin/env python
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

    def insert(self, value):
        index = self.ComputeHash(value)
        self.listArray[index].append(value)

    def delete(self, value):
        index = self.ComputeHash(value)
        if value in self.listArray[index]:
            self.listArray[index].remove(value)
            return True
        return False

    def printHashTable(self):
        for i in range(self.tableSize):
            print("Printing for index value :: " , i , "List of value printing :: ")
            for value in self.listArray[i]:
                print(value, end=' ')
            print("")

    def find(self, value):
        index = self.ComputeHash(value)
        if value in self.listArray[index]:
            return True
        return False

ht = HashTableSC()
for i in range(100, 110):
    ht.insert(i)
print("search 100 :: " , ht.find(100))
print("remove 100 :: " , ht.delete(100))
print("search 100 :: " , ht.find(100))
print("remove 100 :: " , ht.delete(100))