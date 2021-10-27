import heapq

class MedianHeap(object):
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def min_heap_insert(self, value):
        heapq.heappush(self.minHeap, value)
        
    def max_heap_insert(self, value):
        heapq.heappush(self.maxHeap, -1 * value)
        
    def max_heap_peek(self):
        return -1 * self.maxHeap[0]
    
    def min_heap_peek(self):
        return self.minHeap[0]
        
    def min_heap_remove(self):
        return heapq.heappop(self.minHeap)
    
    def max_heap_remove(self):
        return -1 * heapq.heappop(self.maxHeap)

    # Other Methods.
    def insert(self, value):
        if len(self.maxHeap) == 0 or self.max_heap_peek() >= value:
            self.max_heap_insert(value)
        else:
            self.min_heap_insert(value)
        # size balancing
        if len(self.maxHeap) > len(self.minHeap) + 1:
            value = self.max_heap_remove()
            self.min_heap_insert(value)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            value = self.min_heap_remove()
            self.max_heap_insert(value)

    def get_median(self):
        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            return sys.maxsize
        if len(self.maxHeap) == len(self.minHeap):
            return (self.max_heap_peek() + self.min_heap_peek()) // 2
        elif len(self.maxHeap) > len(self.minHeap):
            return self.max_heap_peek()
        else:
            return self.min_heap_peek()

def main():
    arr = [1, 9, 2, 8, 3, 7]
    hp = MedianHeap()
    i = 0
    while i < 6:		
        hp.insert(arr[i])
        print("Median after insertion of ", arr[i], " is ", hp.get_median())
        i += 1

main()

"""
Median after insertion of  1  is  1
Median after insertion of  9  is  5
Median after insertion of  2  is  2
Median after insertion of  8  is  5
Median after insertion of  3  is  3
Median after insertion of  7  is  5
"""