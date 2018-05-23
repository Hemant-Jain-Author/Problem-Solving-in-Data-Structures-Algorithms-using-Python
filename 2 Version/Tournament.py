"""Find second minimum value in an array efficiently the soulution should be done in 
less then (2n-3) comparisions.
"""
import math
def createTournamentTree(arr):
    size = len(arr)
    tree = [0]*(2*size - 1)
    links = [0]*(2*size - 1)
    for i in range(size - 1,2*size - 1,1):
        tree[i] = arr[i - (size - 1)]
        links[i] = i

    last = 2*size - 2
    second = last - 1
    while last >=0 and second >= 0:
        parent = last / 2 - 1
        if tree[last] < tree[second]:
            tree[parent] = tree[last]
            links[parent] = links[last]
        else :
            tree[parent] = tree[second]
            links[parent] = links[second]
        last -= 2;
        second -= 2
    print tree
    print links

    first = tree[0]
    index = links[0]
    print first
    tree[index] = 99999
    parent = index/2 -1
    if index % 2 == 0 :
        sibling = index - 1
    else :
        sibling = index + 1

    while parent >= 0:
        tree[parent] = tree [sibling]
        links[] 
         


input = [1,2,3,4,5]
createTournamentTree(input)
