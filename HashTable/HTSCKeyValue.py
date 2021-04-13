import sys

class HashTableSC(object):
    def __init__(self):
        self.table_size = 512
        self.adj_list = [[] for _ in range(self.table_size)]

    def compute_hash(self, key):
        #  division method
        return key % self.table_size

    def resolver_fun(self, i):
        return i

    def resolver_fun2(self, i):
        return i * i

    def add(self, key, value):
        index = self.compute_hash(key)
        self.adj_list[index].append((key, value))

    def get(self, key):
        index = self.compute_hash(key)
        for pair in self.adj_list[index]:
            if pair[0] == key:
                return pair[1]
        return sys.maxsize
        
    def remove(self, key):
        index = self.compute_hash(key)
        for pair in self.adj_list[index]:
            if pair[0] == key:
                self.adj_list[index].remove(pair)
            return True
        return False

    def print(self):
        for i in range(self.table_size):
            if len(self.adj_list[i]) != 0:
                for keyvalue in self.adj_list[i]:
                    print("Values of key [" , keyvalue[0],"] ::", keyvalue[1])

    def find(self, key):
        index = self.compute_hash(key)
        for pair in self.adj_list[index]:
            if pair[0] == key:
                return True
        return False

# Testing Code
ht = HashTableSC()
ht.add(1, 10)
ht.add(2, 20)
ht.add(3, 30)
ht.print()
print("Find key 2 :", ht.find(2))
ht.remove(2)
print("After deleting node with key 2.")
print("Find key 2 :", ht.find(2))

"""
Values of key [ 1 ] :: 10
Values of key [ 2 ] :: 20
Values of key [ 3 ] :: 30
Find key 2 : True
After deleting node with key 2.
Find key 2 : False
"""