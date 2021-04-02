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
                return 0
            if self.flag[hash_value] == self.FILLED_NODE and self.key_arr[hash_value] == key:
                return self.data_arr[hash_value]
            hash_value += self.resolver_fun(i)
            hash_value %= self.table_size
            i += 1
        return 0

    def delete(self, key):
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
        i = 0
        while i < self.table_size:
            if self.flag[i] == self.FILLED_NODE:
                print("Node at index [" , i , " ] :: " , self.data_arr[i])
            i += 1


ht = HashTable(1000)
ht.add(1, 10)
ht.add(2, 20)
ht.add(3, 30)
ht.print()

print("find key 2 : ", ht.find(2))
print("Value at key 2 : ", ht.get(2))

ht.delete(1)
ht.print()

"""
Node at index [ 1  ] ::  10
Node at index [ 2  ] ::  20
Node at index [ 3  ] ::  30

find key 2 :  True
Value at key 2 :  20

Node at index [ 2  ] ::  20
Node at index [ 3  ] ::  30
"""