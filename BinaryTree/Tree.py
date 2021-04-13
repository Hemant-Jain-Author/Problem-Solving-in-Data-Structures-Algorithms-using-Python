from collections import deque
import math
import sys

class Tree(object):
    class Node(object):
        def __init__(self, v, l=None, r=None):
            self.value = v
            self.lChild = l
            self.rChild = r

    def __init__(self):
        self.root = None

    def level_order_binary_tree(self, arr):
        self.root = self.level_order_binary_tree_util(arr, 0)

    def level_order_binary_tree_util(self, arr, start):
        size = len(arr)
        curr = self.Node(arr[start])
        left = 2 * start + 1
        right = 2 * start + 2
        if left < size:
            curr.lChild = self.level_order_binary_tree_util(arr, left)
        if right < size:
            curr.rChild = self.level_order_binary_tree_util(arr, right)
        return curr

    def add(self, value):
        self.root = self.add_util(self.root, value)

    def add_util(self, node, value):
        if node == None:
            node = self.Node(value)
        else:
            if node.value > value:
                node.lChild = self.add_util(node.lChild, value)
            else:
                node.rChild = self.add_util(node.rChild, value)
        return node


    def print_pre_order(self):
        self.print_pre_order_util(self.root)
        print()


    def print_pre_order_util(self, node):
        # pre order  
        if node != None:
            print(node.value, end=' ')
            self.print_pre_order_util(node.lChild)
            self.print_pre_order_util(node.rChild)

    def nth_pre_order(self, index):
        count = [0] 
        self.nth_pre_order_util(self.root, index, count)

    def nth_pre_order_util(self, node, index, count):
        # pre order  
        if node != None:
            count[0] += 1
            if count[0] == index:
                print(node.value, end=' ')
            self.nth_pre_order_util(node.lChild, index, count)
            self.nth_pre_order_util(node.rChild, index, count)


    def print_post_order(self):
        self.print_post_order_util(self.root)
        print()

    def print_post_order_util(self, node):
        # post order  
        if node != None:
            self.print_post_order_util(node.lChild)
            self.print_post_order_util(node.rChild)
            print(node.value, end=' ')


    def nth_post_order(self, index):
        count = [0]
        self.nth_post_order_util(self.root, index, count)

    def nth_post_order_util(self, node, index, count):
        # post order  
        if node != None:
            self.nth_post_order_util(node.lChild, index, count)
            self.nth_post_order_util(node.rChild, index, count)
            count[0] += 1
            if count[0] == index:
                print(node.value, end=' ')


    def print_in_order(self):
        self.print_in_order_util(self.root)
        print()


    def print_in_order_util(self, node):
        # In order  
        if node != None:
            self.print_in_order_util(node.lChild)
            print(node.value, end=' ')
            self.print_in_order_util(node.rChild)


    def nth_in_order(self, index):
        count = [0]
        self.nth_in_order_util(self.root, index, count)


    def nth_in_order_util(self, node, index, count):
        if node != None:
            self.nth_in_order_util(node.lChild, index, count)
            count[0] += 1
            if count[0] == index:
                print(node.value, end=' ')
            self.nth_in_order_util(node.rChild, index, count)

    def print_breadth_first(self):
        que = deque([])
        temp = None
        if self.root != None:
            que.append(self.root)
        while len(que) != 0:
            temp = que.popleft()
            print(temp.value, end=' ')
            if temp.lChild != None:
                que.append(temp.lChild)
            if temp.rChild != None:
                que.append(temp.rChild)

    def print_depth_first(self):
        stk = []
        if self.root != None:
            stk.append(self.root)
        
        while len(stk) != 0:
            temp = stk.pop()
            print(temp.value, end=' ')
            if temp.rChild != None:
                stk.append(temp.rChild)            
            if temp.lChild != None:
                stk.append(temp.lChild)


    def find(self, value):
        curr = self.root
        while curr != None:
            if curr.value == value:
                return True
            elif curr.value > value:
                curr = curr.lChild
            else:
                curr = curr.rChild
        return False


    def find_min(self):
        node = self.root
        if node == None:
            raise RuntimeError("ListEmptyException")
        while node.lChild != None:
            node = node.lChild
        return node.value


    def find_max(self):
        node = self.root
        if node == None:
            raise RuntimeError("ListEmptyException")
        while node.rChild != None:
            node = node.rChild
        return node.value

    def find_max_util(self, curr):
        node = curr
        if node == None:
            return None
        while node.rChild != None:
            node = node.rChild
        return node

    def find_min_util(self, curr):
        node = curr
        if node == None:
            return None
        while node.lChild != None:
            node = node.lChild
        return node

    def free(self):
        self.root = None

    def delete_node(self, value):
        self.root = self.delete_node_util(self.root, value)

    def delete_node_util(self, node, value):
        temp = None
        if node != None:
            if node.value == value:
                if node.lChild == None and node.rChild == None:
                    return None
                else:
                    if node.lChild == None:
                        temp = node.rChild
                        return temp
                    if node.rChild == None:
                        temp = node.lChild
                        return temp
                    maxnode = self.find_max_util(node.lChild)
                    node.value = maxnode.value
                    node.lChild = self.delete_node_util(node.lChild, maxnode.value)
            else:
                if node.value > value:
                    node.lChild = self.delete_node_util(node.lChild, value)
                else:
                    node.rChild = self.delete_node_util(node.rChild, value)
        return node


    def tree_depth(self):
        return self.tree_depth_util(self.root)

    def tree_depth_util(self, root):
        if root == None:
            return 0
        else:
            lDepth = self.tree_depth_util(root.lChild)
            rDepth = self.tree_depth_util(root.rChild)
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1

    def is_equal(self, T2):
        return self.is_equal(self.root, T2.root)

    def is_equal(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            return (self.is_equal(node1.lChild, node2.lChild) and self.is_equal(node1.rChild, node2.rChild) and (node1.value == node2.value))


    def ancestor(self, first, second):
        if first > second:
            temp = first
            first = second
            second = temp
        curr = self.ancestor_util(self.root, first, second)
        if curr == None:
            retval = sys.maxsize
        else :
            retval = curr.value
        return retval

    def ancestor_util(self, curr, first, second):
        if curr == None:
            return None
        if curr.value > first and curr.value > second:
            return self.ancestor_util(curr.lChild, first, second)
        if curr.value < first and curr.value < second:
            return self.ancestor_util(curr.rChild, first, second)
        return curr


    def copy_tree(self):
        tree2 = Tree()
        tree2.root = self.copy_tree_util(self.root)
        return tree2

    def copy_tree_util(self, curr):
        if curr != None:
            temp = self.Node(curr.value)
            temp.lChild = self.copy_tree_util(curr.lChild)
            temp.rChild = self.copy_tree_util(curr.rChild)
            return temp
        else:
            return None


    def copy_mirror_tree(self):
        tree2 = Tree()
        tree2.root = self.copy_mirror_tree_util(self.root)
        return tree2

    def copy_mirror_tree_util(self, curr):
        if curr != None:
            temp = self.Node(curr.value)
            temp.rChild = self.copy_mirror_tree_util(curr.lChild)
            temp.lChild = self.copy_mirror_tree_util(curr.rChild)
            return temp
        else:
            return None


    def num_nodes(self):
        return self.num_nodes_util(self.root)

    def num_nodes_util(self, curr):
        if curr == None:
            return 0
        else:
            return (1 + self.num_nodes_util(curr.rChild) + self.num_nodes_util(curr.lChild))


    def num_full_nodes_bt(self):
        return self.num_full_nodes_bt_util(self.root)

    def num_full_nodes_bt_util(self, curr):
        if curr == None:
            return 0
        count = self.num_full_nodes_bt_util(curr.rChild) + self.num_full_nodes_bt_util(curr.lChild)
        if curr.rChild != None and curr.lChild != None:
            count += 1
        return count


    def max_length_path_bt(self):
        return self.max_length_path_bt_util(self.root)

    def max_length_path_bt_util(self, curr):
        # diameter
        if curr == None:
            return 0
        leftPath = self.tree_depth_util(curr.lChild)
        rightPath = self.tree_depth_util(curr.rChild)
        maxpath = leftPath + rightPath + 1
        leftMax = self.max_length_path_bt_util(curr.lChild)
        rightMax = self.max_length_path_bt_util(curr.rChild)
        if leftMax > maxpath:
            maxpath = leftMax
        if rightMax > maxpath:
            maxpath = rightMax
        return maxpath


    def num_leaf_nodes(self):
        return self.num_leaf_nodes_util(self.root)

    def num_leaf_nodes_util(self, curr):
        if curr == None:
            return 0
        if curr.lChild == None and curr.rChild == None:
            return 1
        else:
            return (self.num_leaf_nodes_util(curr.rChild) + self.num_leaf_nodes_util(curr.lChild))


    def sum_all_bt(self):
        return self.sum_all_bt_util(self.root)

    def sum_all_bt_util(self, curr):
        if curr == None:
            return 0
        rightSum = self.sum_all_bt_util(curr.rChild)
        leftSum = self.sum_all_bt_util(curr.lChild)
        finalsum = rightSum + leftSum + curr.value
        return finalsum

    def iterative_pre_order(self):
        stk = []
        if self.root != None:
            stk.append(self.root)
        while len(stk) != 0:
            curr = stk.pop()
            print(curr.value, end=' ')
            if curr.rChild != None:
                stk.append(curr.rChild)
            if curr.lChild != None:
                stk.append(curr.lChild)

def iterative_post_order(self):
    stk = []
    visited = []
    if self.root != None:
        stk.append(self.root)
        visited.append(0)
    while len(stk) != 0:
        curr = stk.pop()
        vtd = visited.pop()
        if vtd == 1:
            print(curr.value, end=' ')
        else:
            stk.append(curr)
            visited.append(1)                
            if curr.rChild != None:
                stk.append(curr.rChild)
                visited.append(0)
            if curr.lChild != None:
                stk.append(curr.lChild)
                visited.append(0)

    def iterative_in_order(self):
        stk = []
        visited = []
        if self.root != None:
            stk.append(self.root)
            visited.append(0)
        while len(stk) != 0:
            curr = stk.pop()
            vtd = visited.pop()
            if vtd == 1:
                print(curr.value, end=' ')
            else:
                if curr.rChild != None:
                    stk.append(curr.rChild)
                    visited.append(0)
                stk.append(curr)
                visited.append(1)
                if curr.lChild != None:
                    stk.append(curr.lChild)
                    visited.append(0)

    def is_bst3(self):
        return self.is_bst3_util(self.root)


    def is_bst3_util(self, root):
        if root == None:
            return True
        if root.lChild != None and self.find_max_util(root.lChild).value > root.value:
            return False
        if root.rChild != None and self.find_min_util(root.rChild).value <= root.value:
            return False
        return (self.is_bst3_util(root.lChild) and self.is_bst3_util(root.rChild))


    def is_bst(self):
        return self.is_bst_util(self.root, -999999, 999999)

    def is_bst_util(self, curr, minval, maxval):
        if curr == None:
            return True
        if curr.value < minval or curr.value > maxval:
            return False
        return self.is_bst_util(curr.lChild, minval, curr.value) and self.is_bst_util(curr.rChild, curr.value, maxval)


    def is_bst2(self):
        count = [0]
        return self.is_bst2_util(self.root, count)

    def is_bst2_util(self, curr, count):
        #   in order  traversal 
        ret = bool()
        if curr != None:
            ret = self.is_bst2_util(curr.lChild, count)
            if not ret:
                return False
            if count[0] > curr.value:
                return False
            count[0] = curr.value
            ret = self.is_bst2_util(curr.rChild, count)
            if not ret:
                return False
        return True

        
    def print_all_path(self):
        stk = []
        self.print_all_path_util(self.root, stk)

    def print_all_path_util(self, curr, stk):
        if curr == None:
            return
        stk.append(curr.value)
        if curr.lChild == None and curr.rChild == None:
            print(stk)
            stk.pop()
            return
        self.print_all_path_util(curr.rChild, stk)
        self.print_all_path_util(curr.lChild, stk)
        stk.pop()


    def lca(self, first, second):
        ans = self.lca_util(self.root, first, second)
        if ans != None:
            return ans.value
        else:
            return sys.maxsize

    def lca_util(self, curr, first, second):
        if curr == None:
            return None
        if curr.value == first or curr.value == second:
            return curr
        left = self.lca_util(curr.lChild, first, second)
        right = self.lca_util(curr.rChild, first, second)
        if left != None and right != None:
            return curr
        elif left != None:
            return left
        else:
            return right


    def lca_bst(self, first, second):
        if first > second:
            first, second = second, first
        curr = self.lca_bst_util(self.root, first, second)
        if(curr == None):
            print("LCA does not exist")
        else:
            print("LCA is :", curr.value) 

    def lca_bst_util(self, curr, first, second):
        if curr == None:
            return None
        if curr.value > second:
            return self.lca_bst_util(curr.lChild, first, second)
        if curr.value < first:
            return self.lca_bst_util(curr.rChild, first, second)
        if self.find(first) and self.find(second):
            return curr
        return None


    def trim_outside_range(self, minval, maxval):
        self.trim_outside_range_util(self.root, minval, maxval)

    def trim_outside_range_util(self, curr, minval, maxval):
        if curr == None:
            return None
        curr.lChild = self.trim_outside_range_util(curr.lChild, minval, maxval)
        curr.rChild = self.trim_outside_range_util(curr.rChild, minval, maxval)
        if curr.value < minval:
            return curr.rChild
        if curr.value > maxval:
            return curr.lChild
        return curr


    def print_in_range(self, minval, maxval):
        self.print_in_range_util(self.root, minval, maxval)
        print()

    def print_in_range_util(self, root, minval, maxval):
        if root == None:
            return
        self.print_in_range_util(root.lChild, minval, maxval)
        if root.value >= minval and root.value <= maxval:
            print(root.value, end=' ')
        self.print_in_range_util(root.rChild, minval, maxval)

    def floor_bst(self, val):
        curr = self.root
        floor = sys.maxsize
        while curr != None:
            if curr.value == val:
                floor = curr.value
                break
            elif curr.value > val:
                curr = curr.lChild
            else:
                floor = curr.value
                curr = curr.rChild
        return floor

    def ceil_bst(self, val):
        curr = self.root
        ceil = -1 * (sys.maxunicode)
        while curr != None:
            if curr.value == val:
                ceil = curr.value
                break
            elif curr.value > val:
                ceil = curr.value
                curr = curr.lChild
            else:
                curr = curr.rChild
        return ceil


    def find_max_bt(self):
        return self.find_max_bt_util(self.root)

    def find_max_bt_util(self, curr):
        if curr == None:
            return -1 * sys.maxsize
        maxval = curr.value
        left = self.find_max_bt_util(curr.lChild)
        right = self.find_max_bt_util(curr.rChild)
        if left > maxval:
            maxval = left
        if right > maxval:
            maxval = right
        return maxval

    def search_bt(self, value):
        return self.search_bt_util(self.root, value)

    def search_bt_util(self, root, value):
        if root == None:
            return False
        if root.value == value:
            return True
        left = self.search_bt_util(root.lChild, value)
        if left:
            return True
        right = self.search_bt_util(root.rChild, value)
        if right:
            return True
        return False


    def create_binary_tree(self, arr):
        self.root = self.create_binary_tree_util(arr, 0, len(arr)-1)

    def create_binary_tree_util(self, arr, start, end):
        if start > end:
            return None
        mid = math.floor((start + end) / 2)
        curr = self.Node(arr[mid])
        curr.lChild = self.create_binary_tree_util(arr, start, mid - 1)
        curr.rChild = self.create_binary_tree_util(arr, mid + 1, end)
        return curr

    def tree_to_list(self):
        return self.tree_to_list_rec(self.root)

    def tree_to_list_rec(self, curr):
        if curr == None:
            return None        
        if curr.lChild == None and curr.rChild == None:
            curr.lChild = curr
            curr.rChild = curr
            return curr
        if curr.lChild != None:
            head = self.tree_to_list_rec(curr.lChild)
            tail = head.lChild
            curr.lChild = tail
            tail.rChild = curr
        else:
            head = curr
            
        if curr.rChild != None:
            temp_head = self.tree_to_list_rec(curr.rChild)
            tail = temp_Head.lChild
            curr.rChild = temp_head
            temp_head.lChild = curr
        else:
            tail = curr
        
        head.lChild = tail
        tail.rChild = head
        return head

    def level_order_binary_tree(self, arr):
        self.root = self.level_order_binary_tree_util(arr, 0)

    def level_order_binary_tree_util(self, arr, start):
        size = len(arr)
        curr = self.Node(arr[start])
        left = 2 * start + 1
        right = 2 * start + 2
        if left < size:
            curr.lChild = self.level_order_binary_tree_util(arr, left)
        if right < size:
            curr.rChild = self.level_order_binary_tree_util(arr, right)
        return curr

    def print_breadth_first(self):
        que = deque([])
        output = []
        temp = None
        if self.root != None:
            que.append(self.root)
        while len(que) != 0:
            temp = que.popleft()
            output.append(temp.value)
            if temp.lChild != None:
                que.append(temp.lChild)
            if temp.rChild != None:
                que.append(temp.rChild)
        print(output)

    def print_level_order_linebyline(self):
        que1 = deque([])
        que2 = deque([])
        temp = None
        if self.root != None:
            que1.append(self.root)
        while len(que1) != 0 or len(que2) != 0 :
            while len(que1) != 0:
                temp = que1.popleft()
                print(temp.value, end=" ")
                if temp.lChild != None:
                    que2.append(temp.lChild)
                if temp.rChild != None:
                    que2.append(temp.rChild)
            print("")
            while len(que2) != 0:
                temp = que2.popleft()
                print(temp.value, end=" ")
                if temp.lChild != None:
                    que1.append(temp.lChild)
                if temp.rChild != None:
                    que1.append(temp.rChild)
            print("")

    def print_level_order_linebyline2(self):
        que = deque([])
        temp = None
        if self.root != None:
            que.append(self.root)
        while len(que) != 0 :
            count = len(que)
            while count > 0:
                temp = que.popleft()
                print (temp.value, end=" ")
                if temp.lChild != None:
                    que.append(temp.lChild)
                if temp.rChild != None:
                    que.append(temp.rChild)
                count -= 1
            print("")

    def print_spiral_tree(self):
        stk1 = []
        stk2 = []
        output = []
        temp = None
        if self.root != None:
            stk1.append(self.root)
        while len(stk1) !=0 or len(stk2) != 0:
            while len(stk1) != 0:
                temp = stk1.pop()
                output.append(temp.value)
                if temp.rChild != None:
                    stk2.append(temp.rChild)
                if temp.lChild != None:
                    stk2.append(temp.lChild)

            while len(stk2) != 0:
                temp = stk2.pop()
                output.append(temp.value)
                if temp.lChild != None:
                    stk1.append(temp.lChild)
                if temp.rChild != None:
                    stk1.append(temp.rChild)
        print(output)

    """
    To see if tree is a heap we need to check two conditions:
    1) It is a complete tree.
    2) Value of a node is grater than or equal to it's left and right child.
    """
    def find_count_util(self, curr):
        if curr == None:
            return 0
        return (1 + self.find_count_util(curr.lChild) + self.find_count_util(curr.rChild))

    def find_count(self):
        return self.find_count_util(self.root)

    def is_complete_tree_util(self, curr, index, count):
        if curr == None:
            return True
        if index > count:
            return False 
        return self.is_complete_tree_util(curr.lChild, index*2+1, count) and self.is_complete_tree_util(curr.rChild, index*2+2, count)

    def is_complete_tree(self):
        count = self.find_count()
        return self.is_complete_tree_util(self.root, 0, count)

    def is_complete_tree2(self):
        que = deque([])
        temp = None
        noChild = False
        if self.root != None:
            que.append(self.root)
        while len(que) != 0:
            temp = que.popleft()
            if temp.lChild != None:
                if noChild == True:
                    return False
                que.append(temp.lChild)
            else:
                noChild = True

            if temp.rChild != None:
                if noChild == True:
                    return False
                que.append(temp.rChild)
            else:
                noChild = True
        return True

    def is_heap_util(self, curr, parentValue):
        if curr == None:
            return True
        if curr.value < parentValue:
            return False
        return ( self.is_heap_util(curr.lChild, curr.value) and self.is_heap_util(curr.rChild, curr.value ))

    def is_heap(self):
        infi = -9999999
        return self.is_complete_tree() and self.is_heap_util(self.root, infi)


    def is_heap_util2(self, curr, index, count, parentValue):
        if curr == None:
            return True
        if index > count:
            return False
        if curr.value < parentValue:
            return False 
        return self.is_heap_util2(curr.lChild, index*2+1, count, curr.value) and self.is_heap_util2(curr.rChild, index*2+2, count, curr.value)

    def is_heap2(self):
        count = self.find_count()
        parentValue = -9999999
        return self.is_heap_util2(self.root, 0, count, parentValue)

    def is_heap3(self):
        que = deque([])
        que.append(self.root)
        que.append(0)
        que.append(-99999)
        count = 0
        while len(que) != 0:
            curr = que.popleft()
            currIndex = que.popleft()
            parentValue = que.popleft()

            if curr.value < parentValue or currIndex != count :
                return False
            count += 1
            if curr.lChild != None :
                que.append(curr.lChild)
                que.append(currIndex * 2 + 1)
                que.append(curr.value)
            
            if curr.rChild != None :
                que.append(curr.rChild)
                que.append(currIndex * 2 + 2)
                que.append(curr.value)

        return True



#=======================================================================
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t = Tree()
    t.level_order_binary_tree(arr)
    t.print_pre_order()
    # 1 2 4 8 9 5 10 3 6 7 

    t.print_post_order()
    # 8 9 4 10 5 2 6 7 3 1 

    t.print_in_order()
    # 8 4 9 2 10 5 1 6 3 7 

    t.print_breadth_first()
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    t.print_depth_first()
    # 1 2 4 8 9 5 10 3 6 7

    t.print_level_order_linebyline()
    """
    1 
    2 3 
    4 5 6 7 
    8 9 10 
    """

    t.print_level_order_linebyline2()
    """
    1 
    2 3 
    4 5 6 7 
    8 9 10
    """
    t.print_spiral_tree()
    # [1, 2, 3, 7, 6, 5, 4, 8, 9, 10]

    t.nth_in_order(2)
    t.nth_post_order(2)
    t.nth_pre_order(2)
    """
    4 
    9 
    2 
    """

    t.print_all_path()
    """
    [1, 3, 7]
    [1, 3, 6]
    [1, 2, 5, 10]
    [1, 2, 4, 9]
    [1, 2, 4, 8]
    """

    print(t.num_nodes())
    # 10

    print(t.sum_all_bt())
    # 55

    print(t.num_leaf_nodes())
    # 5

    print(t.num_full_nodes_bt())
    # 4

    print(t.search_bt(9))  
    # True

    print(t.find_max_bt())
    # 10

    print(t.tree_depth())
    # 4

    print(t.max_length_path_bt())
    # 6

    t2 = t.copy_tree()
    #
    print("Printing original tree")
    t.print_level_order_linebyline()
    """
    Printing original tree
    1 
    2 3 
    4 5 6 7 
    8 9 10 
    """

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t = Tree()
    t.level_order_binary_tree(arr)

    t.print_level_order_linebyline()
    t2 = t.copy_mirror_tree()
    t2.print_level_order_linebyline()
    """
    1 
    2 3 
    4 5 6 7 
    8 9 10 

    1 
    3 2 
    7 6 5 4 
    10 9 8 
    """

    print("Printing mirror tree")
    t2.print_level_order_linebyline()
    """
    Printing mirror tree
    1 
    2 3 
    4 5 6 7 
    8 9 10 
    """
    print(t.is_equal(t2))
    # True

    print(t.is_complete_tree())
    # True

    print(t.is_complete_tree2())
    # True

    print(t.is_heap())
    print(t.is_heap2())
    print(t.is_heap3())

    """
    True
    True
    True
    """

    # l = t.tree_to_list()
    # l.PrintDLL()	

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t = Tree()
    t.create_binary_tree(arr)
    t.iterative_in_order()
    # 1 2 3 4 5 6 7 8 9 10 

    t = Tree()
    t.add(2)
    t.add(1)
    t.add(3)
    t.add(4)
    t.print_in_order()
    # 1 2 3 4
    print(t.find(3))
    print(t.find(6))
    """
    True
    False
    1
    4
    """
    t = Tree()
    t.add(2)
    t.add(1)
    t.add(3)
    t.add(4)
    print(t.find_min())
    print(t.find_max())
    """
    1
    4
    """

    t = Tree()
    t.add(2)
    t.add(1)
    t.add(3)
    t.add(4)
    print(t.is_bst())
    print(t.is_bst2())
    print(t.is_bst3())
    """
    True
    True
    True
    """

    t = Tree()
    t.add(2)
    t.add(1)
    t.add(3)
    t.add(4)
    print("Before delete operation.")
    t.print_in_order()
    t.delete_node(2)
    print("After delete operation.")
    t.print_in_order()
    """
    Before delete operation.
    1 2 3 4 
    After delete operation.
    1 3 4 
    """

    t = Tree()
    t.add(2)
    t.add(1)
    t.add(3)
    t.add(4)
    t.lca_bst(3, 4)
    t.lca_bst(1, 4)
    t.lca_bst(10, 4)
    """
    LCA is : 3
    LCA is : 2
    LCA does not exist
    """

def main2():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t = Tree()
    t.create_binary_tree(arr)

    t.print_in_range(4, 7)
    # 4 5 6 7 

    t.trim_outside_range(4, 7)
    t.print_in_order()
    # 4 5 6 7 

    print(t.ancestor(1, 10))
    # 5


    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t = Tree()
    t.create_binary_tree(arr)    
    print(t.ceil_bst(5.5))
    # 6

    print(t.floor_bst(8))
    # 8

def main3():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t = Tree()
    t.create_binary_tree(arr)
    t.iterative_in_order()
    t.iterative_pre_order()
    t.iterative_post_order()

        print ( t.lca(10, 3) )
    """
    1 2 3 4 5 6 7 8 9 10 
    5 2 1 3 4 8 6 7 9 10 
    1 4 3 2 7 6 10 9 8 5 
    5
    """


def is_bst_array(preorder):
    size = len(preorder)
    stk = []
    root = -999999
    i = 0
    while i < size :
        value = preorder[i]
        # If value of the right child is less than root.
        if (value < root):
            return False
        # First left child values will be popped
        # Last popped value will be the root.
        while (len(stk) > 0 and stk[len(stk) - 1] < value) :
            root = stk.pop()
        
        # add current value to the stack.
        stk.append(value)
        i += 1

    return True



def main4():
    arr = [5, 2, 4, 6, 9, 10]
    print(is_bst_array(arr))

    arr = [5, 2, 6, 4, 7, 9, 10]
    print(is_bst_array(arr))

"""
True
False
"""

#main()
#main2()
#main3()
#main4()


"""
Given an array. Construct an output array which 
the number of elements on the right side which are smaller 
then elements of given array.
"""
"""
Simple solution is by using two loops. One for picking element and 
another loop for finding other elements which are smaller then it.
O(n2)

An another efficient solution is to use balanced BST.
Traverse from right to left put values in tree. 
The nodes of the tree will keep track the number of elements 
in its left child or nodes which have value less than it.
so finding nodes which have value less than it is O(logn) this step 
will be repeted for all the nodes. so complexity will be O(nlogn)

"""
