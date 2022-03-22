from collections import deque

class Stack :
    def __init__(self):
        self.que1 =  deque([])
        self.que2 =  deque([])
        self.size = 0

    def push(self, value) :
        self.que1.append(value)
        self.size += 1

    def pop(self) :
        value = 0
        s = self.size
        while (s > 0) :
            value = self.que1.popleft()
            if (s > 1) : 
                self.que2.append(value)
            s -= 1
        self.que1, self.que2 = self.que2 , self.que1
        self.size -= 1
        return  value
        
    def pop2(self) :
        value = 0
        s = self.size
        while (s > 0) :
            value = self.que1.popleft()
            if (s > 1) : 
                self.que1.append(value)
            s -= 1
        self.size -= 1
        return  value

    
# Testing Code
s = Stack()
s.push(1)
s.push(2)
s.push(3) 
print("Pop :", s.pop())
print("Pop :", s.pop())
print()

s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3) 
print("Pop :", s1.pop2())
print("Pop :", s1.pop2())
    
"""
Pop : 3
Pop : 2
"""
    
    
    