#!/usr/bin/env python
import heapq
import sys
from collections import deque

class Graph(object):
    def __init__(self, cnt):
        self.count = cnt
        self.array = [[] for _ in range(cnt)]
    
    def AddDirectedEdge(self, source, destination, cost=1):
        edge = (destination, cost)
        self.array[source].append(edge)
    
    def AddUndirectedEdge(self, source, destination, cost=1):
        self.AddDirectedEdge(source, destination, cost)
        self.AddDirectedEdge(destination, source, cost)

    def Print(self):
        for i in range(self.count):
            print "Vertex " , i , " is connected to : ",
            for edge in self.array[i]:
                print (edge[0] , edge[1]),
            print("")


class PriorityQueue(object):

    def __init__(self):
        self.pQueue = []
        self.count = 0
    
    def Add(self, key, value):
        heapq.heappush(self.pQueue, (key, value))
    
    def UpdateKey(self, key, value):
        # this is a dummy function actual implimentation 
        # tbd
        heapq.heappush(self.pQueue, (key, value))

    def Pop(self):
        val = heapq.heappop(self.pQueue)
        return val

    def Size(self):
        return len(self.pQueue)
    

def BellmanFordShortestPath(gph, source):
    count = gph.count
    distance = [sys.maxsize] * count
    path = [-1] * count
    distance[source] = 0

    # Outer loop will run (V-1) number of times. 
    # Inner for loop and while loop runs combined will 
    # run for Edges number of times.
    # Which make the total complexity as O(V*E)
    for _ in range(count - 1):
        for j in range(count):
            for edge in gph.array[j]:
                newDistance = distance[j] + edge[1]
                if distance[edge[0]] > newDistance:
                    distance[edge[0]] = newDistance
                    path[edge[0]] = j
    for i in range(count):
        print (path[i] , "to" , i , "weight" , distance[i])


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
        visited[source] = True
        for edge in gph.array[source]:
            destination = edge[0]
            cost = edge[1]
            alt = cost + dist[source]
            if alt < dist[destination] and visited[destination] == False:
                dist[destination] = alt
                previous[destination] = source
                pq.UpdateKey(alt, destination)

    
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
        visited[source] = True

        for edge in gph.array[source]:
            destination = edge[0]
            cost = edge[1]
            if cost < dist[destination] and visited[destination] == False:
                dist[destination] = cost
                previous[destination] = source
                pq.UpdateKey(cost, destination)
    
    for i in range(gph.count):
        if dist[i] == sys.maxsize:
            print("node id" , i , "prev" , previous[i] , "distance : Unreachable")
        else:
            print("node id" , i , "prev" , previous[i] , "distance :" , dist[i])

def DFSUtil(gph, index, visited):
    visited[index] = True
    for edge in gph.array[index]:
        if visited[edge[0]] == False:
            DFSUtil(gph, edge[0], visited)

def RootVertex(gph):
    count = gph.count
    visited = [False] * count
    retVal = -1
    for i in range(count):
        if visited[i] == False:
            DFSUtil(gph, i, visited)
            retVal = i
    print "Root vertex is :: ", retVal

def TopologicalSortDFS(gph, index, visited, stk):
    visited[index] = True
    for edge in gph.array[index]:
        destination = edge[0]
        if visited[destination] == False:
            TopologicalSortDFS(gph, destination, visited, stk)
    stk.append(index)

def TopologicalSort(gph):
    stk = []
    count = gph.count
    visited = [False] * count
    for i in range(count):
        if visited[i] == False:
            TopologicalSortDFS(gph, i, visited, stk)
    print "TopologicalSort :: ",
    while len(stk) != 0:
        print stk.pop() , 
    print ""

def PathExist(gph, source, destination):
    count = gph.count
    visited = [False] * count
    DFSRec(gph, source, visited)
    return visited[destination]

def DFSRec(gph, index, visited):
    visited[index] = True
    # print index ,
    for edge in gph.array[index]:
        destination = edge[0]
        if visited[destination] == False:
            DFSRec(gph, destination, visited)

def reverseGraph(gph):
    count = gph.count
    g = Graph(count)
    for i in range(count):
        for edge in gph.array[i]:
            destination = edge[0]
            g.AddDirectedEdge(destination, i)
    return g


def DFSRec2(gph, index, visited, stk):
    visited[index] = True
    for edge in gph.array[index]:
        destination = edge[0]
        if visited[destination] == False:
            DFSRec2(gph, destination, visited, stk)
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
        

def isConnectedUndirected(gph):
    count = gph.count
    visited = [False] * count
    DFSRec(gph, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True
    
def DFSStack(gph, source):
    count = gph.count
    visited = [False] * count
    stk = []
    stk.append(source)
    visited[source] = True

    while len(stk) != 0:
        curr = stk.pop()
        print curr ,
        for edge in gph.array[curr]:
            destination = edge[0]
            if visited[destination] == False:
                stk.append(destination)
                visited[destination] = True
            
def DFS(gph, source):
    count = gph.count
    visited = [False] * count
    print "DFS : ",
    DFSRec(gph, source, visited)
 
def BFSQueue(gph, source, visited):
    que = deque([])
    que.append(source)
    visited[source] = True
    while len(que) != 0:
        curr = que.popleft()
        print curr ,
        for edge in gph.array[curr]:
            destination = edge[0]
            if visited[destination] == False:
                que.append(destination)
                visited[destination] = True
 
def BFS(gph, source):
    count = gph.count
    visited = [False] * count
    print "BFS : ",
    BFSQueue(gph, source, visited)


def ShortestPath(gph, source):
    count = gph.count
    distance = [-1] * count
    path = [-1] * count
    que = deque([])
    que.append(source)
    distance[source] = 0
    while len(que) != 0:
        curr = que.popleft()
        for edge in gph.array[curr]:
            destination = edge[0]
            if distance[destination] == -1:
                distance[destination] = distance[curr] + 1
                path[destination] = curr
                que.append(destination)
    
    for i in range(count):
        print(path[i] , "to" , i , "weight" , distance[i])


g = Graph(5)
g.AddDirectedEdge(0, 1, 3)
g.AddDirectedEdge(0, 4, 2)
g.AddDirectedEdge(1, 2, 1)
g.AddDirectedEdge(2, 3, 1)
g.AddDirectedEdge(4, 1, -2)
g.AddDirectedEdge(4, 3, 1)
g.Print()
BellmanFordShortestPath(g, 0)

g = Graph(7)
g.AddDirectedEdge(0, 1)
g.AddDirectedEdge(0, 2)
g.AddDirectedEdge(1, 3)
g.AddDirectedEdge(4, 1)
g.AddDirectedEdge(6, 4)
g.AddDirectedEdge(5, 6)
g.AddDirectedEdge(5, 2)
g.AddDirectedEdge(6, 0)
g.Print()
RootVertex(g)


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
Dijkstra(graph, 0)

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
BellmanFordShortestPath(gph, 1)
DFS(g, 0)
BFS(g, 0)
Dijkstra(gph, 1)
Prims(gph)

print(PathExist(gph, 1, 5))
print(isConnectedUndirected(gph))
ShortestPath(gph, 1)

g = Graph(6)
g.AddDirectedEdge(5, 2)
g.AddDirectedEdge(5, 0)
g.AddDirectedEdge(4, 0)
g.AddDirectedEdge(4, 1)
g.AddDirectedEdge(2, 3)
g.AddDirectedEdge(3, 1)
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