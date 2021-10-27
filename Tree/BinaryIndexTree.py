
class BinaryIndexTree :
    def __init__(self, arr) :
        self.size = len(arr)
        self.bit = [0] * (self.size + 1) #  Populating bit. 
        for i in range(self.size) :
            self.update(i, arr[i])    
    
    def set(self, arr,  index,  val) :
        diff = val - arr[index]
        arr[index] = val
        #  Difference is propagated.
        self.update(index, diff)

    def update(self, index,  val) :
        #  Index in bit is 1 more than the input list.
        index = index + 1
        #  Traverse to ancestors of nodes.
        while (index <= self.size) :
            #  Add val to current node of Binary Index Tree.
            self.bit[index] += val
            #  Next element which need to store val.
            index += index & (-index)
    
    #  Range sum in the range start to end.
    def range_sum(self, start,  end) :
        #  Check for error conditions.
        if (start > end or start < 0 or end > self.size - 1) :
            print("Invalid Input.")
            return  -1
        return  self.prefix_sum(end) - self.prefix_sum(start - 1)

    #  Prefix sum in the range 0 to index.
    def prefix_sum(self, index) :
        sum = 0
        index = index + 1
        #  Traverse ancestors of Binary Index Tree nodes.
        while (index > 0) :
            #  Add current element to sum.
            sum += self.bit[index]
            #  Parent index calculation.
            index -= index & (-index)
        return  sum


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tree = BinaryIndexTree(arr)
print("Sum of elements in range(0, 5): " + str(tree.prefix_sum(5)))
print("Sum of elements in range(2, 5): " + str(tree.range_sum(2, 5)))
tree.set(arr, 3, 10) #  Set fourth element to 10.
#  Find sum after the value is updated
print("Sum of elements in range(0, 5): " + str(tree.prefix_sum(5)))

"""
Sum of elements in range(0, 5): 21
Sum of elements in range(2, 5): 18
Sum of elements in range(0, 5): 27
"""