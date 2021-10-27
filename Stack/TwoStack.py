from collections import deque

class TwoStack(object):
    def __init__(self):
        self.data = deque([])
        self.size1 = 0
        self.size2 = 0

    def push1(self, value):
        self.data.appendleft(value)
        self.size1 += 1
        
    def pop1(self):
        if self.size1 == 0:
            raise RuntimeError("stack empty")
        self.size1 -= 1
        return self.data.popleft()   

    def push2(self, value):
        self.data.append(value)
        self.size2 += 1

    def pop2(self):
        if self.size2 == 0:
            raise RuntimeError("stack empty")
        self.size2 -= 1
        return self.data.pop()


st = TwoStack()
st.push1(1)
st.push1(2)
st.push1(3)
st.push2(4)
st.push2(5)
st.push2(6)

print("stk1 pop", st.pop1())
print("stk1 pop", st.pop1())
print("stk2 pop", st.pop2())
print("stk2 pop", st.pop2())

"""
stk1 pop 3
stk1 pop 2
stk2 pop 6
stk2 pop 5
"""