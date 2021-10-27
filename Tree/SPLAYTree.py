
class SPLAYTree :
    class Node :
        def __init__(self, d,  l,  r) :
            self.data = d
            self.left = l
            self.right = r
            self.parent = None

    def __init__(self) :
        self.root = None

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
        print(node.data)
        self.print_tree_util(node.left, indent, True)
        self.print_tree_util(node.right, indent, False)

    #  Function to right rotate subtree rooted with x
    def right_rotate(self, x) :
        y = x.left
        T = y.right
        #  Rotation
        y.parent = x.parent
        y.right = x
        x.parent = y
        x.left = T
        if (T != None) : T.parent = x
        if (y.parent != None and y.parent.left == x) : 
            y.parent.left = y
        elif (y.parent != None and y.parent.right == x) : 
            y.parent.right = y
        #  Return new root
        return  y

    #  Function to left rotate subtree rooted with x
    def left_rotate(self, x) :
        y = x.right
        T = y.left
        #  Rotation
        y.parent = x.parent
        y.left = x
        x.parent = y
        x.right = T
        if (T != None) : T.parent = x
        if (y.parent != None and y.parent.left == x) : 
            y.parent.left = y
        elif (y.parent != None and y.parent.right == x) : 
            y.parent.right = y
        #  Return new root
        return  y

    def parent(self, node) :
        if (node == None or node.parent == None) :
            return  None
        return  node.parent

    def splay(self, node) :
        while (node != self.root) :
            parent = self.parent(node)
            grand = self.parent(parent)
            if (parent == None) :
                #  rotations had created new root, always last condition.
                self.root = node
            elif (grand == None) :
                #  single rotation case.
                if (parent.left == node) :
                    node = self.right_rotate(parent)
                else :
                    node = self.left_rotate(parent)
            elif (grand.left == parent and parent.left == node) :
                #  Zig Zig case.
                self.right_rotate(grand)
                node = self.right_rotate(parent)
            elif (grand.right == parent and parent.right == node) :
                #  Zag Zag case.
                self.left_rotate(grand)
                node = self.left_rotate(parent)
            elif (grand.left == parent and parent.right == node) :
                # Zig Zag case.
                self.left_rotate(parent)
                node = self.right_rotate(grand)
            elif (grand.right == parent and parent.left == node) :
                #  Zag Zig case.
                self.right_rotate(parent)
                node = self.left_rotate(grand)

    def find(self, data) :
        curr = self.root
        while (curr != None) :
            if (curr.data == data) :
                self.splay(curr)
                return  True
            elif (curr.data > data) :
                curr = curr.left
            else :
                curr = curr.right
        return  False

    def insert(self, data) :
        newnode = self.Node(data, None, None)
        if (self.root == None) :
            self.root = newnode
            return
        node = self.root
        parent = None
        while (node != None) :
            parent = node
            if (node.data > data) :
                node = node.left
            elif (node.data < data) :
                node = node.right
            else :
                self.splay(node)
                #  duplicate insertion not allowed but splaying for it.
                return
        newnode.parent = parent
        if (parent.data > data) :
            parent.left = newnode
        else :
            parent.right = newnode
        self.splay(newnode)

    def find_min_node(self, curr) :
        node = curr
        if (node == None) :
            return  None
        while (node.left != None) :
            node = node.left
        return  node

    def delete(self, data) :
        node = self.root
        parent = None
        next = None
        while (node != None) :
            if (node.data == data) :
                parent = node.parent
                if (node.left == None and node.right == None) :
                    next = None
                elif (node.left == None) :
                    next = node.right
                elif (node.right == None) :
                    next = node.left
                if (node.left == None or node.right == None) :
                    if (node == self.root) :
                        self.root = next
                        return
                    if (parent.left == node) :
                        parent.left = next
                    else :
                        parent.right = next
                    if (next != None) : next.parent = parent
                    break
                minnode = self.find_min_node(node.right)
                data = minnode.data
                node.data = data
                node = node.right
            elif (node.data > data) :
                parent = node
                node = node.left
            else :
                parent = node
                node = node.right
        self.splay(parent)

    def print_in_order(self) :
        self.print_in_order_util(self.root)
        print()

    def print_in_order_util(self, node) :
        # In order
        if (node != None) :
            self.print_in_order_util(node.left)
            print(node.data, end =" ")
            self.print_in_order_util(node.right)


tree = SPLAYTree()
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.print_tree()
print("Value 2 found: " + str(tree.find(2)))
tree.delete(2)
tree.delete(5)
tree.print_tree()

"""
R:3
   L:2
   |  L:1
   R:6
      L:4
      |  R:5

Value 2 found: True
R:4
   L:3
   |  L:1
   R:6
"""