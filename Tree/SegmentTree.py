import math

class SegmentTree :
    def __init__(self, input) :
        self.size = len(input)
        #  Height of segment tree.
        x = math.ceil(math.log(self.size) / math.log(2))
        # Maximum size of segment tree
        max_size = 2 * int(math.pow(2,x)) - 1
        #  Allocate memory for segment tree
        self.segarray = [0] * (max_size)
        self.construct_segtree(input, 0, self.size - 1, 0)

    def construct_segtree(self, input,  start,  end,  index) :
        #  Store it in current node of the segment tree and return
        if (start == end) :
            self.segarray[index] = input[start]
            return  input[start]
        #  If there are more than one elements, 
        #  then traverse left and right subtrees 
        #  and store the sum of values in current node.
        mid = (start + end) // 2
        self.segarray[index] = self.construct_segtree(input, start, mid, index * 2 + 1) + self.construct_segtree(input, mid + 1, end, index * 2 + 2)
        return  self.segarray[index]

    def get_sum(self, start,  end) :
        #  Check for error conditions.
        if (start > end or start < 0 or end > self.size - 1) :
            print("Invalid Input.")
            return  -1
        return  self.get_sum_util(0, self.size - 1, start, end, 0)

    def get_sum_util(self, seg_start,  seg_end,  query_start,  query_end,  index) :
        if (query_start <= seg_start and seg_end <= query_end) : #  complete overlapping case.
            return  self.segarray[index]
        if (seg_end < query_start or query_end < seg_start) : #  no overlapping case.
            return  0
        #  Segment tree is partly overlaps with the query range.
        mid = (seg_start + seg_end) // 2
        return  self.get_sum_util(seg_start, mid, query_start, query_end, 2 * index + 1) + \
            self.get_sum_util(mid + 1, seg_end, query_start, query_end, 2 * index + 2)
        
    def set(self, arr,  ind,  val) :
        #  Check for error conditions.
        if (ind < 0 or ind > self.size - 1) :
            print("Invalid Input.")
            return
        arr[ind] = val
        #  Set new value in segment tree
        self.set_util(0, self.size - 1, ind, val, 0)

    #  Always diff will be returned.
    def set_util(self, seg_start,  seg_end,  ind,  val,  index) :
        #  set index lies outside the range of current segment.
        #  So diff to its parent node will be zero.
        if (ind < seg_start or ind > seg_end) :
            return  0
        #  If the input index is in range of this node, then set the
        #  value of the node and its children
        if (seg_start == seg_end) :
            if (seg_start == ind) :
                #  Index that need to be set.
                diff = val - self.segarray[index]
                self.segarray[index] = val
                return  diff
            else :
                return  0
        mid = (seg_start + seg_end) // 2
        diff = self.set_util(seg_start, mid, ind, val, 2 * index + 1) + self.set_util(mid + 1, seg_end, ind, val, 2 * index + 2)
        #  Current node value is set with diff. 
        self.segarray[index] = self.segarray[index] + diff
        #  Value of diff is propagated to the parent node.
        return  diff

arr = [1, 2, 4, 8, 16, 32, 64]
tree = SegmentTree(arr)
print("Sum of values in the range(0, 3): " + str(tree.get_sum(1, 3)))
print("Sum of values of all the elements: " + str(tree.get_sum(0, len(arr) - 1)))
tree.set(arr, 1, 10)
print("Sum of values in the range(0, 3): " + str(tree.get_sum(1, 3)))
print("Sum of values of all the elements: " + str(tree.get_sum(0, len(arr) - 1)))

"""
Sum of values in the range(0, 3): 14
Sum of values of all the elements: 127
Sum of values in the range(0, 3): 22
Sum of values of all the elements: 135
"""