#!/usr/bin/env python
class TST(object):
    class Node(object):
        def __init__(self, d, isLast = False):
            self.data = d
            self.isLastChar = isLast
            self.left = self.equal = self.right = None

    def __init__(self):
        self.root = None
        
    def insert(self, word):
        self.root = self.insertUtil(self.root, word, 0)

    def insertUtil(self, curr, word, wordIndex):
        if curr == None:
            curr = self.Node(word[wordIndex])
        if word[wordIndex] < curr.data:
            curr.left = self.insertUtil(curr.left, word, wordIndex)
        elif word[wordIndex] > curr.data:
            curr.right = self.insertUtil(curr.right, word, wordIndex)
        else:
            if wordIndex < len(word) - 1:
                curr.equal = self.insertUtil(curr.equal, word, wordIndex + 1)
            else:
                curr.isLastChar = True
        return curr

    def findUtil(self, curr, word, wordIndex):
        if curr == None:
            return False
        if word[wordIndex] < curr.data:
            return self.findUtil(curr.left, word, wordIndex)
        elif word[wordIndex] > curr.data:
            return self.findUtil(curr.right, word, wordIndex)
        else:
            if wordIndex == len(word) - 1:
                return curr.isLastChar
            return self.findUtil(curr.equal, word, wordIndex + 1)

    def find(self, word):
        ret = self.findUtil(self.root, word, 0)
        print word , " :: ",
        if ret:
            print " Found "
        else:
            print "Not Found "
        return ret

tt = TST()
tt.insert("banana")
tt.insert("apple")
tt.insert("mango")
print "Search apple, banana, grapes and mango :"
tt.find("apple")
tt.find("banana")
tt.find("mango")
tt.find("grapes")
