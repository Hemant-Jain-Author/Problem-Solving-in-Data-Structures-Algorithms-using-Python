class HashTable(object):
    EMPTY_NODE = -1
    LAZY_DELETED = -2
    FILLED_NODE = 0

    def __init__(self, tSize):
        self.table_size = tSize
        self.key_arr = [0] * (tSize + 1)
        self.data_arr = [0] * (tSize + 1)
        self.flag = [self.EMPTY_NODE] * (tSize + 1)

    def compute_hash(self, key):
        return key % self.table_size

    def resolver_fun(self, index):
        return index

    def add(self, key, value):
        hash_value = self.compute_hash(key)
        i = 0
        while i < self.table_size:
            if self.flag[hash_value] == self.EMPTY_NODE or self.flag[hash_value] == self.LAZY_DELETED:
                self.data_arr[hash_value] = value
                self.key_arr[hash_value] = key
                self.flag[hash_value] = self.FILLED_NODE
                return True
            elif self.flag[hash_value] == self.FILLED_NODE and self.key_arr[hash_value] == key:
                self.data_arr[hash_value] = value
                return True

            hash_value += self.resolver_fun(i)
            hash_value %= self.table_size
            i += 1
        return False

    def find(self, key):
        hash_value = self.compute_hash(key)
        i = 0
        while i < self.table_size:
            if self.flag[hash_value] == self.EMPTY_NODE:
                return False
            if self.flag[hash_value] == self.FILLED_NODE and self.key_arr[hash_value] == key:
                return True
            hash_value += self.resolver_fun(i)
            hash_value %= self.table_size
            i += 1
        return False

    def get(self, key):
        hash_value = self.compute_hash(key)
        i = 0
        while i < self.table_size:
            if self.flag[hash_value] == self.EMPTY_NODE:
                return sys.maxsize
            if self.flag[hash_value] == self.FILLED_NODE and self.key_arr[hash_value] == key:
                return self.data_arr[hash_value]
            hash_value += self.resolver_fun(i)
            hash_value %= self.table_size
            i += 1
        return sys.maxsize

    def remove(self, key):
        hash_value = self.compute_hash(key)
        i = 0
        while i < self.table_size:
            if self.flag[hash_value] == self.EMPTY_NODE:
                return False
            if self.flag[hash_value] == self.FILLED_NODE and self.key_arr[hash_value] == key:
                self.flag[hash_value] = self.LAZY_DELETED
                return True
            hash_value += self.resolver_fun(i)
            hash_value %= self.table_size
            i += 1
        return False

    def print(self):
        for i in range(self.table_size) :
            if self.flag[i] == self.FILLED_NODE:
                print("Value for key [" , self.key_arr[i] , "] ::" , self.data_arr[i])

# Testing Code
ht = HashTable(1000)
ht.add(1, 10)
ht.add(2, 20)
ht.add(3, 30)
ht.print()
print("Find key 2 :", ht.find(2))
ht.remove(2)
print("After deleting node with key 2.")
print("Find key 2 :", ht.find(2))

"""
Value at index [ 1 ] :: 10
Value at index [ 2 ] :: 20
Value at index [ 3 ] :: 30
Find key 2 : True
After deleting node with key 2.
Find key 2 : False
"""