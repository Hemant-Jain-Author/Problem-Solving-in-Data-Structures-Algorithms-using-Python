
class BTree :
    #  Maximum degree
    #  Minimum degree
    def __init__(self, dg) :
        self.root = None        #  Pointer to root node
        self.maxval = dg           #  Max number of children.
        self.minval = dg // 2  #  Min number of children.
    
    class Node :
        #  Constructor
        def __init__(self, leaf, mx) :
            self.n = 0 #  Current number of keys
            self.keys = [0] * mx #  A list of keys
            self.arr = [None] * (mx + 1) #  An list of child pointers
            self.leaf = leaf #  Is true when node is leaf. Otherwise false
    
    def print_tree(self) :
        self.print_tree_util(self.root, "")
        print()

    def print_tree_util(self, node,  indent) :
        if (node == None) :
            return
        i = 0
        while(i < node.n) :
            self.print_tree_util(node.arr[i], indent + "    ")
            print(indent, "key[", i, "]:", node.keys[i])
            i += 1

        self.print_tree_util(node.arr[i], indent + "    ")

    def print_in_order(self, node) :
        for i in range(node.n) :
            if (node.leaf == False) : self.print_in_order(node.arr[i])
            print(node.keys[i], end =" ")
            
        if (node.leaf == False) :
            self.print_in_order(node.arr[i])

    def search(self, key) :
        if (self.root == None) :
            return  None
        return  self.search_util(self.root, key)

    def search_util(self, node,  key) :
        i = 0
        while (i < node.n and node.keys[i] < key) :
            i += 1
        #  If the found key is equal to key, return this node
        if (node.keys[i] == key) :
            return  node
        #  If the key is not found and this is a leaf node
        if (node.leaf == True) :
            return  None
        #  Search in the appropriate child
        return  self.search_util(node.arr[i], key)

    def insert(self, key) :
        #  If tree is empty
        if (self.root == None) :
            self.root = self.Node(True, self.maxval) #  Allocate memory for root
            self.root.keys[0] = key #  Insert key
            self.root.n = 1 #  Update number of keys in root
            return

        if (self.root.leaf == True) :
            #  Finds the location where new key can be inserted.
            #  By moving all keys greater than key to one place forward.
            i = self.root.n - 1
            while (i >= 0 and self.root.keys[i] > key) :
                self.root.keys[i + 1] = self.root.keys[i]
                i -= 1
            #  Insert the new key at found location
            self.root.keys[i + 1] = key
            self.root.n = self.root.n + 1
        else :
            i = 0
            while (i < self.root.n and self.root.keys[i] < key) :
                i += 1
            self.insert_util(self.root, self.root.arr[i], i, key)

        if (self.root.n == self.maxval) :
            #  If root contains more then allowed nodes, then tree grows in height.
            #  Allocate memory for new root
            rt = self.Node(False, self.maxval)
            rt.arr[0] = self.root
            self.split(rt, self.root, 0) #  divide the child into two and then add the median to the parent.
            self.root = rt
    
    #  Insert a new key in this node
    #  Arguments are parent, child, index of child and key.
    def insert_util(self, parent,  child,  index,  key) :
        if (child.leaf == True) :
            #  Finds the location where new key will be inserted 
            #  by moving all keys greater than key to one place forward.
            i = child.n - 1
            while (i >= 0 and child.keys[i] > key) :
                child.keys[i + 1] = child.keys[i]
                i -= 1
            #  Insert the new key at found location
            child.keys[i + 1] = key
            child.n += 1
        else :
            #  insert the node to the proper child.
            i = 0
            while (i < child.n and child.keys[i] < key) :
                i += 1
            self.insert_util(child, child.arr[i], i, key)
        if (child.n == self.maxval) : #  More nodes than allowed.
            #  divide the child into two and then add the median to the parent.
            self.split(parent, child, index)
    
    def split(self, parent,  child,  index) :
        #  Getting index of median.
        median = int(self.maxval / 2)

        #  Reduce the number of keys in child
        child.n = median
        node = self.Node(child.leaf, self.maxval)

        #  Copy the second half keys of child to node
        j = 0
        while (median + 1 + j < self.maxval) :
            node.keys[j] = child.keys[median + 1 + j]
            j += 1
        node.n = j
        #  Copy the second half children of child to node
        j = 0
        while (child.leaf == False and median + j <= self.maxval - 1) :
            node.arr[j] = child.arr[median + 1 + j]
            j += 1
        #  parent is going to have a new child,
        #  create space of new child
        j = parent.n
        while (j >= index + 1) :
            parent.arr[j + 1] = parent.arr[j]    
            j -= 1
        #  Link the new child to the parent node
        parent.arr[index + 1] = node
        #  A key of child will move to the parent node. 
        #  Find the location of new key by moving
        #  all greater keys one space forward.
        j = parent.n - 1
        while (j >= index) :
            parent.keys[j + 1] = parent.keys[j]    
            j -= 1
        #  Copy the middle key of child to the parent
        parent.keys[index] = child.keys[median]
        #  Increment count of keys in this parent
        parent.n += 1

    def remove(self, key) :
        self.remove_util(self.root, key)
        if (self.root.n == 0) :
            #  Shrinking : If root is pointing to empty node.
            #  If that node is a leaf node then root will become null.
            #  Else root will point to first child of node.
            if (self.root.leaf) : 
                self.root = None
            else :
                self.root = self.root.arr[0]
        
    def remove_util(self, node,  key) :
        index = self.find_key(node, key)
        if (node.leaf) :
            if (index < node.n and node.keys[index] == key) :
                self.remove_from_leaf(node, index)
            else :
                print("The key " + str(key) + " not found.")
                return
        else :
            if (index < node.n and node.keys[index] == key) :
                self.remove_from_non_leaf(node, index)
            else :
                self.remove_util(node.arr[index], key)
            #  All the property violation in index subtree only.
            #  which include remove from leaf case too.
            if (node.arr[index].n < self.minval) :
                self.fix_BTree(node, index)
    
    #  Returns the index of first key which is greater than or equal to key.
    def find_key(self, node,  key) :
        index = 0
        while (index < node.n and node.keys[index] < key) :
            index += 1
        return  index

    #  Remove the index key from leaf node.
    def remove_from_leaf(self, node,  index) :
        #  Move all the keys after the index position one step left.
        i = index + 1
        while (i < node.n) :
            node.keys[i - 1] = node.keys[i]    
            i += 1
        
        #  Reduce the key count.
        node.n -= 1
        return
    
    #  Remove the index key from a non-leaf node.
    def remove_from_non_leaf(self, node,  index) :
        key = node.keys[index]
        #  If the child that precedes key has at least min keys,
        #  Find the predecessor 'pred' of key in the subtree rooted at index.
        #  Replace key by pred and recursively delete pred in arr[index]
        if (node.arr[index].n > self.minval) :
            pred = self.get_pred(node, index)
            node.keys[index] = pred
            self.remove_util(node.arr[index], pred)
        # If the child that succeeds key has at least min keys,
        # Find the successor 'succ' of key in the subtree rooted at index+1.
        # Replace key by succ and recursively delete succ in arr[ index+1].
        elif (node.arr[index + 1].n > self.minval) :
            succ = self.get_succ(node, index)
            node.keys[index] = succ
            self.remove_util(node.arr[index + 1], succ)
        # If both left and right subtree has min number of keys.
        # Then merge left, right child along with parent key.
        # Then call remove on the merged child.
        else :
            self.merge(node, index)
            self.remove_util(node.arr[index], key)
        return

    #  To get predecessor of keys[index]
    def get_pred(self, node,  index) :
        #  Keep moving to the right most node of left subtree until we reach a leaf.
        cur = node.arr[index]
        while (not cur.leaf) :
            cur = cur.arr[cur.n]
        #  Return the last key of the leaf
        return  cur.keys[cur.n - 1]
    
    #  To get successor of keys[index]
    def get_succ(self, node,  index) :
        #  Keep moving to the left most node of right subtree until we reach a leaf
        cur = node.arr[index + 1]
        while (not cur.leaf) :
            cur = cur.arr[0]
        #  Return the first key of the leaf
        return  cur.keys[0]

    #  Make sure that the node have at least min number of keys
    def fix_BTree(self, node,  index) :
        #  If the left sibling has more than min keys.
        if (index != 0 and node.arr[index - 1].n > self.minval) :
            self.borrow_from_left(node, index)
        # If the right sibling has more than min keys.
        elif (index != node.n and node.arr[index + 1].n > self.minval) :
            self.borrow_from_right(node, index)
        # If both siblings has less than min keys.
        # When right sibling exist always merge with the right sibling.
        # When right sibling does not exist then merge with left sibling.
        else :
            if (index != node.n) : 
                self.merge(node, index)
            else :
                self.merge(node, index - 1)
    
    #  Move a key from parent to right and left to parent.
    def borrow_from_left(self, node,  index) :
        child = node.arr[index]
        sibling = node.arr[index - 1]
        #  Moving all key in child one step forward.
        i = child.n - 1
        while (i >= 0) :
            child.keys[i + 1] = child.keys[i]    
            i -= 1
        
        #  Move all its child pointers one step forward.
        i = child.n
        while (not child.leaf and i >= 0) :
            child.arr[i + 1] = child.arr[i]    
            i -= 1

        #  Setting child's first key equal to of the current node.
        child.keys[0] = node.keys[index - 1]

        #  Moving sibling's last child as child's first child.
        if (not child.leaf) : 
            child.arr[0] = sibling.arr[sibling.n]

        #  Moving the key from the sibling to the parent
        node.keys[index - 1] = sibling.keys[sibling.n - 1]

        #  Increase child key count and decrease sibling key count.
        child.n += 1
        sibling.n -= 1
        return
    
    #  Move a key from parent to left and right to parent.
    def borrow_from_right(self, node,  index) :
        child = node.arr[index]
        sibling = node.arr[index + 1]
        #  node key is inserted as the last key in child.
        child.keys[child.n] = node.keys[index]
        #  Sibling's first child is inserted as the last child of child.
        if (not (child.leaf)) : 
            child.arr[(child.n) + 1] = sibling.arr[0]
        # First key from sibling is inserted into node.
        node.keys[index] = sibling.keys[0]
        #  Moving all keys in sibling one step left
        i = 1
        while (i < sibling.n) :
            sibling.keys[i - 1] = sibling.keys[i]    
            i += 1
        #  Moving the child pointers one step behind
        i = 1
        while (not sibling.leaf and i <= sibling.n) :
            sibling.arr[i - 1] = sibling.arr[i]    
            i += 1
        #  Increase child key count and decrease sibling key count.
        child.n += 1
        sibling.n -= 1
        return

    #  Merge node's children at index and index+1.
    def merge(self, node,  index) :
        left = node.arr[index]
        right = node.arr[index + 1]
        start = left.n
        #  Adding a key from node to the left child.
        left.keys[start] = node.keys[index]
        #  Copying the keys from right to left.
        i = 0
        while (i < right.n) :
            left.keys[start + 1 + i] = right.keys[i]    
            i += 1
        #  Copying the child pointers from right to left.
        i = 0
        while (not left.leaf and i <= right.n) :
            left.arr[start + 1 + i] = right.arr[i]    
            i += 1
        #  Moving all keys after  index in the current node one step forward.
        i = index + 1
        while (i < node.n) :
            node.keys[i - 1] = node.keys[i]    
            i += 1
        #  Moving the child pointers after (index+1) in the current node one step forward.
        i = index + 2
        while (i <= node.n) :
            node.arr[i - 1] = node.arr[i]    
            i += 1
        #  Updating the key count of child and the current node
        left.n += right.n + 1
        node.n -= 1
        return

t = BTree(3)
#  A B-Tree with max key 3
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(7)
t.insert(8)
t.insert(9)
t.insert(10)
t.print_tree()
print("6 : " + ("Present" if (t.search(6) != None) else "Not Present"))
print("11 : " + ("Present" if (t.search(11) != None) else "Not Present"))
t.remove(6)
t.remove(3)
t.remove(7)
t.print_tree()
"""
         key[ 0 ]: 1
     key[ 0 ]: 2
         key[ 0 ]: 3
 key[ 0 ]: 4
         key[ 0 ]: 5
     key[ 0 ]: 6
         key[ 0 ]: 7
     key[ 1 ]: 8
         key[ 0 ]: 9
         key[ 1 ]: 10

6 : Present
11 : Not Present
     key[ 0 ]: 1
     key[ 1 ]: 2
 key[ 0 ]: 4
     key[ 0 ]: 5
 key[ 1 ]: 8
     key[ 0 ]: 9
     key[ 1 ]: 10

"""