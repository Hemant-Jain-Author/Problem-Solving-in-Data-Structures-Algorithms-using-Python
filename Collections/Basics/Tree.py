class Tree(object):
    class Node(object):
        def __init__(self, v, l=None, r=None):
            self.value = v
            self.lChild = l
            self.rChild = r       
        #  Nested Class Node other fields and methods.    

    def __init__(self):
        self.root = None
    #  Outer Class Tree other fields and methods.
