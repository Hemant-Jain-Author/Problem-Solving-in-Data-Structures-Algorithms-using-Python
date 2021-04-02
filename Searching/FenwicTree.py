"""
Start from index+1 if you updating index in original array. Keep adding this value 
for next node till you reach outside range of tree
"""
def update_util(binary_indexed_tree, val, index):
    size = len(binary_indexed_tree)
    while index < size:
        binary_indexed_tree[index] += val
        index = get_next(index)

def update(binary_indexed_tree, diff, index):
    update_util(binary_indexed_tree, diff, index+1)

"""
Start from index+1 if you want prefix sum 0 to index. Keep adding value
till you reach 0
"""
def get_sum(binary_indexed_tree, index):
    index = index + 1
    sum = 0
    while index > 0 :
        sum += binary_indexed_tree[index]
        index = get_parent(index)
    return sum

def get_range_sum(binary_indexed_tree, first, second):
    index = first
    first_sum = 0
    while index > 0 :
        first_sum += binary_indexed_tree[index]
        index = get_parent(index)
        
    index = second + 1
    second_sum = 0
    while index > 0 :
        second_sum += binary_indexed_tree[index]
        index = get_parent(index)
    return (second_sum - first_sum)

"""
Creating tree is like updating Fenwick tree for every value in array
"""
def create_tree(input):
    size = len(input)
    binary_indexed_tree = [0]*(size+1)
    for i in range(size) :
        update_util(binary_indexed_tree, input[i], i+1)
    return binary_indexed_tree

"""
To get parent
1) Boolean AND (2's complement of index) with index
2) Subtract the result from index
"""
def get_parent(index):
    return index - (index & -index)

"""
To get next
1) Boolean AND (2's complement of index) with index
2) Add the result to index
"""
def get_next(index):
    return index + (index & -index)

input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
binary_indexed_tree = create_tree(input)
for i in range(len(input)):
    print(get_sum(binary_indexed_tree, i))
    print(get_range_sum(binary_indexed_tree, 0, i))

print(get_range_sum(binary_indexed_tree, 8, 8))