class CircularLinkedList(object):
    class Node(object):
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    def __init__(self):
        self.tail = None
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.tail == None

    def peek(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        return self.tail.next.value

    def add_tail(self, value):
        temp = self.Node(value, None)
        self.count += 1
        if self.tail == None:
            self.tail = temp
            temp.next = temp
        else:
            temp.next = self.tail.next
            self.tail.next = temp
            self.tail = temp
        

    def add_head(self, value):
        temp = self.Node(value, None)
        self.count += 1
        if self.tail == None:
            self.tail = temp
            temp.next = temp
        else:
            temp.next = self.tail.next
            self.tail.next = temp

    def remove_head(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        self.count -= 1
        value = self.tail.next.value
        if self.tail == self.tail.next:
            self.tail = None
        else:
            self.tail.next = self.tail.next.next
        return value

    def remove_node(self, key):
        if self.is_empty():
            return False
        self.count -= 1
        curr = self.tail.next
        head = self.tail.next
        if curr.value == key:
            #  head and single node case.
            if curr == curr.next:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next
            return True
        prev = curr
        curr = curr.next
        while curr != head:
            if curr.value == key:
                if curr == self.tail:
                    self.tail = prev
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def copy_list_reversed(self):
        cl = CircularLinkedList()
        curr = self.tail.next
        head = curr
        if curr != None:
            cl.add_head(curr.value)
            curr = curr.next
        while curr != head:
            cl.add_head(curr.value)
            curr = curr.next
        return cl

    def copy_list(self):
        cl = CircularLinkedList()
        curr = self.tail.next
        head = curr
        if curr != None:
            cl.add_tail(curr.value)
            curr = curr.next
        while curr != head:
            cl.add_tail(curr.value)
            curr = curr.next
        return cl

    def search (self, data):
        temp = self.tail
        for i in range(self.size()) :
            if temp.value == data:
                return True
            temp = temp.next
        return False

    def free(self):
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
    ll = CircularLinkedList()
    ll.add_head(1)
    ll.add_head(2)
    ll.add_head(3)
    ll.print()
    print("Search:", ll.search(2))
    print("Search:", ll.search(4))
    ll.remove_head()
    ll.print()

"""
3 2 1
Search: True
Search: False
2 1
"""

# Testing Code
def test2():
    ll = CircularLinkedList()
    ll.add_tail(1)
    ll.add_tail(2)
    ll.add_tail(3)
    ll.print()

"""
1 2 3
"""


# Testing Code
def test3():
    ll = CircularLinkedList()
    ll.add_head(1)
    ll.add_head(2)
    ll.add_head(3)
    ll.print()
    ll.remove_node(2)
    ll.print()


"""
3 2 1
3 1
"""


# Testing Code
def test4():
    ll = CircularLinkedList()
    ll.add_head(1)
    ll.add_head(2)
    ll.add_head(3)
    ll.print()

    ll2 = ll.copy_list()
    ll2.print()

    ll3 = ll.copy_list_reversed()
    ll3.print()

"""
3 2 1 
3 2 1
1 2 3
"""
test1()
test2()
test3()
test4()