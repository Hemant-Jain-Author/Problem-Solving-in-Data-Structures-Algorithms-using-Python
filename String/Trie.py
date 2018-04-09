#!/usr/bin/env python
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
    
    def Insert(self, token):
        if token == None:
            return self.root
        return self.InsertUtil(self.root, token.lower(), 0)

    def InsertUtil(self, curr, token, index):
        if curr == None:
            curr = self.Node(token[index - 1])
        if index == len(token):
            curr.isLastChar = True
        else:
            curr.child[ord(token[index]) - ord('a')] = self.InsertUtil(curr.child[ord(token[index]) - ord('a')], token, index + 1)
        return curr

    
    def Remove(self, token):
        if token == None:
            return
        token = token.lower()
        self.RemoveUtil(self.root, token, 0)

    def RemoveUtil(self, curr, token, index):
        if curr == None:
            return
        if index == len(token):
            if curr.isLastChar:
                curr.isLastChar = False
            return
        self.RemoveUtil(curr.child[ord(token[index]) - ord('a')], token, index + 1)
    
    def Find(self, token):
        if token == None:
            return False
        token = token.lower()
        return self.FindUtil(self.root, token, 0)

    def FindUtil(self, curr, token, index):
        if curr == None:
            return False
        if index == len(token):
            return curr.isLastChar
        return self.FindUtil(curr.child[ord(token[index]) - ord('a')], token, index + 1)

t = Trie()
a = "apple"
b = "app"
c = "appletree"
d = "tree"
t.Insert(a)
t.Insert(d)
print t.Find(a)
print t.Find(b)
print t.Find(c)
print t.Find(d)
