#!/usr/bin/env python
import heapq
import sys
from collections import deque

class Graph(object):
    class Edge(object):
        def __init__(self, dst, cst=1):
            self.destination = dst
            self.cost = cst
            self.next = None

    def __init__(self, cnt):
        self.count = cnt
        self.array = [None] * cnt
        i = 0
        while i < cnt:
            self.array[i] = None
            i += 1
    
    def AddDirectedEdge(self, source, destination, cost=1):
        node = self.Edge(destination, cost)
        node.next = self.array[source]
        self.array[source] = node
    
    def AddUndirectedEdge(self, source, destination, cost=1):
        self.AddDirectedEdge(source, destination, cost)
        self.AddDirectedEdge(destination, source, cost)

    def Print(self):
        i = 0
        while i < self.count:
            ad = self.array[i]
            if ad != None:
                print "Vertex " , i , " is connected to : ",
                while ad != None:
                    print ad.destination ,
                    ad = ad.next
                print("")
            i += 1

class PriorityQueue(object):
    def __init__(self):
        self.pQueue = []
        self.count = 0
    
    def Add(self, key, value):
        heapq.heappush(self.pQueue, (key, value))
    
    def UpdateKey(self, key, value):
        heapq.heappush(self.pQueue, (key, value))

    def Pop(self):
        val = heapq.heappop(self.pQueue)
        return val

    def Size(self):
        return len(self.pQueue)
    

def Dijkstra(gph, source):
    previous = [-1] * gph.count
    dist = [sys.maxsize] * gph.count
    visited = [False] * gph.count

    dist[source] = 0
    previous[source] = -1
    pq = PriorityQueue()
    for i in range(gph.count):
        pq.Add(sys.maxint, i)
    pq.UpdateKey(0, source)
    
    while pq.Size() != 0:
        val = pq.Pop()
        source = val[1]
        curr = gph.array[source]
        visited[source] = True
        
        while curr != None:
            alt = curr.cost + dist[source]
            if alt < dist[curr.destination] and visited[curr.destination] == False:
                dist[curr.destination] = alt
                previous[curr.destination] = source
                pq.UpdateKey(alt, curr.destination)
            curr = curr.next
    
    for i in range(gph.count):
        if dist[i] == sys.maxsize:
            print("node id" , i , "prev" , previous[i] , "distance : Unreachable")
        else:
            print("node id" , i , "prev" , previous[i] , "distance :" , dist[i])
    
def Prims(gph):
    previous = [-1] * gph.count
    dist = [sys.maxsize] * gph.count
    visited = [False] * gph.count
    source = 0
    dist[source] = 0
    previous[source] = -1
    pq = PriorityQueue()
    for i in range(gph.count):
        pq.Add(sys.maxint, i)
    pq.UpdateKey(0, source)
    
    while pq.Size() != 0:
        val = pq.Pop()
        source = val[1]
        curr = gph.array[source]
        visited[source] = True

        while curr != None:
            alt = curr.cost
            if alt < dist[curr.destination] and visited[curr.destination] == False:
                dist[curr.destination] = curr.cost
                previous[curr.destination] = source
                pq.UpdateKey(alt, curr.destination)
            curr = curr.next
    
    for i in range(gph.count):
        if dist[i] == sys.maxsize:
            print("node id" , i , "prev" , previous[i] , "distance : Unreachable")
        else:
            print("node id" , i , "prev" , previous[i] , "distance :" , dist[i])
        

def TopologicalSortDFS(gph, index, visited, stk):
    head = gph.array[index]
    visited[index] = True
    while head != None:
        if visited[head.destination] == False:
            TopologicalSortDFS(gph, head.destination, visited, stk)
        head = head.next
    stk.append(index)

def TopologicalSort(gph):
    stk = []
    count = gph.count
    visited = [False] * count
    for i in range(count):
        if visited[i] == False:
            TopologicalSortDFS(gph, i, visited, stk)

    while len(stk) != 0:
        print stk.pop() , 

def PathExist(gph, source, destination):
    count = gph.count
    visited = [False] * count
    DFSRec(gph, source, visited)
    return visited[destination]

def DFSRec(gph, index, visited):
    head = gph.array[index]
    visited[index] = True
    while head != None:
        if visited[head.destination] == False:
            DFSRec(gph, head.destination, visited)
        head = head.next

def reverseGraph(gph):
    count = gph.count
    g = Graph(count)
    for i in range(count):
        head = gph.array[i]
        while head != None:
            g.AddDirectedEdge(head.destination, i)
            head = head.next
    return g


def DFSRec2(gph, index, visited, stk):
    head = gph.array[index]
    visited[index] = True
    while head != None:
        if visited[head.destination] == False:
            DFSRec2(gph, head.destination, visited, stk)
        head = head.next
    stk.append(index)

