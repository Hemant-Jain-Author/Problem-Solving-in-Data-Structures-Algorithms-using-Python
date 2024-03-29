class DoublyCircularLinkedList(object):
    class Node(object):
        def __init__(self, v, nxt=None, prv=None):
            self.value = v
            self.next = nxt
            self.prev = prv
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.head == None

    def peek_head(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        return self.head.value

    def add_head(self, value):
        new_node = self.Node(value, None, None)
        self.count += 1
        if self.head == None:
            self.tail = self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev = new_node
            new_node.prev.next = new_node
            self.head = new_node


    def add_tail(self, value):
        new_node = self.Node(value, None, None)
        self.count += 1
        if self.head == None:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.tail.next
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next.prev = new_node
            self.tail = new_node


    def remove_head(self):
        if self.head == None:
            raise RuntimeError("EmptyListException")
        
        self.count -= 1
        value = self.head.value
        
        if self.head == self.head.next:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        
        next_node = self.head.next
        next_node.prev = self.tail
        self.tail.next = next_node
        self.head = next_node
        return value

    def remove_tail(self):
        if self.count == 0:
            raise RuntimeError("EmptyListException")
        
        self.count -= 1
        value = self.tail.value
        
        if self.count == 0:
            self.head = None
            self.tail = None
            return value
        
        prev = self.tail.prev
        prev.next = self.head
        self.head.prev = prev
        self.tail = prev
        return value

    def search (self, key):
        temp = self.head
        if self.head == None:
            return False

        for i in range(self.size()) :
            if temp.value == key:
                return True
            temp = temp.next
            
        return False

    def free(self):
        self.head = None
        self.tail = None
        self.count = 0

    def print(self):
        if self.is_empty():
            return
        temp = self.tail.next
        while temp != self.tail:
            print(temp.value, end=' ')
            temp = temp.next
        print(temp.value)
            
            
# Testing Code
def test1():
    ll = DoublyCircularLinkedList()
    ll.add_head(1)
    ll.add_head(2)
    ll.add_head(3)
    print(ll.size())
    ll.print()

"""
3
3 2 1
"""

def test2():
    ll = DoublyCircularLinkedList()
    ll.add_tail(1)
    ll.add_tail(2)
    ll.add_tail(3)
    ll.print()

"""
1 2 3
"""

# Testing Code
def test3():
    ll = DoublyCircularLinkedList()
    ll.add_head(1)
    ll.add_head(2)
    ll.add_head(3)
    ll.print()
    ll.remove_head()
    ll.print()

"""
3 2 1
2 1
"""

# Testing Code
def test4():
    ll = DoublyCircularLinkedList()
    ll.add_head(1)
    ll.add_head(2)
    ll.add_head(3)
    ll.print()
    ll.remove_tail()
    ll.print()

"""
3 2 1
3 2
"""

test1()
test2()
test3()
test4()
