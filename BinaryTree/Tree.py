#!/usr/bin/env python
from collections import deque
import math

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
    
    def InsertNode(self, value):
        self.root = self.InsertNodeUtil(self.root, value)

    def InsertNodeUtil(self, node, value):
        if node == None:
            node = self.Node(value)
        else:
            if node.value > value:
                node.lChild = self.InsertNodeUtil(node.lChild, value)
            else:
                node.rChild = self.InsertNodeUtil(node.rChild, value)
        return node

    
    def PrintPreOrder(self):
        self.PrintPreOrderUtil(self.root)


    def PrintPreOrderUtil(self, node):
        #    pre order  
        if node != None:
            print(node.value, end=' ')
            self.PrintPreOrderUtil(node.lChild)
            self.PrintPreOrderUtil(node.rChild)

    def NthPreOrder(self, index):
        count = [0] 
        self.NthPreOrderUtil(self.root, index, count)

    def NthPreOrderUtil(self, node, index, count):
        #    pre order  
        if node != None:
            count[0] += 1
            if count[0] == index:
                print(node.value, end=' ')
            self.NthPreOrderUtil(node.lChild, index, count)
            self.NthPreOrderUtil(node.rChild, index, count)

    
    def PrintPostOrder(self):
        self.PrintPostOrderUtil(self.root)

    def PrintPostOrderUtil(self, node):
        #    post order  
        if node != None:
            self.PrintPostOrderUtil(node.lChild)
            self.PrintPostOrderUtil(node.rChild)
            print(node.value, end=' ')

    
    def NthPostOrder(self, index):
        count = [0]
        self.NthPostOrderUtil(self.root, index, count)

    def NthPostOrderUtil(self, node, index, count):
        #    post order  
        if node != None:
            self.NthPostOrderUtil(node.lChild, index, count)
            self.NthPostOrderUtil(node.rChild, index, count)
            count[0] += 1
            if count[0] == index:
                print(node.value, end=' ')

    
    def PrintInOrder(self):
        self.PrintInOrderUtil(self.root)


    def PrintInOrderUtil(self, node):
        #    In order  
        if node != None:
            self.PrintInOrderUtil(node.lChild)
            print(node.value, end=' ')
            self.PrintInOrderUtil(node.rChild)

    
    def NthInOrder(self, index):
        count = [0]
        self.NthInOrderUtil(self.root, index, count)


    def NthInOrderUtil(self, node, index, count):
        if node != None:
            self.NthInOrderUtil(node.lChild, index, count)
            count[0] += 1
            if count[0] == index:
                print(node.value, end=' ')
            self.NthInOrderUtil(node.rChild, index, count)

    def PrintBredthFirst(self):
        que = deque([])
        temp = None
        if self.root != None:
            que.append(self.root)
        while len(que) != 0:
            temp = que.popleft()
            print(temp.value, end=' ')
            if temp.lChild != None:
                que.append(temp.lChild)
            if temp.rChild != None:
                que.append(temp.rChild)

    def PrintDepthFirst(self):
        stk = []
        if self.root != None:
            stk.append(self.root)
        while stk.isEmpty() == False:
            temp = stk.pop()
            print(temp.value, end=' ')
            if temp.lChild != None:
                stk.append(temp.lChild)
            if temp.rChild != None:
                stk.append(temp.rChild)

    def Find(self, value):
        curr = self.root
        while curr != None:
            if curr.value == value:
                return True
            elif curr.value > value:
                curr = curr.lChild
            else:
                curr = curr.rChild
        return False

    
    def FindMin(self):
        node = self.root
        if node == None:
            raise RuntimeError("ListEmptyException")
        while node.lChild != None:
            node = node.lChild
        return node.value

    
    def FindMax(self):
        node = self.root
        if node == None:
            raise RuntimeError("ListEmptyException")
        while node.rChild != None:
            node = node.rChild
        return node.value

    def FindMaxUtil(self, curr):
        node = curr
        if node == None:
            return None
        while node.rChild != None:
            node = node.rChild
        return node

    def FindMinUtil(self, curr):
        node = curr
        if node == None:
            return None
        while node.lChild != None:
            node = node.lChild
        return node

    def Free(self):
        self.root = None
    
    def DeleteNode(self, value):
        self.root = self.DeleteNodeUtil(self.root, value)

    def DeleteNodeUtil(self, node, value):
        temp = None
        if node != None:
            if node.value == value:
                if node.lChild == None and node.rChild == None:
                    return None
                else:
                    if node.lChild == None:
                        temp = node.rChild
                        return temp
                    if node.rChild == None:
                        temp = node.lChild
                        return temp
                    maxnode = self.FindMaxUtil(node.lChild)
                    node.value = maxnode.value
                    node.lChild = self.DeleteNodeUtil(node.lChild, maxnode.value)
            else:
                if node.value > value:
                    node.lChild = self.DeleteNodeUtil(node.lChild, value)
                else:
                    node.rChild = self.DeleteNodeUtil(node.rChild, value)
        return node

    
    def TreeDepth(self):
        return self.TreeDepthUtil(self.root)

    def TreeDepthUtil(self, root):
        if root == None:
            return 0
        else:
            lDepth = self.TreeDepthUtil(root.lChild)
            rDepth = self.TreeDepthUtil(root.rChild)
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1

    def isEqual(self, T2):
        return self.Identical(self.root, T2.root)

    def Identical(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            return (self.Identical(node1.lChild, node2.lChild) and self.Identical(node1.rChild, node2.rChild) and (node1.value == node2.value))

    
    def Ancestor(self, first, second):
        if first > second:
            temp = first
            first = second
            second = temp
        curr = self.AncestorUtil(self.root, first, second)
        if curr == None:
            retval = sys.maxsize
        else :
            retval = curr.value
        return retval

    def AncestorUtil(self, curr, first, second):
        if curr == None:
            return None
        if curr.value > first and curr.value > second:
            return self.AncestorUtil(curr.lChild, first, second)
        if curr.value < first and curr.value < second:
            return self.AncestorUtil(curr.rChild, first, second)
        return curr

    
    def CopyTree(self):
        tree2 = Tree()
        tree2.root = self.CopyTreeUtil(self.root)
        return tree2

    def CopyTreeUtil(self, curr):
        if curr != None:
            temp = self.Node(curr.value)
            temp.lChild = self.CopyTreeUtil(curr.lChild)
            temp.rChild = self.CopyTreeUtil(curr.rChild)
            return temp
        else:
            return None

    
    def CopyMirrorTree(self):
        tree2 = Tree()
        tree2.root = self.CopyMirrorTreeUtil(self.root)
        return tree2

    def CopyMirrorTreeUtil(self, curr):
        if curr != None:
            temp = self.Node(curr.value)
            temp.rChild = self.CopyMirrorTreeUtil(curr.lChild)
            temp.lChild = self.CopyMirrorTreeUtil(curr.rChild)
            return temp
        else:
            return None

    
    def numNodes(self):
        return self.numNodesUtil(self.root)

    def numNodesUtil(self, curr):
        if curr == None:
            return 0
        else:
            return (1 + self.numNodesUtil(curr.rChild) + self.numNodesUtil(curr.lChild))

    
    def numFullNodesBT(self):
        return self.numFullNodesBTUtil(self.root)

    def numFullNodesBTUtil(self, curr):
        if curr == None:
            return 0
        count = self.numFullNodesBTUtil(curr.rChild) + self.numFullNodesBTUtil(curr.lChild)
        if curr.rChild != None and curr.lChild != None:
            count += 1
        return count

    
    def maxLengthPathBT(self):
        return self.maxLengthPathBTUtil(self.root)

    def maxLengthPathBTUtil(self, curr):
        # diameter
        if curr == None:
            return 0
        leftPath = self.TreeDepthUtil(curr.lChild)
        rightPath = self.TreeDepthUtil(curr.rChild)
        maxpath = leftPath + rightPath + 1
        leftMax = self.maxLengthPathBTUtil(curr.lChild)
        rightMax = self.maxLengthPathBTUtil(curr.rChild)
        if leftMax > maxpath:
            maxpath = leftMax
        if rightMax > max:
            maxpath = rightMax
        return maxpath

    
    def numLeafNodes(self):
        return self.numLeafNodesUtil(self.root)

    def numLeafNodesUtil(self, curr):
        if curr == None:
            return 0
        if curr.lChild == None and curr.rChild == None:
            return 1
        else:
            return (self.numLeafNodesUtil(curr.rChild) + self.numLeafNodesUtil(curr.lChild))

    
    def sumAllBT(self):
        return self.sumAllBTUtil(self.root)

    def sumAllBTUtil(self, curr):
        if curr == None:
            return 0
        rightSum = self.sumAllBTUtil(curr.rChild)
        leftSum = self.sumAllBTUtil(curr.lChild)
        finalsum = rightSum + leftSum + curr.value
        return finalsum

    def iterativePreOrder(self):
        stk = []
        if self.root != None:
            stk.append(self.root)
        while len(stk) != 0:
            curr = stk.pop()
            print(curr.value, end=' ')
            if curr.rChild != None:
                stk.append(curr.rChild)
            if curr.lChild != None:
                stk.append(curr.lChild)

    def iterativePostOrder(self):
        stk = []
        visited = []
        if self.root != None:
            stk.append(self.root)
            visited.append(0)
        while len(stk) != 0:
            curr = stk.pop()
            vtd = visited.pop()
            if vtd == 1:
                print(curr.value, end=' ')
            else:
                stk.append(curr)
                visited.append(1)                
                if curr.rChild != None:
                    stk.append(curr.rChild)
                    visited.append(0)
                if curr.lChild != None:
                    stk.append(curr.lChild)
                    visited.append(0)

    def iterativeInOrder(self):
        stk = []
        visited = []
        if self.root != None:
            stk.append(self.root)
            visited.append(0)
        while len(stk) != 0:
            curr = stk.pop()
            vtd = visited.pop()
            if vtd == 1:
                print(curr.value, end=' ')
            else:
                if curr.rChild != None:
                    stk.append(curr.rChild)
                    visited.append(0)
                stk.append(curr)
                visited.append(1)
                if curr.lChild != None:
                    stk.append(curr.lChild)
                    visited.append(0)

    def isBST3(self, root):
        if root == None:
            return True
        if root.lChild != None and self.FindMax(root.lChild).value > root.value:
            return False
        if root.rChild != None and self.FindMin(root.rChild).value <= root.value:
            return False
        return (self.isBST3(root.lChild) and self.isBST3(root.rChild))

    
    def isBST(self):
        return self.isBSTUtil(self.root, -999999, 999999)

    def isBSTUtil(self, curr, minval, maxval):
        if curr == None:
            return True
        if curr.value < minval or curr.value > maxval:
            return False
        return self.isBSTUtil(curr.lChild, minval, curr.value) and self.isBSTUtil(curr.rChild, curr.value, maxval)

    
    def isBST2(self):
        count = [0]
        return self.isBST2Util(self.root, count)

    def isBST2Util(self, curr, count):
        #   in order  traversal 
        ret = bool()
        if curr != None:
            ret = self.isBST2Util(curr.lChild, count)
            if not ret:
                return False
            if count[0] > curr.value:
                return False
            count[0] = curr.value
            ret = self.isBST2Util(curr.rChild, count)
            if not ret:
                return False
        return True

        
    def printAllPath(self):
        stk = []
        self.printAllPathUtil(self.root, stk)

    def printAllPathUtil(self, curr, stk):
        if curr == None:
            return
        stk.append(curr.value)
        if curr.lChild == None and curr.rChild == None:
            print(stk)
            stk.pop()
            return
        self.printAllPathUtil(curr.rChild, stk)
        self.printAllPathUtil(curr.lChild, stk)
        stk.pop()

    
    def LCA(self, first, second):
        ans = self.LCAUtil(self.root, first, second)
        if ans != None:
            return ans.value
        else:
            return sys.maxsize

    def LCAUtil(self, curr, first, second):
        if curr == None:
            return None
        if curr.value == first or curr.value == second:
            return curr
        left = self.LCAUtil(curr.lChild, first, second)
        right = self.LCAUtil(curr.rChild, first, second)
        if left != None and right != None:
            return curr
        elif left != None:
            return left
        else:
            return right

    
    def LcaBST(self, first, second):
        curr = self.LcaBSTUtil(self.root, first, second)
        if(curr == None):
            raise RuntimeError("LCAMissing")
        return curr.value

    def LcaBSTUtil(self, curr, first, second):
        if curr == None:
            return None
        if curr.value > first and curr.value > second:
            return self.LcaBSTUtil(curr.lChild, first, second)
        if curr.value < first and curr.value < second:
            return self.LcaBSTUtil(curr.rChild, first, second)
        return curr

    
    def trimOutsideRange(self, minval, maxval):
        self.trimOutsideRangeUtil(self.root, minval, maxval)

    def trimOutsideRangeUtil(self, curr, minval, maxval):
        if curr == None:
            return None
        curr.lChild = self.trimOutsideRangeUtil(curr.lChild, minval, maxval)
        curr.rChild = self.trimOutsideRangeUtil(curr.rChild, minval, maxval)
        if curr.value < minval:
            return curr.rChild
        if curr.value > maxval:
            return curr.lChild
        return curr

    
    def printInRange(self, minval, maxval):
        self.printInRangeUtil(self.root, minval, maxval)

    def printInRangeUtil(self, root, minval, maxval):
        if root == None:
            return
        self.printInRangeUtil(root.lChild, minval, maxval)
        if root.value >= minval and root.value <= maxval:
            print(root.value, end=' ')
        self.printInRangeUtil(root.rChild, minval, maxval)

    def FloorBST(self, val):
        curr = self.root
        floor = sys.maxsize
        while curr != None:
            if curr.value == val:
                floor = curr.value
                break
            elif curr.value > val:
                curr = curr.lChild
            else:
                floor = curr.value
                curr = curr.rChild
        return floor

    def CeilBST(self, val):
        curr = self.root
        ceil = -1 * (sys.maxunicode)
        while curr != None:
            if curr.value == val:
                ceil = curr.value
                break
            elif curr.value > val:
                ceil = curr.value
                curr = curr.lChild
            else:
                curr = curr.rChild
        return ceil

    
    def findMaxBT(self):
        ans = self.findMaxBTUtil(self.root)
        return ans

    def findMaxBTUtil(self, curr):
        if curr == None:
            return -1 * sys.maxsize
        maxval = curr.value
        left = self.findMaxBTUtil(curr.lChild)
        right = self.findMaxBTUtil(curr.rChild)
        if left > maxval:
            maxval = left
        if right > maxval:
            maxval = right
        return maxval

    def searchBT(self, root, value):
        if root == None:
            return False
        if root.value == value:
            return True
        left = self.searchBT(root.lChild, value)
        if left:
            return True
        right = self.searchBT(root.rChild, value)
        if right:
            return True
        return False

    
    def CreateBinaryTree(self, arr):
        self.root = self.CreateBinaryTreeUtil(arr, 0, len(arr)-1)

    def CreateBinaryTreeUtil(self, arr, start, end):
        if start > end:
            return None
        mid = math.floor((start + end) / 2) 
        curr = self.Node(arr[mid])
        curr.lChild = self.CreateBinaryTreeUtil(arr, start, mid - 1)
        curr.rChild = self.CreateBinaryTreeUtil(arr, mid + 1, end)
        return curr

    def treeToList(self):
        return self.treeToListRec(self.root)

    def treeToListRec(self, curr):
        if curr == None:
            return None        
        if curr.lChild == None and curr.rChild == None:
            curr.lChild = curr
            curr.rChild = curr
            return curr
        if curr.lChild != None:
            Head = self.treeToListRec(curr.lChild)
            Tail = Head.lChild
            curr.lChild = Tail
            Tail.rChild = curr
        else:
            Head = curr
            
        if curr.rChild != None:
            tempHead = self.treeToListRec(curr.rChild)
            Tail = tempHead.lChild
            curr.rChild = tempHead
            tempHead.lChild = curr
        else:
            Tail = curr
        
        Head.lChild = Tail
        Tail.rChild = Head
        return Head

#=======================================================================
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# t2 = Tree()
# t2.levelOrderBinaryTree(arr)
#=======================================================================
#=======================================================================
# t = Tree()
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # t.levelOrderBinaryTree(arr)
# t.InsertNode(5)
# t.InsertNode(3)
# t.InsertNode(4)
# t.InsertNode(2)
# t.InsertNode(1)
# t.InsertNode(8)
# t.InsertNode(7)
# t.InsertNode(9)
# # print(t.CeilBST(6))
# t.printAllPath()
# print("")
# t.iterativeInOrder()
# print("")
# t.PrintInOrder()
# print("") 
# t.iterativePreOrder()
# print("")
# t.PrintPreOrder()
# print("")
# t.iterativePostOrder()
# print("")        
# t.PrintPostOrder()
# print("")
# 
# t.PrintBredthFirst()
# # t.treeToList();
# print ( t.LCA(10, 3) )
#=======================================================================
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t2 = Tree()
# t2.levelOrderBinaryTree(arr)
#=======================================================================
# t2.InsertNode(5)
# t2.InsertNode(3)
# t2.InsertNode(4)
# t2.InsertNode(2)
# t2.InsertNode(1)
# t2.InsertNode(8)
# t2.InsertNode(7)
# t2.InsertNode(9)
#=======================================================================
#print(t2.Ancestor(1, 10))
#print(t2.CeilBST(7))
#print(t2.FloorBST(12))
t2.CreateBinaryTree(arr)
t2.PrintInOrder()
print("")
t2.iterativeInOrder()
print("")
t2.PrintPostOrder()
print("")
t2.iterativePostOrder()
print("")
t2.PrintPreOrder()
print("")
t2.iterativePreOrder()
#t2.DeleteNode(8)
#=======================================================================
# t3 = t2.CopyMirrorTree()
# t2.PrintInOrder()
# print("")
# t3.PrintInOrder()
# print(t2.Find(18))
# print(t2.findMaxBT())
# print(t2.FindMax())
# print(t2.FindMin())
# t4 = t2.CopyTree()
# t4.PrintInOrder()
# print("")
# t2.PrintInOrder()
# print("")
# t2.PrintPostOrder()
# print("")
# t2.PrintPreOrder()
# print("")
# print(t2.numNodes())
# print(t2.NthInOrder(2))
# print(t2.NthPostOrder(2))
# print(t2.NthPreOrder(2))
# print(t2.isEqual(t4))
# print(t2.TreeDepth())
# print(t2.maxLengthPathBT())
# print(t2.numFullNodesBT())
# print(t2.isBST())
# print(t2.isBST2())
# print(t2.numLeafNodes())
# print(t2.numNodes())
# print(t2.printInRange(4, 7))
# print(t2.trimOutsideRange(3, 8))
# print(t2.PrintInOrder())
#=======================================================================
