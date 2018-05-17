from collections import deque

class Tree(object):
    class Node(object):
        def __init__(self, v, l=None, r=None):
            self.value = v
            self.lChild = l
            self.rChild = r
    
    def __init__(self):
        self.root = None

    def levelOrderBinaryTree(self, arr):
        self.root = self.levelOrderBinaryTreeUtil(arr, 0)

    def levelOrderBinaryTreeUtil(self, arr, start):
        size = len(arr)
        curr = self.Node(arr[start])
        left = 2 * start + 1
        right = 2 * start + 2
        if left < size:
            curr.lChild = self.levelOrderBinaryTreeUtil(arr, left)
        if right < size:
            curr.rChild = self.levelOrderBinaryTreeUtil(arr, right)
        return curr

    def PrintBredthFirst(self):
        que = deque([])
        output = []
        temp = None
        if self.root != None:
            que.append(self.root)
        while len(que) != 0:
            temp = que.popleft()
            output.append(temp.value)
            if temp.lChild != None:
                que.append(temp.lChild)
            if temp.rChild != None:
                que.append(temp.rChild)
        print output

    def PrintSpiralTree(self):
        stk1 = []
        stk2 = []
        output = []
        temp = None
        if self.root != None:
            stk1.append(self.root)
        while len(stk1) !=0 or len(stk2) != 0:
            while len(stk1) != 0:
                temp = stk1.pop()
                output.append(temp.value)
                if temp.rChild != None:
                    stk2.append(temp.rChild)
                if temp.lChild != None:
                    stk2.append(temp.lChild)

            while len(stk2) != 0:
                temp = stk2.pop()
                output.append(temp.value)
                if temp.lChild != None:
                    stk1.append(temp.lChild)
                if temp.rChild != None:
                    stk1.append(temp.rChild)

        print output


t = Tree()
arr = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20]
t.levelOrderBinaryTree(arr)
t.PrintBredthFirst()
t.PrintSpiralTree()
