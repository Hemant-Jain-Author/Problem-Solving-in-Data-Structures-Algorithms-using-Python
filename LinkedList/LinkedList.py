class LinkedList(object):
    # Node class representing elements of linked list.
    class Node:
        def __init__(self, v, n=None):
            self.value = v
            self.next = n
            
    # Constructor of linked list.
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        return self.head.value

    def add_head(self, value):
        self.head = self.Node(value, self.head)
        self.size += 1

    def add_tail(self, value):
        new_node = self.Node(value, None)
        curr = self.head
        if self.head == None:
            self.head = new_node
            return
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.size += 1

    def remove_head(self):
        if self.is_empty():
            raise RuntimeError("EmptyListException")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def is_present(self, data):
        temp = self.head
        while temp != None:
            if temp.value == data:
                return True
            temp = temp.next
        return False

    def delete_node(self, delValue):
        temp = self.head
        if self.is_empty():
            return False
        if delValue == self.head.value:
            self.head = self.head.next
            self.size -= 1
            return True
        while temp.next != None:
            if temp.next.value == delValue:
                temp.next = temp.next.next
                self.size -= 1
                return True
            temp = temp.next
        return False

    def delete_nodes(self, delValue):
        currNode = self.head
        while currNode != None and currNode.value == delValue:
            # first node 
            self.head = currNode.next
            currNode = self.head
            self.size -= 1
        while currNode != None:
            next_node = currNode.next
            if next_node != None and next_node.value == delValue:
                currNode.next = next_node.next
                self.size -= 1
            else:
                currNode = next_node

    def reverse_recurse_util(self, currentNode, next_node):
        if currentNode == None:
            return None
        if currentNode.next == None:
            currentNode.next = next_node
            return currentNode
        ret = self.reverse_recurse_util(currentNode.next, currentNode)
        currentNode.next = next_node
        return ret

    def reverse_recurse(self):
        self.head = self.reverse_recurse_util(self.head, None)

    def reverse(self):
        curr = self.head
        prev = None
        while curr != None:
            nextval = curr.next
            curr.next = prev
            prev = curr
            curr = nextval
        self.head = prev

    def copy_list_reversed(self):
        temp_node = None
        curr = self.head
        while curr != None:
            temp_node2 = self.Node(curr.value, temp_node)
            curr = curr.next
            temp_node = temp_node2
        ll2 = LinkedList()
        ll2.head = temp_node
        return ll2

    def copy_list(self):
        curr = self.head
        if curr == None:
            return None
        tailNode = headNode = self.Node(curr.value, None)
        curr = curr.next
        while curr != None:
            temp_node = self.Node(curr.value, None)
            tailNode.next = temp_node
            tailNode = temp_node
            curr = curr.next
        ll2 = LinkedList()
        ll2.head = headNode
        return ll2


    def compare_list(self, ll):
        return self.compare_list_util(self.head, ll.head)

    def compare_list_util(self, head1, head2):
        if head1 == None and head2 == None:
            return True
        elif (head1 == None) or (head2 == None) or (head1.value != head2.value):
            return False
        else:
            return self.compare_list_util(head1.next, head2.next)

    def compare_list2(self, ll2):
        head1 = self.head
        head2 = ll2.head

        while head1 != None and head2 != None:
            if head1.value != head2.value:
                return False
            head1 = head1.next
            head2 = head2.next

        if head1 == None and head2 == None:
            return True
        return False

    def length(self):
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next
        return count

    def nth_node_from_begining(self, index):
        if index > self.length() or index < 1:
            raise RuntimeError("IndexOutOfRange")
        count = 1
        curr = self.head
        while curr != None and count < index:
            count += 1
            curr = curr.next
        return curr.value


    def nth_node_from_end(self, index):
        if self.size != 0 and self.size < index:
            raise RuntimeError("IndexOutOfRange")
        startIndex = self.size - index + 1
        return self.nth_node_from_begining(startIndex)

    def nth_node_from_end2(self, index):
        count = 1
        forward = self.head
        curr = self.head
        while forward != None and count <= index:
            count += 1
            forward = forward.next
        if forward == None:
            raise RuntimeError("IndexOutOfRange")
        while forward != None:
            forward = forward.next
            curr = curr.next
        return curr.value

    def find_intersection(self, head, head2):
        l1 = 0
        l2 = 0
        tempHead = head
        tempHead2 = head2
        while tempHead != None:
            l1 += 1
            tempHead = tempHead.next
        while tempHead2 != None:
            l2 += 1
            tempHead2 = tempHead2.next
        diff = int()
        if l1 < 12:
            temp = head
            head = head2
            head2 = temp
            diff = l2 - l1
        else:
            diff = l1 - l2
        while diff > 0:
            head = head.next
            diff -= 1
        while head != head2:
            head = head.next
            head2 = head2.next
        return head

    def free(self):
        self.head = None
        self.size = 0

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next
        print("")

    def sorted_insert(self, value):
        new_node = self.Node(value, None)
        curr = self.head
        if curr == None or curr.value > value:
            new_node.next = self.head
            self.head = new_node
            return
        while curr.next != None and curr.next.value < value:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def remove_duplicate(self):
        curr = self.head
        while curr != None:
            if curr.next != None and curr.value == curr.next.value:
                curr.next = curr.next.next
            else:
                curr = curr.next

    def make_loop(self):
        temp = self.head
        while temp != None:
            if temp.next == None:
                temp.next = self.head
                return
            temp = temp.next

    def loop_detect(self):
        slowPtr = fastPtr = self.head
        while fastPtr.next != None and fastPtr.next.next != None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                print("loop found")
                return True
        print("loop not found")
        return False

    def reverse_list_loop_detect(self):
        tempHead = self.head
        self.reverse()
        if tempHead == self.head:
            self.reverse()
            print("loop found")
            return True
        else:
            self.reverse()
            print("loop not found")
            return False

    def loop_type_detect(self):
        slowPtr = fastPtr = self.head
        while fastPtr.next != None and fastPtr.next.next != None:
            if self.head == fastPtr.next or self.head == fastPtr.next.next:
                print("circular list loop found")
                return 2
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                print("loop found")
                return 1
        print("loop not found")
        return 0

    def loop_point_detect(self):
        slowPtr = fastPtr = self.head
        while fastPtr.next != None and fastPtr.next.next != None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                return slowPtr
        return None

    def remove_loop(self):
        loopPoint = self.loop_point_detect()
        if loopPoint == None:
            raise RuntimeError("LoopNotFound")
        firstPtr = self.head
        if loopPoint == self.head:
            while firstPtr.next != self.head:
                firstPtr = firstPtr.next;
            firstPtr.next = None
            return
        secondPtr = loopPoint
        while firstPtr.next != secondPtr.next:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next
        secondPtr.next = None



