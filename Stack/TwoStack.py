#!/usr/bin/env python
from collections import deque

class TwoStack(object):
    def __init__(self):
        self.data = deque([])
        self.size1 = 0
        self.size2 = 0

    def StackPush1(self, value):
        self.data.appendleft(value)
        self.size1 += 1
        
    def StackPop1(self):
        if self.size1 == 0:
            raise RuntimeError("stack empty")
        self.size1 -= 1
        return self.data.popleft()   

    def StackPush2(self, value):
        self.data.append(value)
        self.size2 += 1

    def StackPop2(self):
        if self.size2 == 0:
            raise RuntimeError("stack empty")
        self.size2 -= 1
        return self.data.pop()


st = TwoStack()
i = 0
while i < 10:
    st.StackPush1(i)
    i += 1
j = 0
while j < 10:
    st.StackPush2(j + 10)
    j += 1
i = 0
while i < 10:
    # print "stack one pop value is : " , st.StackPop1()
    print("stack two pop value is : " , st.StackPop2())
    i += 1

