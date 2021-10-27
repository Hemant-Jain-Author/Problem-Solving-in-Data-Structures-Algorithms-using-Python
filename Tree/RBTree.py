
class RBTree :
    class Node :
        def __init__(self, data,  nullNode) :
            self.data = data
            self.left = nullNode
            self.right = nullNode
            self.colour = True  #  New node are red in colour.
                                #  true for red colour, false for black colour
            self.parent = nullNode

    def __init__(self) :
        self.NullNode = self.Node(0, None)
        self.NullNode.colour = False
        self.root = self.NullNode

    #  To check whether node is of colour red or not.
    def is_red(self, node) :
        return False if (node == None) else (node.colour == True)

    def uncle(self, node) :
        #  If no parent or grandparent, then no uncle
        if (node.parent == self.NullNode or node.parent.parent == self.NullNode) :
            return  None
        if (node.parent == node.parent.parent.left) : #  uncle on right
            return  node.parent.parent.right
        else : #  uncle on left
            return  node.parent.parent.left
    
    #  Function to right rotate subtree rooted with x
    def right_rotate(self, x) :
        y = x.left
        T = y.right
        #  Rotation
        y.parent = x.parent
        y.right = x
        x.parent = y
        x.left = T
        if (T != self.NullNode) : 
            T.parent = x

        if (x == self.root) :
            self.root = y
            return  y

        if (y.parent.left == x) : 
            y.parent.left = y
        else :
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
        if (T != self.NullNode) : 
            T.parent = x
        if (x == self.root) :
            self.root = y
            return  y
        if (y.parent.left == x) : 
            y.parent.left = y
        else :
            y.parent.right = y
        return  y   #  Return new root

    def right_left_rotate(self, node) :
        node.right = self.right_rotate(node.right)
        return  self.left_rotate(node)

    def left_right_rotate(self, node) :
        node.left = self.left_rotate(node.left)
        return  self.right_rotate(node)

    def find(self, data) :
        curr = self.root
        while (curr != self.NullNode) :
            if (curr.data == data) :
                return  curr
            elif (curr.data > data) :
                curr = curr.left
            else :
                curr = curr.right
        return  None

    def print_tree(self) :
        self.print_tree_util(self.root, "", False)
        print()

    def print_tree_util(self, node,  indent,  isLeft) :
        if (node == self.NullNode) :
            return
        if (isLeft) :
            print(indent + "L:", end ="")
            indent += "|  "
        else :
            print(indent + "R:", end ="")
            indent += "   "
        print(str(node.data) + "(" + str(node.colour) + ")")
        self.print_tree_util(node.left, indent, True)
        self.print_tree_util(node.right, indent, False)

    def insert(self, data) :
        self.root = self.insert_util(self.root, data)
        temp = self.find(data)
        self.fixRedRed(temp)

    def insert_util(self, node,  data) :
        if (node == self.NullNode) :
            node = self.Node(data, self.NullNode)
        elif (node.data > data) :
            node.left = self.insert_util(node.left, data)
            node.left.parent = node
        elif (node.data < data) :
            node.right = self.insert_util(node.right, data)
            node.right.parent = node
        return  node

    def fixRedRed(self, x) :
        #  if x is root colour it black and return
        if (x == self.root) :
            x.colour = False
            return
        if (x.parent == self.NullNode or x.parent.parent == self.NullNode) :
            return
        #  Initialize parent, grandparent, uncle
        parent = x.parent
        grandparent = parent.parent
        uncle = self.uncle(x)
        mid = None
        if (parent.colour == False) :
            return
        #  parent colour is red. gp is black.
        if (uncle != self.NullNode and uncle.colour == True) :
            #  uncle and parent is red.
            parent.colour = False
            uncle.colour = False
            grandparent.colour = True
            self.fixRedRed(grandparent)
            return
        #  parent is red, uncle is black and gp is black.
        #  Perform LR, LL, RL, RR
        if (parent == grandparent.left and x == parent.left) : #  LL
            mid = self.right_rotate(grandparent)
        elif (parent == grandparent.left and x == parent.right) : #  LR
            mid = self.left_right_rotate(grandparent)
        elif (parent == grandparent.right and x == parent.left) : #  RL
            mid = self.right_left_rotate(grandparent)
        elif (parent == grandparent.right and x == parent.right) : #  RR
            mid = self.left_rotate(grandparent)
        mid.colour = False
        mid.left.colour = True
        mid.right.colour = True

    def delete(self, data) :
        self.delete_util(self.root, data)

    def delete_util(self, node,  key) :
        z = self.NullNode
        while (node != self.NullNode) :
            if (node.data == key) :
                z = node
                break
            elif (node.data <= key) :
                node = node.right
            else :
                node = node.left
        if (z == self.NullNode) :
            print("Couldn't find key in the tree")
            return
        y = z
        ycolour = y.colour
        if (z.left == self.NullNode) :
            x = z.right
            self.join_parent_child(z, z.right)
        elif (z.right == self.NullNode) :
            x = z.left
            self.join_parent_child(z, z.left)
        else :
            y = self.minimum(z.right)
            ycolour = y.colour
            z.data = y.data
            self.join_parent_child(y, y.right)
            x = y.right
        if (ycolour == False) :
            if (x.colour == True) :
                x.colour = False
                return
            else :
                self.fix_double_black(x)

    def fix_double_black(self, x) :
        if (x == self.root) : #  Root node.
            return
        sib = self.sibling(x)
        parent = x.parent
        if (sib == self.NullNode) :
            #  No sibling double black shifted to parent.
            self.fix_double_black(parent)
        else :
            if (sib.colour == True) :
                #  Sibling colour is red.
                parent.colour = True
                sib.colour = False
                if (sib.parent.left == sib) :
                    #  Sibling is left child.
                    self.right_rotate(parent)
                else :
                    #  Sibling is right child.
                    self.left_rotate(parent)
                self.fix_double_black(x)
            else :
                #  Sibling colour is black
                #  At least one child is red.
                if (sib.left.colour == True or sib.right.colour == True) :
                    if (sib.parent.left == sib) :
                        #  Sibling is left child.
                        if (sib.left != self.NullNode and sib.left.colour == True) :
                            #  left left case.
                            sib.left.colour = sib.colour
                            sib.colour = parent.colour
                            self.right_rotate(parent)
                        else :
                            #  left right case.
                            sib.right.colour = parent.colour
                            self.left_rotate(sib)
                            self.right_rotate(parent)
                    else :
                        #  Sibling is right child.
                        if (sib.left != self.NullNode and sib.left.colour == True) :
                            #  right left case.
                            sib.left.colour = parent.colour
                            self.right_rotate(sib)
                            self.left_rotate(parent)
                        else :
                            #  right right case.
                            sib.right.colour = sib.colour
                            sib.colour = parent.colour
                            self.left_rotate(parent)
                    parent.colour = False
                else :
                    #  Both children black.
                    sib.colour = True
                    if (parent.colour == False) : 
                        self.fix_double_black(parent)
                    else :
                        parent.colour = False

    def sibling(self, node) :
        #  sibling null if no parent
        if (node.parent == self.NullNode) :
            return  None
        if (node.parent.left == node) :
            return  node.parent.right
        return  node.parent.left

    def join_parent_child(self, u,  v) :
        if (u.parent == self.NullNode) :
            self.root = v
        elif (u == u.parent.left) :
            u.parent.left = v
        else :
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node) :
        while (node.left != self.NullNode) :
            node = node.left
        return  node

tree = RBTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(7)
tree.insert(6)
tree.insert(8)
tree.insert(9)
tree.print_tree()
tree.delete(4)
tree.print_tree()
tree.delete(7)
tree.print_tree()
