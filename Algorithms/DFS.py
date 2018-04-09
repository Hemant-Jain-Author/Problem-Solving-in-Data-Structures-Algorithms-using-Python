def DFS(head):
    curr = head
    count = 0;
    while (curr !=  None & curr.visited == False):
        count += 1
        if (curr.lChild != None & curr.lChild.visited == False):
            curr= curr.lChild
        elif (curr.rChild != None & curr.rChild.visited == False):
            curr= curr.rChild;
        else:
            print (curr.value)
            curr.visited = 1;
            curr = head;

    print("count is : ", count)