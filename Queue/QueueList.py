class Queue(object):
    class Node(object):
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def length(self):
        return self.count
    
    def is_empty(self):
        return (self.head == None)

    def peek(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        return self.head.value

    def add(self, value):
        temp = self.Node(value, None)
        self.count += 1
        if self.head == None:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def remove(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        self.count -= 1
        value = self.head.value
        self.head = self.head.next
        return value

    def print(self):
        temp = self.head
        print("Queue:", end=' ')
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next
        print()

# Testing Code
que = Queue()
que.add(1)
que.add(2)
que.add(3)
que.print()
print("Queue length:", que.length())
print("Queue is empty:", que.is_empty())
print("Queue remove:", que.remove())
que.print()

"""
Queue: 1 2 3 
Queue length: 3
Queue is empty: False
Queue remove: 1
Queue: 2 3 
"""

