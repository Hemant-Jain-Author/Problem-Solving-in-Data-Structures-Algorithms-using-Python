
class Polynomial(object):
        # Node class representing elements of linked list.
    class Node:
        def __init__(self, c, p, n=None):
            self.coeff = c
            self.pow = p
            self.next = n
            
    # Constructor of Polynomial.
    def __init__(self, coeffs=None, pows=None, size=0):
        self.head = None
        tail=None
        temp=None
        for i in range(size) :
            temp = self.Node(coeffs[i], pows[i])
            if(self.head == None):
                self.head = tail = temp
            else :
                tail.next = temp
                tail=tail.next

    def add(self, poly2):
        poly = Polynomial()
        p1 = self.head
        p2 = poly2.head

        while (p1 != None or p2 != None) :
            if (p1 == None or p1.pow < p2.pow) :
                temp = self.Node(p2.coeff, p2.pow)
                p2 = p2.next
            elif (p2 == None or p1.pow > p2.pow) :
                temp = self.Node(p1.coeff, p1.pow)
                p1 = p1.next
            elif (p1.pow == p2.pow) :
                temp = self.Node(p1.coeff + p2.coeff, p1.pow)
                p1 = p1.next
                p2 = p2.next

            if(poly.head == None):
                poly.head = tail = temp
            else :
                tail.next = temp
                tail=tail.next
        return poly


    def print(self) :
        head = self.head
        while (head != None) :
            print(head.coeff, end="")
            if(head.pow != 0) :
                print("x^"+ str(head.pow), end="")
            
            if (head.next != None) :
                print(" + ", end="")
            head = head.next


# Testing code.
c1 = [6, 5, 4]
p1 = [2, 1, 0]
s1 = 3
first = Polynomial(c1, p1, s1)

c2 = [3, 2, 1]
p2 = [3, 1, 0]
s2 = 3 
second = Polynomial(c2, p2, s2)
    
sum = first.add(second)
sum.print()

"""
3x^3 + 6x^2 + 7x^1 + 5
"""