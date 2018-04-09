#!/usr/bin/env python
class StringTree(object):
    class Node(object):
        def __init__(self, v, cnt=1, l=None, r=None):
            self.value = v
            self.count = cnt
            self.lChild = l
            self.rChild = r
    
    def __init__(self):
        self.root = None

    # Other Methods. 
    def printTree(self):
        self.printTreeUtil(self.root)

    def printTreeUtil(self, curr):
        #  pre order 
        if curr != None:
            print("[",curr.value, ":" , curr.count,"]")
            self.printTreeUtil(curr.lChild)
            self.printTreeUtil(curr.rChild)

    
    def insert(self, value):
        self.root = self.insertUtil(value, self.root)


    def insertUtil(self, value, curr):
        if curr == None:
            curr = self.Node(value)
        else:
            compare = self.strcmp(curr.value, value)
            if compare == 0:
                curr.count += 1
            elif compare == 1:
                curr.lChild = self.insertUtil(value, curr.lChild)
            else:
                curr.rChild = self.insertUtil(value, curr.rChild)
        return curr

    def strcmp(self, first, second):
        if(first == second):
            return 0
        elif(first < second):
            return 1
        else:
            return -1
        
    def freeTree(self):
        self.root = None

    
    def find(self, value):
        ret = self.findUtil(self.root, value)
        print(value , "found::" , ret)
        return ret

    def findUtil(self, curr, value):
        if curr == None:
            return False
        compare = self.strcmp(curr.value, value)
        if compare == 0:
            return True
        elif compare == 1:
            return self.findUtil(curr.lChild, value)
        else:
            return self.findUtil(curr.rChild, value)

    
    def frequency(self, value):
        return self.frequencyUtil(self.root, value)

    def frequencyUtil(self, curr, value):
        if curr == None:
            return 0
        compare = self.strcmp(curr.value, value)
        if compare == 0:
            return curr.count
        elif compare > 0:
            return self.frequencyUtil(curr.lChild, value)
        else:
            return self.frequencyUtil(curr.rChild, value)



tt = StringTree()
tt.insert("banana")
tt.insert("apple")
tt.insert("mango")
tt.insert("banana")
tt.insert("apple")
tt.insert("mango")
tt.find("apple")
tt.find("banana")
tt.find("mango")
tt.find("banan")
tt.find("appletree")
tt.find("grapes")

tt.printTree()
print("apple::" , tt.frequency("apple"))
print("banana::" , tt.frequency("banana"))
print("mango::" , tt.frequency("mango"))
print("android::" , tt.frequency("android"))

