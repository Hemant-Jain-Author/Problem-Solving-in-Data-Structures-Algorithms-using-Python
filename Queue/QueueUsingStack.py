class QueueUsingStack(object):
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def add(self, value):
        self.stk1.append(value)

    def remove(self):
        if len(self.stk2) != 0:
            return self.stk2.pop()
        while len(self.stk1) != 0:
            value = self.stk1.pop()
            self.stk2.append(value)
        return self.stk2.pop()

    def length(self):
        return len(self.stk1) + len(self.stk2)

    def is_empty(self):
        return len(self.stk1) + len(self.stk2) == 0

# Testing Code
que = QueueUsingStack()
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