# Kosaraju Algorithm
"""
Kosaraju’s Algorithm to find strongly connected directed graph based on DFS :
1)	Create a visited array of size V, and Initialize all vertices in visited array as False.
2)	Choose any vertice and perform a DFS traversal of graph. For all visited vertices mark them visited as True. 
3)	If DFS traversal does not mark all vertices as True, then return False.
4)	Find transpose or reverse of graph
5)	Repeat step 1, 2 and 3 for the reversed graph. 
6)	If DFS traversal mark all the vertices as True, then return True.

"""
def isStronglyConnected(gph):
    count = gph.count
    visited = [False] * count
    DFSRec(gph, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    gReversed = reverseGraph(gph)
    visited = [False] * count
    DFSRec(gReversed, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True

def stronglyConnectedComponent(gph):
    count = gph.count
    visited = [False] * count
    stk = []
    for i in range(count):
        if visited[i] == False:
            DFSRec2(gph, i, visited, stk)
    
    gReversed = reverseGraph(gph)
    visited = [False] * count
    while len(stk) != 0:
        index = stk.pop()
        if visited[index] == False:
            stk2 = []
            DFSRec2(gReversed, index, visited, stk2)
            print stk2
        
    DFSRec(gReversed, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True

def isConnectedUndirected(gph):
    count = gph.count
    visited = [False] * count
    DFSRec(gph, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True
    
def DFSStack(gph):
    count = gph.count
    visited = [False] * count
    stk = []
    stk.append(object)
    while len(stk) != 0:
        curr = stk.pop()
        visited[curr] = True
        head = gph.array[curr]
        while head != None:
            if visited[head.destination] == False:
                visited[head.destination] = True
                stk.append(head.destination)
            head = head.next
 
def DFS(gph):
    count = gph.count
    visited = [False] * count
    for i in range(count):
        if visited[i] == 0:
            DFSRec(gph, i, visited)
 
def BFSQueue(gph, index, visited):
    que = deque([])
    que.append(index)
    while len(que) != 0:
        curr = que.popleft()
        visited[curr] = True
        head = gph.array[curr]
        while head != None:
            if visited[head.destination] == 0:
                visited[head.destination] = True
                que.append(head.destination)
            head = head.next
 
def BFS(gph):
    count = gph.count
    visited = [False] * count
    for i in range(count):
        if visited[i] == 0:
            BFSQueue(gph, i, visited)


def ShortestPath(gph, source):
    count = gph.count
    distance = [-1] * count
    path = [-1] * count
    que = deque([])

    que.append(source)
    distance[source] = 0
    while len(que) != 0:
        curr = que.popleft()
        head = gph.array[curr]
        while head != None:
            if distance[head.destination] == -1:
                distance[head.destination] = distance[curr] + 1
                path[head.destination] = curr
                que.append(head.destination)
            head = head.next
    
    for i in range(count):
        print(path[i] , "to" , i , "weight" , distance[i])

def BellmanFordShortestPath(gph, source):
    count = gph.count
    distance = [sys.maxsize] * count
    path = [-1] * count
    distance[source] = 0
    for i in range(count - 1):
        for j in range(count):
            head = gph.array[j]
            while head != None:
                if distance[j] != sys.maxint:
                    newDistance = distance[j] + head.cost
                    if distance[head.destination] > newDistance:
                        distance[head.destination] = newDistance
                        path[head.destination] = j
                head = head.next
        
    for i in range(count):
        print(path[i] , "to" , i , "weight" , distance[i])

"""
graph = Graph(9)
graph.AddUndirectedEdge(0, 1, 4)
graph.AddUndirectedEdge(0, 7, 8)
graph.AddUndirectedEdge(1, 2, 8)
graph.AddUndirectedEdge(1, 7, 11)
graph.AddUndirectedEdge(2, 3, 7)
graph.AddUndirectedEdge(2, 8, 2)
graph.AddUndirectedEdge(2, 5, 4)
graph.AddUndirectedEdge(3, 4, 9)
graph.AddUndirectedEdge(3, 5, 14)
graph.AddUndirectedEdge(4, 5, 10)
graph.AddUndirectedEdge(5, 6, 2)
graph.AddUndirectedEdge(6, 7, 1)
graph.AddUndirectedEdge(6, 8, 6)
graph.AddUndirectedEdge(7, 8, 7)
Prims(graph)
# Dijkstra(graph, 0)
"""
gph = Graph(9)
gph.AddUndirectedEdge(0, 2, 1)
gph.AddUndirectedEdge(1, 2, 5)
gph.AddUndirectedEdge(1, 3, 7)
gph.AddUndirectedEdge(1, 4, 9)
gph.AddUndirectedEdge(3, 2, 2)
gph.AddUndirectedEdge(3, 5, 4)
gph.AddUndirectedEdge(4, 5, 6)
gph.AddUndirectedEdge(4, 6, 3)
gph.AddUndirectedEdge(5, 7, 1)
gph.AddUndirectedEdge(6, 7, 7)
gph.AddUndirectedEdge(7, 8, 17)
Prims(gph)
Dijkstra(gph, 1)
gph.Print()

print(PathExist(gph, 1, 5))
print(isConnectedUndirected(gph))
ShortestPath(gph, 1)
BellmanFordShortestPath(gph, 1)
"""
g = Graph(6)
g.AddDirectedEdge(5, 2)
g.AddDirectedEdge(5, 0)
g.AddDirectedEdge(4, 0)
g.AddDirectedEdge(4, 1)
g.AddDirectedEdge(2, 3)
g.AddDirectedEdge(3, 1)
print("Topological Sort::")
TopologicalSort(g)

# Create a graph given in the above diagram
g1 = Graph(5)
g1.AddDirectedEdge(0, 1)
g1.AddDirectedEdge(1, 2)
g1.AddDirectedEdge(2, 3)
g1.AddDirectedEdge(3, 0)
g1.AddDirectedEdge(2, 4)
g1.AddDirectedEdge(4, 2)
print isStronglyConnected(g1)
 
g2 = Graph(4)
g2.AddDirectedEdge(0, 1)
g2.AddDirectedEdge(1, 2)
g2.AddDirectedEdge(2, 3)
print isStronglyConnected(g2)

graph = Graph(7)
graph.AddDirectedEdge(0, 1)
graph.AddDirectedEdge(1, 2)
graph.AddDirectedEdge(2, 0)
graph.AddDirectedEdge(2, 3)
graph.AddDirectedEdge(3, 4)
graph.AddDirectedEdge(4, 5)
graph.AddDirectedEdge(5, 3)
graph.AddDirectedEdge(5, 6)
stronglyConnectedComponent(graph)
"""