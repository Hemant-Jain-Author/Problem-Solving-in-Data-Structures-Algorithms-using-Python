#!/usr/bin/env python
import heapq

class MedianHeap(object):
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def MinHeapInsert(self, value):
        heapq.heappush(self.minHeap, value)
        
    def MaxHeapInsert(self, value):
        heapq.heappush(self.maxHeap, -1 * value)
        
    def MaxHeapPeek(self):
        return -1 * self.maxHeap[0]
    
    def MinHeapPeek(self):
        return self.minHeap[0]
        
    def MinHeapRemove(self):
        return heapq.heappop(self.minHeap)
    
    def MaxHeapRemove(self):
        return -1 * heapq.heappop(self.maxHeap)

    # Other Methods.
    def insert(self, value):
        if len(self.maxHeap) == 0 or self.MaxHeapPeek() >= value:
            self.MaxHeapInsert(value)
        else:
            self.MinHeapInsert(value)
        # size balancing
        if len(self.maxHeap) > len(self.minHeap) + 1:
            value = self.MaxHeapRemove()
            self.MinHeapInsert(value)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            value = self.MinHeapRemove()
            self.MaxHeapInsert(value)

    def getMedian(self):
        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            return sys.maxsize
        if len(self.maxHeap) == len(self.minHeap):
            return (self.MaxHeapPeek() + self.MinHeapPeek()) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return self.MaxHeapPeek()
        else:
            return self.MinHeapPeek()
    


arr = [1, 9, 2, 8, 3, 7, 4, 6, 5, 1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 10]
hp = MedianHeap()
i = 0
while i < 20:
    hp.insert(arr[i])
    print("Median after insertion of " , arr[i] , " is  " , hp.getMedian())
    i += 1
