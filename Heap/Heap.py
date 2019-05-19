#!/usr/bin/env python

import math

class Heap:
    def __init__(self, array=None):
        self.size = len(array)
        self.arr = [0] #  we do not use 0 index
        self.arr.extend(array)     
        
        #  Build Heap operation over array
        i = math.floor(self.size / 2)
        while i > 0:
            self.proclateDown(i)
            i -= 1

    #  Other Methods.
    def proclateDown(self, position):
        lChild = 2 * position
        rChild = lChild + 1
        small = -1
        if lChild <= self.size:
            small = lChild
        if rChild <= self.size and self.arr[rChild] - self.arr[lChild] < 0:
            small = rChild
        if small != -1 and self.arr[small] - self.arr[position] < 0:
            temp = self.arr[position]
            self.arr[position] = self.arr[small]
            self.arr[small] = temp
            self.proclateDown(small)

    def proclateUp(self, position):
        parent = math.floor(position / 2)
        if parent == 0:
            return
        if self.arr[parent].compareTo(self.arr[position]) < 0:
            temp = self.arr[position]
            self.arr[position] = self.arr[parent]
            self.arr[parent] = temp
            self.proclateUp(parent)

    def add(self, value):
        self.size += 1
        self.arr[self.size] = value
        self.proclateUp(self.size)

    def remove(self):
        if self.size == 0:
            raise RuntimeError("Heap is empty.")
        value = self.arr[1]
        self.arr[1] = self.arr[self.size]
        self.size -= 1
        self.proclateDown(1)
        return value

    def printHeap(self):
        print(self.arr[1:], end=' ')
        print("")

    def isEmpty(self):
        return (self.size == 0)

    def peek(self):
        if self.size() == 0:
            raise RuntimeError("Heap is empty.")        
        return self.arr[1]

    def IsMinHeap(self, arr):
        size = len(arr)
        i = 0
        while(i<= size/2):
            if 2*i + 1 < size:
                if arr[i] > arr[2*i + 1]:
                    return False
            if 2*i + 2 < size:
                if arr[i] > arr[2*i +2]:
                    return False
            i += 1
        return True
    
    
    def IsMaxHeap(self, arr):
        size = len(arr)
        i = 0
        #last element index size - 1
        while(i<= size/2):
            if 2*i + 1 < size:
                if arr[i] < arr[2*i + 1]:
                    return False
            if 2*i + 2 < size:
                if arr[i] < arr[2*i +2]:
                    return False
            i += 1
        return True



def heapSort(array):
    hp = Heap(array)
    i = 0
    while i < len(array):
        array[i] = hp.remove()
        i += 1

# Testing Code
a = [1, 9, 6, 7, 8, 0, 2, 4, 5, 3]
hp = Heap(a)
hp.printHeap()
b = hp.arr[1:]
print(hp.IsMinHeap(b))
print(hp.IsMinHeap(a))
i = 0
while i < len(a):
    print(hp.remove(), end=' ')
    i += 1
print("")
heapSort(a)
print(a, end=' ')
