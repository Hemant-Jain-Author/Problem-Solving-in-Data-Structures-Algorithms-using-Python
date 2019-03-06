
def isMaxHeap2(arr):
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


def isMaxHeap(arr):
    size = len(arr)
    parent = 0
    #last element index size - 1
    for parent in range(size/2 + 1):
        lchild = parent*2 + 1
        rchild = parent*2 + 2
        # heap property check.
        if ((lchild < size) and (arr[parent] < arr[lchild])) or ((rchild < size) and (arr[parent] < arr[rchild])) :
            return False
    return True

def isMinHeap(arr):
    size = len(arr)
    parent = 0
    #last element index size - 1
    for parent in range(size/2 + 1):
        lchild = parent*2 + 1
        rchild = parent*2 + 2
        # heap property check.
        if ((lchild < size) and (arr[parent] > arr[lchild])) or ((rchild < size) and (arr[parent] > arr[rchild])) :
            return False
    return True


	size = len(arr)
	parent = 0
	#last element index size - 1
	while(parent <= size/2):
		if 2*i + 1 < size:
			if arr[i] > arr[2*i + 1]:
                111
				return False
		if 2*i + 2 < size:
			if arr[i] > arr[2*i +2]:
				return False
		i += 1
	return True


arr = [8,7,6,5,7,5,2.1]
print isMaxHeap(arr)