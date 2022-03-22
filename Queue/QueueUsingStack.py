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

    def print(self):
        l1 = len(self.stk1)
        l2 = len(self.stk2)
        print("Queue:", end=' ')
        for i in range(l2-1, -1, -1):
            print(self.stk2[i], end=" ")

        for i in range(l1):
            print(self.stk1[i], end=" ")
        print()


# Testing Code
que = QueueUsingStack()
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