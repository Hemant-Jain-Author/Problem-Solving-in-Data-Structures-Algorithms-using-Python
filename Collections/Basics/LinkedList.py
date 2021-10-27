class LinkedList(object):
    class Node(object):
        def __init__(self, v, n=None):
            self.value = v
            self.next = n


    def __init__(self):
        self.head = None
