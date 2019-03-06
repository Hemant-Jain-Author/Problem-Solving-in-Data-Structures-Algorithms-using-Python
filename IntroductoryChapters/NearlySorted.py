"""
Given a nearly sorted array, in which an element is at max k units away from its sorted possition.

If you use sorting then it will take O(NlogN) time 

There is one algorithm by which it can be done in O(NlogK) time.
You can create a min Heap of size K+1 from first K+1 elements of input array.
pop an elements from heap and store it into output array. 
push next element from array to heap.
repeat this process till all the elements of array are consumed and heap is empty.
In the end you have sorted array.
"""
import heapq

def sortK(arr, k):
    size = len(arr)
    heap = arr[0:k+1]
    heapq.heapify(heap)
    output = []
    for i in range(k+1, size, 1):
        output.append( heapq.heappop(heap))
        heapq.heappush(heap, arr[i])
    
    while len(heap) > 0:
        output.append( heapq.heappop(heap))
    print output

def sortK2(arr, k):
    size = len(arr)
    heap = arr[0:k+1]
    heapq.heapify(heap)
    index = 0
    for i in range(k+1, size, 1):
        arr[index] = heapq.heappop(heap)
        index += 1
        heapq.heappush(heap, arr[i])
    
    while len(heap) > 0:
        arr[index] = heapq.heappop(heap)
        index += 1

k = 3
arr = [1, 5, 4, 10, 50, 9]
sortK2(arr, k)
print arr