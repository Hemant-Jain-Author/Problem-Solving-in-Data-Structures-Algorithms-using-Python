"""
Given an array. Construct an output array which 
the number of elements on the right side which are smaller 
then elements of given array.
"""
Simple solution is by using two loops. One for picking element and 
another loop for finding other elements which are smaller then it.
O(n2)

An another efficient solution is to use balanced BST.
Traverse from right to left put values in tree. 
The nodes of the tree will keep track the number of elements in its left child or 
nodes which have value less than it.
so finding nodes which have value less than it is O(logn) this step will be repeted 
for all the nodes. so complexity will be O(nlogn)


