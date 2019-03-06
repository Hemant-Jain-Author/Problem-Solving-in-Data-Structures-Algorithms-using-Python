"""
In preorder traversal <Root><Left child><Right child>. 
Once we have a value grater then root value then we are in Right child subtree. 
So all the nodes that will come will have value grater then root value.
"""
def isBSTArray(preorder):
    stk = []
    root = -99999
    for value in preorder:
        # If value of the right child is less then root.
        if value < root :
            return False
        # First left child values will be popped
        # Last popped value will be the root.
        while(len(stk) > 0 and stk[-1] < value) :
            root = stk.pop()
        # add current value to the stack.
        stk.append(value)
    return True
 
preorder1 = [30 , 20 , 25 , 70 , 200]
print ("Is BST Array" , isBSTArray(preorder1) )
preorder2 = [30 , 20 , 25 , 10 , 70 , 200]
print ("Is BST Array" , isBSTArray(preorder2) )
preorder3 = [30 , 20 , 35 , 30 ]
print ("Is BST Array" , isBSTArray(preorder3) )
preorder4 = [30 , 20 , 35 , 29 ]
print ("Is BST Array" , isBSTArray(preorder4) )