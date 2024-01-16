from heapq import heapify
import math

def greater(first, second):
    return first > second # Min Heap
    
def less(first, second):
    return first < second # Max Heap

class Heap:
    def __init__(self, array=None, comp = greater):    
        self.comp = comp
        
        if array == None:
            self.arr = []
            self.size = 0
        else:
            self.arr = array
            self.size = len(array)
            self.heapify()

    def heapify(self):
        #  Build Heap operation over array
        i = self.size // 2
        while i >= 0:
            self.percolate_down(i)
            i -= 1

    def print(self):
        print(self.arr)

    def is_empty(self):
        return (self.size == 0)
    
    def size(self):
        return self.size
    
    def peek(self):
        if self.size() == 0:
            raise RuntimeError("Heap is empty.")        
        return self.arr[0]

    #  Other Methods.
        
    def add(self, value):    
        self.arr.append(value)
        self.size += 1
        self.percolate_up(self.size-1)
            
    def remove(self):
        if self.size == 0:
            raise RuntimeError("Heap is empty.")

        value = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.percolate_down(0)
        return value


    def peek(self):
        if self.size() == 0:
            raise RuntimeError("Heap is empty.")        
        return self.arr[0]

    def percolate_down(self, parent):
        left_child = 2 * parent +  1
        right_child = left_child + 1
        child = -1

        if left_child < self.size:
            child = left_child

        if right_child < self.size and self.comp(self.arr[left_child], self.arr[right_child]):
            child = right_child

        if child != -1 and self.comp(self.arr[parent], self.arr[child]):
            self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
            self.percolate_down(child)

    def percolate_up(self, child):
        parent = (child - 1)// 2

        if parent < 0:
            return

        if self.comp(self.arr[parent], (self.arr[child])):
            self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
            self.percolate_up(parent)


# Testing Code
a = [1, 9, 6, 7, 8, 0, 2, 4, 5, 3]
hp2 = Heap()
for i in range(len(a)) :
    hp2.add(a[i])
hp2.print()

for i in range(len(a)):
    print(hp2.remove(), end=' ')
print()

"""
[0, 3, 1, 5, 4, 6, 2, 9, 7, 8]
0 1 2 3 4 5 6 7 8 9 
"""

a = [1, 9, 6, 7, 8, 0, 2, 4, 5, 3]
hp = Heap(a, greater)
hp.print()
for i in range(len(a)) :
    print(hp.remove(), end=' ')
print("")
"""
[0, 3, 1, 4, 8, 6, 2, 7, 5, 9]
0 1 2 3 4 5 6 7 8 9 
"""


a = [1, 9, 6, 7, 8, 0, 2, 4, 5, 3]
hp = Heap(a, less)
hp.print()
for i in range(len(a)) :
    print(hp.remove(), end=' ')
print("")
"""
[9, 8, 6, 7, 3, 0, 2, 4, 5, 1]
9 8 7 6 5 4 3 2 1 0 
"""

def heap_sort(array, is_inc):
    if is_inc :
        hp = Heap(array, less) # max heap
    else:
        hp = Heap(array, greater) # min heap 
    
    size = len(array)
    for i in range(size):
        array[size - i -1] = hp.remove()

# Testing Code
a = [1, 9, 6, 7, 8, 0, 2, 4, 5, 3]
heap_sort(a, True)
print(a)

heap_sort(a, False)
print(a)

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

"""

def is_min_heap(arr):
    size = len(arr)
    for parent in range(size//2 + 1):
        left_child = parent * 2 + 1
        right_child = parent * 2 + 2
        # heap property check.
        if (((left_child < size) and (arr[parent] > arr[left_child])) or ((right_child < size) and (arr[parent] > arr[right_child]))):
            return False
    return True

# Testing Code
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(is_min_heap(a))

"""
True 
"""

def is_max_heap(arr):
    size = len(arr)
    #last element index size - 1
    for parent in range(size//2 + 1):
        left_child = parent * 2 + 1
        right_child = left_child + 1
        # heap property check.
        if (((left_child < size) and (arr[parent] < arr[left_child])) or ((right_child < size) and (arr[parent] < arr[right_child]))):
            return False
    return True

# Testing Code
b = [8, 7, 6, 5, 4, 3, 2, 1]
print(is_max_heap(b))

"""
True 
"""