ll = LinkedList()
ll.add_head(1)
ll.add_head(2)
ll.add_head(3)
ll.add_head(4)
ll.print()

print(ll.compare_list2(ll))
"""
4 3 2 1 
True
"""
# ll.sorted_insert(1)
# ll.sorted_insert(2)
# ll.sorted_insert(3)
# ll.sorted_insert(5)
# ll.sorted_insert(0)
# ll.print()
# ll.make_loop()
# print(ll.loop_detect())
# print(ll.loop_type_detect())
# print(ll.loop_point_detect().value)
# print(ll.reverse_list_loop_detect())
# print(ll.remove_loop())

#=======================================================================
# print ll.is_empty()
#=======================================================================
#=======================================================================
# print ll.is_empty()
# print ll.peek()
# print ll.remove_head()
# ll.print()
#=======================================================================
#=======================================================================
# print ll.is_present(5)
# print ll.is_present(2)
# ll.remove_duplicate()
# print ll.is_empty()
# ll.delete_nodes(3)
#=======================================================================
#=======================================================================
# ll.reverse()
# ll.print()
# ll.reverse_recurse()
# ll.print()
#=======================================================================
#=======================================================================
# ll3 = ll.copy_list_reversed()
# ll3.print()
#  
# ll2 = ll.copy_list()
# ll2.print()
# print ll.length()
#=======================================================================
#=======================================================================
# print ll.nth_node_from_begining(2)
# print ll.nth_node_from_end(2)
# print ll.nth_node_from_end2(2)
#=======================================================================

      
