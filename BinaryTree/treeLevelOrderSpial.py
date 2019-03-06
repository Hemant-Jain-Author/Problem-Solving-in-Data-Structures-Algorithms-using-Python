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

    def PrintLevelOrderLineByLine(self):
        que1 = deque([])
        que2 = deque([])
        temp = None
        if self.root != None:
            que1.append(self.root)
        while len(que1) != 0 or len(que2) != 0 :
            while len(que1) != 0:
                temp = que1.popleft()
                print temp.value,
                if temp.lChild != None:
                    que2.append(temp.lChild)
                if temp.rChild != None:
                    que2.append(temp.rChild)
            print ""
            while len(que2) != 0:
                temp = que2.popleft()
                print temp.value,
                if temp.lChild != None:
                    que1.append(temp.lChild)
                if temp.rChild != None:
                    que1.append(temp.rChild)
            print ""

    def PrintLevelOrderLineByLine2(self):
        que = deque([])
        temp = None
        if self.root != None:
            que.append(self.root)
        while len(que) != 0 :
            count = len(que)
            while count > 0:
                temp = que.popleft()
                print temp.value,
                if temp.lChild != None:
                    que.append(temp.lChild)
                if temp.rChild != None:
                    que.append(temp.rChild)
                count -= 1
            print ""

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

    """
    To see if tree is a heap we need to check two conditions:
    1) It is a complete tree.
    2) Value of a node is grater than or equal to it's left and right child.
    """
    def findCountUtil(self, curr):
        if curr == None:
            return 0
        return (1 + self.findCountUtil(curr.lChild) + self.findCountUtil(curr.rChild))

    def findCount(self):
        return self.findCountUtil(self.root)
    
    def isCompleteTreeUtil(self, curr, index, count):
        if curr == None:
            return True
        if index > count:
            return False 
        return self.isCompleteTreeUtil(curr.lChild, index*2+1, count) and self.isCompleteTreeUtil(curr.rChild, index*2+2, count)

    def isCompleteTree(self):
        count = self.findCount()
        return self.isCompleteTreeUtil(self.root, 0, count)

    def isCompleteTree2(self):
        que = deque([])
        temp = None
        noChild = False
        if self.root != None:
            que.append(self.root)
        while len(que) != 0:
            temp = que.popleft()
            if temp.lChild != None:
                if noChild == True:
                    return False
                que.append(temp.lChild)
            else:
                noChild = True

            if temp.rChild != None:
                if noChild == True:
                    return False
                que.append(temp.rChild)
            else:
                noChild = True

    def isHeapUtil(self, curr, parentValue):
        if curr == None:
            return True
        if curr.value < parentValue:
            return False
        return ( self.isHeapUtil(curr.lChild, curr.value) and self.isHeapUtil(curr.rChild, curr.value ))

    def isHeap(self):
        infi = -9999999
        return self.isCompleteTree() and self.isHeapUtil(self.root, infi)


    def isHeapUtil2(self, curr, index, count, parentValue):
        if curr == None:
            return True
        if index > count:
            return False
        if curr.value < parentValue:
            return False 
        return self.isHeapUtil2(curr.lChild, index*2+1, count, curr.value) and self.isHeapUtil2(curr.rChild, index*2+2, count, curr.value)

    def isHeap2(self):
        count = self.findCount()
        parentValue = -9999999
        return self.isHeapUtil2(self.root, 0, count, parentValue)



    def isHeap3(self):
        que = deque([])
        que.append(self.root)
        que.append(0)
        que.append(-99999)
        count = 0
        while len(que) != 0:
            curr = que.popleft()
            currIndex = que.popleft()
            parentValue = que.popleft()

            if curr.value < parentValue or currIndex != count :
                return False
            count += 1
            if curr.lChild != None :
                que.append(curr.lChild)
                que.append(currIndex * 2 + 1)
                que.append(curr.value)
            
            if curr.rChild != None :
                que.append(curr.rChild)
                que.append(currIndex * 2 + 2)
                que.append(curr.value)

        return True


"""
Use queue to traverse the tree. In queue you will keep index and parent value. 
When you dequeue element from queue you will keep track count of element 
count should be equal to the index value.
"""

t = Tree()
arr = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20]
t.levelOrderBinaryTree(arr)
t.PrintBredthFirst()
t.PrintLevelOrderLineByLine()
#print t.isCompleteTree()
print t.isHeap()
# t.PrintSpiralTree()
# t.PrintLevelOrderLineByLine()
# t.PrintLevelOrderLineByLine2()
# Print Level order sum
# Print level order max
# Print Level order sum max