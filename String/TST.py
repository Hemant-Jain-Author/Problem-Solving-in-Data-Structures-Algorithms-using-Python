class TST(object):
    class Node(object):
        def __init__(self, d, isLast = False):
            self.data = d
            self.is_last_char = isLast
            self.left = self.equal = self.right = None

    def __init__(self):
        self.root = None
        
    def insert(self, word):
        self.root = self.insert_util(self.root, word, 0)

    def insert_util(self, curr, word, word_index):
        if curr == None:
            curr = self.Node(word[word_index])
        if word[word_index] < curr.data:
            curr.left = self.insert_util(curr.left, word, word_index)
        elif word[word_index] > curr.data:
            curr.right = self.insert_util(curr.right, word, word_index)
        else:
            if word_index < len(word) - 1:
                curr.equal = self.insert_util(curr.equal, word, word_index + 1)
            else:
                curr.is_last_char = True
        return curr

    def find_util(self, curr, word, word_index):
        if curr == None:
            return False
        if word[word_index] < curr.data:
            return self.find_util(curr.left, word, word_index)
        elif word[word_index] > curr.data:
            return self.find_util(curr.right, word, word_index)
        else:
            if word_index == len(word) - 1:
                return curr.is_last_char
            return self.find_util(curr.equal, word, word_index + 1)

    def find(self, word):
        ret = self.find_util(self.root, word, 0)
        return ret

# Testing code.
t = TST()
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