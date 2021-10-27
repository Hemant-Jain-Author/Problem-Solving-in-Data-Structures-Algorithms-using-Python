import math

class AVLTree :
    class Node :
        def __init__(self, d,  l,  r) :
            self.data = d
            self.left = l
            self.right = r
            self.height = 0

    def __init__(self) :
        self.root = None

    def height(self, n) :
        if (n == None) :
            return  -1
        return  n.height

    def get_balance(self, node) :
        return 0 if (node == None) else (self.height(node.left) - self.height(node.right))
    
    def insert(self, data) :
        self.root = self.insert_util(self.root, data)
    
    def insert_util(self, node,  data) :
        if (node == None) :
            return  self.Node(data, None, None)
        if (node.data > data) :
            node.left = self.insert_util(node.left, data)
        elif(node.data < data) :
            node.right = self.insert_util(node.right, data)
        else :
            #  Duplicate data not allowed
            return  node
        
        node.height = max(self.height(node.left), self.height(node.right)) + 1

        balance = self.get_balance(node)
        if (balance > 1) :
            if (data < node.left.data) : #  Left Left Case
                return  self.right_rotate(node)
            if (data > node.left.data) : #  Left Right Case
                return  self.left_right_rotate(node)
        if (balance < -1) :
            if (data > node.right.data) : #  Right Right Case
                return  self.left_rotate(node)
            if (data < node.right.data) : #  Right Left Case
                return  self.right_left_rotate(node)
        return  node

    #  Function to right rotate subtree rooted with x
    def right_rotate(self, x) :
        y = x.left
        T = y.right
        #  Rotation
        y.right = x
        x.left = T
        #  Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        #  Return new root
        return  y
    
    #  Function to left rotate subtree rooted with x
    def left_rotate(self, x) :
        y = x.right
        T = y.left
        #  Rotation
        y.left = x
        x.right = T
        #  Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        #  Return new root
        return  y
    
    #  Function to right then left rotate subtree rooted with x
    def right_left_rotate(self, x) :
        x.right = self.right_rotate(x.right)
        return  self.left_rotate(x)
    
    #  Function to left then right rotate subtree rooted with x
    def left_right_rotate(self, x) :
        x.left = self.left_rotate(x.left)
        return  self.right_rotate(x)
    
    def delete(self, data) :
        self.root = self.delete_util(self.root, data)
    
    def delete_util(self, node,  data) :
        if (node == None) :
            return  None
        if (node.data == data) :
            if (node.left == None and node.right == None) :
                return  None
            elif (node.left == None) :
                return  node.right
            elif (node.right == None) :
                return  node.left
            else :
                min_node = self.find_min(node.right)
                node.data = min_node.data
                node.right = self.delete_util(node.right, min_node.data)
        else :
            if (node.data > data) :
                node.left = self.delete_util(node.left, data)
            else :
                node.right = self.delete_util(node.right, data)
        
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        balance = self.get_balance(node)

        if (balance > 1) :
            if (data >= node.left.data) : #  Left Left Case
                return  self.right_rotate(node)
            if (data < node.left.data) : #  Left Right Case
                return  self.left_right_rotate(node)
        if (balance < -1) :
            if (data <= node.right.data) : #  Right Right Case
                return  self.left_rotate(node)
            if (data > node.right.data) : #  Right Left Case
                return  self.right_left_rotate(node)
        return  node
    
    def find_min(self, curr) :
        node = curr
        if (node == None) :
            return  None
        while (node.left != None) :
            node = node.left
        return  node
    
    def print_tree(self) :
        self.print_tree_util(self.root, "", False)
        print()
    
    def print_tree_util(self, node,  indent,  isLeft) :
        if (node == None) :
            return
        if (isLeft) :
            print(indent + "L:", end ="")
            indent += "|  "
        else :
            print(indent + "R:", end ="")
            indent += "   "
        print(str(node.data) + "(" + str(node.height) + ")")
        self.print_tree_util(node.left, indent, True)
        self.print_tree_util(node.right, indent, False)

t = AVLTree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(7)
t.insert(8)
t.print_tree()
# R:4(3)
#   L:2(1)
#   |  L:1(0)
#   |  R:3(0)
#   R:6(2)
#      L:5(0)
#      R:7(1)
#         R:8(0)
t.delete(5)
t.print_tree()
# R:4(2)
#   L:2(1)
#   |  L:1(0)
#   |  R:3(0)
#   R:7(1)
#      L:6(0)
#      R:8(0)
t.delete(1)
t.print_tree()
# R:4(2)
#   L:2(1)
#   |  R:3(0)
#   R:7(1)
#      L:6(0)
#      R:8(0)
t.delete(2)
t.print_tree()