import math
import sys

class RmqST :
    def __init__(self, input) :
        self.n = len(input)
        #  Height of segment tree.
        x = math.ceil(math.log(self.n) / math.log(2))
        # Maximum size of segment tree
        max_size = 2 * int(math.pow(2,x)) - 1
        #  Allocate memory for segment tree
        self.segarray = [0] * (max_size)
        self.construct_segtree(input, 0, self.n - 1, 0)

    def construct_segtree(self, input,  start,  end,  index) :
        #  Store it in current node of the segment tree and return
        if (start == end) :
            self.segarray[index] = input[start]
            return  input[start]
        #  If there are more than one elements, 
        #  then traverse left and right subtrees 
        #  and store the minimum of values in current node.
        mid = int((start + end) / 2)
        self.segarray[index] = min(self.construct_segtree(input, start, mid, index * 2 + 1), self.construct_segtree(input, mid + 1, end, index * 2 + 2))
        return  self.segarray[index]


    def get_min(self, start,  end) :
        #  Check for error conditions.
        if (start > end or start < 0 or end > self.n - 1) :
            print("Invalid Input.")
            return  sys.maxsize
        return  self.get_min_util(0, self.n - 1, start, end, 0)

    def get_min_util(self, seg_start,  seg_end,  query_start,  query_end,  index) :
        if (query_start <= seg_start and seg_end <= query_end) : #  complete overlapping case.
            return  self.segarray[index]
        if (seg_end < query_start or query_end < seg_start) : #  no overlapping case.
            return  sys.maxsize
        #  Segment tree is partly overlaps with the query range.
        mid = int((seg_start + seg_end) / 2)
        return  min(self.get_min_util(seg_start, mid, query_start, query_end, 2 * index + 1),
                self.get_min_util(mid + 1, seg_end, query_start, query_end, 2 * index + 2))

    def update(self, ind,  val) :
        #  Check for error conditions.
        if (ind < 0 or ind > self.n - 1) :
            print("Invalid Input.")
            return
        #  Update the values in segment tree
        self.update_util(0, self.n - 1, ind, val, 0)

    #  Always min inside valid range will be returned.
    def update_util(self, seg_start,  seg_end,  ind,  val,  index) :
        #  Update index lies outside the range of current segment.
        #  So minimum will not change.
        if (ind < seg_start or ind > seg_end) :
            return  self.segarray[index]
        #  If the input index is in range of this node, then update the
        #  value of the node and its children
        if (seg_start == seg_end) :
            if (seg_start == ind) :
                #  Index value need to be updated.
                self.segarray[index] = val
                return  val
            else :
                return  self.segarray[index]
        mid = int((seg_start + seg_end) / 2)
        #  Current node value is updated with min. 
        self.segarray[index] = min(self.update_util(seg_start, mid, ind, val, 2 * index + 1), self.update_util(mid + 1, seg_end, ind, val, 2 * index + 2))
        #  Value of diff is propagated to the parent node.
        return  self.segarray[index]


# Testing Code
arr = [2, 3, 1, 7, 12, 5]
tree = RmqST(arr)
print("Min value in the range(1, 5): " + str(tree.get_min(1, 5)))
print("Min value of all the elements: " + str(tree.get_min(0, len(arr) - 1)))
tree.update(2, -1)
print("Min value in the range(1, 5): " + str(tree.get_min(1, 5)))
print("Min value of all the elements: " + str(tree.get_min(0, len(arr) - 1)))
tree.update(5, -2)
print("Min value in the range(0, 4): " + str(tree.get_min(0, 4)))
print("Min value of all the elements: " + str(tree.get_min(0, len(arr) - 1)))

"""
Min value in the range(1, 5): 1
Min value of all the elements: 1
Min value in the range(1, 5): -1
Min value of all the elements: -1
Min value in the range(0, 4): -1
Min value of all the elements: -2
"""
