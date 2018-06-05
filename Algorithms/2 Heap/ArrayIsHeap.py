
def isMaxHeap(arr):
    size = len(arr)
    parent = (size/2 - 1)
    while parent >= 0:
        lchild = parent*2 + 1
        rchild = parent*2 + 2
        # heap property check.
        # rchild can overflow.
        if ( arr[parent] < arr[lchild] ) or ( rchild < size - 1 and arr[parent] < arr[rchild]):
            return False
        parent -= 1
    return True

arr = [8,7,6,5,7,7,2.1]
print isMaxHeap(arr)