class StringTree(object):
    class Node(object):
        def __init__(self, v, cnt=1, l=None, r=None):
            self.value = v
            self.count = cnt
            self.left = l
            self.right = r
    
    def __init__(self):
        self.root = None

    # Other Methods. 
    def print_tree(self):
        self.print_tree_util(self.root)

    def print_tree_util(self, curr):
        #  pre order 
        if curr != None:
            print("[", curr.value, ":", curr.count, "]")
            self.print_tree_util(curr.left)
            self.print_tree_util(curr.right)
    
    def insert(self, value):
        self.root = self.insert_util(value, self.root)

    def insert_util(self, value, curr):
        if curr == None:
            curr = self.Node(value)
        else:
            compare = self.strcmp(curr.value, value)
            if compare == 0:
                curr.count += 1
            elif compare == 1:
                curr.left = self.insert_util(value, curr.left)
            else:
                curr.right = self.insert_util(value, curr.right)
        return curr

    def strcmp(self, first, second):
        if(first == second):
            return 0
        elif(first < second):
            return 1
        else:
            return -1
        
    def free(self):
        self.root = None
    
    def find(self, value):
        ret = self.find_util(self.root, value)
        return ret

    def find_util(self, curr, value):
        if curr == None:
            return False
        compare = self.strcmp(curr.value, value)
        if compare == 0:
            return True
        elif compare == 1:
            return self.find_util(curr.left, value)
        else:
            return self.find_util(curr.right, value)
    
    def frequency(self, value):
        return self.frequency_util(self.root, value)

    def frequency_util(self, curr, value):
        if curr == None:
            return 0
        compare = self.strcmp(curr.value, value)
        if compare == 0:
            return curr.count
        elif compare > 0:
            return self.frequency_util(curr.left, value)
        else:
            return self.frequency_util(curr.right, value)

# Testing code.
t = StringTree()
t.insert("banana")
t.insert("apple")
t.insert("mango")
print("Apple Found:", t.find("apple"))
print("Grapes Found:", t.find("grapes"))
print("Banana Found:", t.find("banana"))

"""
Apple Found: True
Grapes Found: False
Banana Found: True
"""