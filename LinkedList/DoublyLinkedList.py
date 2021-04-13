class DoublyLinkedList(object):
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
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        return self.head.value

    def add_head(self, value):
        self.count += 1
        if self.head == None:
            self.tail = self.head = self.Node(value, None, None)
        else:
            new_node = self.Node(value, self.head, None)
            self.head.prev = new_node
            self.head = new_node


    def add_tail(self, value):
        new_node = self.Node(value, None, None)
        self.count += 1
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        self.count -= 1
        value = self.head.value
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    def remove_node(self, key):
        curr = self.head
        if curr == None:
            return False # empty list
        
        if curr.value == key:
            # head is the node with value key.
            self.head = self.head.next
            if self.head != None:
                self.head = None
            else:
                self.tail = None
            #  only one element in list.
            self.count -= 1
            return True
        while curr.next != None:
            if curr.next.value == key:
                curr.next = curr.next.next
                if curr.next == None:
                    self.tail = curr
                else:
                    curr.next = curr
                self.count -= 1
                return True
            curr = curr.next
        return False

    def is_present(self, key):
        temp = self.head
        while temp != None:
            if temp.value == key:
                return True
            temp = temp.next
        return False

    def free(self):
        self.head = None
        self.tail = None
        self.count = 0

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next
        print("")

    # SORTED INSERT DECREASING
    def sorted_insert(self, value):
        temp = self.Node(value)
        curr = self.head
        self.count += 1
        if curr == None:
            # first element
            self.head = temp
            self.tail = temp
            return
            
        if self.head.value <= value: # at the begining  
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
            return

        while curr.next != None and curr.next.value > value: # treversal
            curr = curr.next
        
        if curr.next == None: # at the end
            self.tail = temp
            temp.prev = curr
            curr.next = temp
        else:                 # all other
            temp.next = curr.next
            temp.prev = curr
            curr.next = temp
            temp.next.prev = temp


    # Reverse a doubly linked List iteratively
    def reverse_list(self):
        curr = self.head
        temp_node = self.Node()
        while curr != None:
            temp_node = curr.next
            curr.next = curr.prev
            curr.prev = temp_node
            if curr.prev == None:
                self.tail = self.head
                self.head = curr
                return
            curr = curr.prev
        return

    #   Remove Duplicate 
    def remove_duplicate(self):
        curr = self.head
        deleteMe = self.Node()
        while curr != None:
            if (curr.next != None) and curr.value == curr.next.value:
                deleteMe = curr.next
                curr.next = deleteMe.next
                curr.next.prev = curr
                if deleteMe == self.tail:
                    self.tail = curr
            else:
                curr = curr.next

    def copy_list_reversed(self):
        dll = DoublyLinkedList()
        curr = self.head
        while curr != None:
            dll.add_head(curr.value)
            curr = curr.next
        return dll

    def copy_list(self):
        dll = DoublyLinkedList()
        curr = self.head
        while curr != None:
            dll.add_tail(curr.value)
            curr = curr.next
        return dll



ll = DoublyLinkedList()
ll.add_head(1)
ll.add_head(2)
ll.add_head(3)
ll.add_head(4)
ll.print()
ll.remove_head()
ll.print()
ll2 = ll.copy_list()
ll2.print()
ll3 = ll.copy_list_reversed()
ll3.print()
"""
4 3 2 1 
3 2 1 
3 2 1 
1 2 3 
"""