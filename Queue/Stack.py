from collections import deque

class Stack :
    que1 =  deque([])
    que2 =  deque([])
    size = 0

    def push(self, value) :
        self.que1.append(value)
        self.size += 1

    def pop(self) :
        value = 0
        s = self.size
        while (s > 0) :
            value = self.que1.popleft()
            if (s > 1) : self.que2.append(value)
            s -= 1
        self.que1, self.que2 = self.que2 , self.que1
        self.size -= 1
        return  value
        
    def pop2(self) :
        value = 0
        s = self.size
        while (s > 0) :
            value = self.que1.popleft()
            if (s > 1) : self.que1.append(value)
            s -= 1
        self.size -= 1
        return  value


s =  Stack()
i = 0
while (i < 5) :
    s.push(i)    
    i += 1
i = 0
while (i < 5) :
    print(str(s.pop2()) + " ", end ="")    
    i += 1