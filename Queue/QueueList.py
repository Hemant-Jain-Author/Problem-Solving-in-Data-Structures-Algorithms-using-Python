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
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next

 
que = Queue()
que.add(1)
que.add(2)
que.add(3)
print(que.length())
print(que.is_empty())
print(que.remove())
print(que.remove())
print(que.remove())
print(que.length())
print(que.is_empty())
"""
3
False
1
2
3
0
True
"""

