class Stack(object):
    class Node(object):
        def __init__(self, v, n):
            self.value = v
            self.next = n

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        return self.head.value

    def push(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise RuntimeError("StackEmptyException")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value


    def print(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next
        print()


s = Stack()
s.push(1)
s.push(2)
s.push(3) 
s.print()
print(s.pop())
s.print()

"""
3 2 1 
3
2 1 
"""
