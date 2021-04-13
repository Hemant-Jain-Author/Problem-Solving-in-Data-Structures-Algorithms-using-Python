class Trie(object):
    class Node(object):
        CharCount = 26
        
        def __init__(self, c, isLast = False):
            self.child = [None] * (self.CharCount)
            self.isLastChar = isLast
            self.ch = c

    def __init__(self):
        self.root = self.Node(' ')
        #  first node with dummy value.
    
    def insert(self, token):
        if token == None:
            return self.root
        return self.insert_util(self.root, token.lower(), 0)

    def insert_util(self, curr, token, index):
        if curr == None:
            curr = self.Node(token[index - 1])
        if index == len(token):
            curr.isLastChar = True
        else:
            curr.child[ord(token[index]) - ord('a')] = self.insert_util(curr.child[ord(token[index]) - ord('a')], token, index + 1)
        return curr

    
    def remove(self, token):
        if token == None:
            return
        token = token.lower()
        self.remove_util(self.root, token, 0)

    def remove_util(self, curr, token, index):
        if curr == None:
            return
        if index == len(token):
            if curr.isLastChar:
                curr.isLastChar = False
            return
        self.remove_util(curr.child[ord(token[index]) - ord('a')], token, index + 1)
    
    def find(self, token):
        if token == None:
            return False
        token = token.lower()
        return self.find_util(self.root, token, 0)

    def find_util(self, curr, token, index):
        if curr == None:
            return False
        if index == len(token):
            return curr.isLastChar
        return self.find_util(curr.child[ord(token[index]) - ord('a')], token, index + 1)

# Testing code.
t = Trie()
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
