#!/usr/bin/env python
import heapq
import sys
from collections import deque

class Graph(object):
    def __init__(self, cnt):
        self.count = cnt
        self.adj = [[] for _ in range(cnt)]
    
    def AddDirectedEdge(self, source, destination, cost=1):
        edge = (destination, cost)
        self.adj[source].append(edge)
    
    def AddUndirectedEdge(self, source, destination, cost=1):
        self.AddDirectedEdge(source, destination, cost)
        self.AddDirectedEdge(destination, source, cost)

    def Print(self):
        for i in range(self.count):
            print "Vertex " , i , " is connected to : ",
            for edge in self.adj[i]:
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
            for edge in gph.adj[j]:
                newDistance = distance[j] + edge[1]
                if distance[edge[0]] > newDistance:
                    distance[edge[0]] = newDistance
                    path[edge[0]] = j
    for i in range(count):
        print (path[i] , "to" , i , "weight" , distance[i])

"""
g = Graph(5)
g.AddDirectedEdge(0, 1, 3)
g.AddDirectedEdge(0, 4, 2)
g.AddDirectedEdge(1, 2, 1)
g.AddDirectedEdge(2, 3, 1)
g.AddDirectedEdge(4, 1, -2)
g.AddDirectedEdge(4, 3, 1)
BellmanFordShortestPath(g, 0)
"""

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
        for edge in gph.adj[source]:
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

        for edge in gph.adj[source]:
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
Dijkstra(graph, 0)
"""

def DFSUtil(gph, index, visited):
    visited[index] = True
    for edge in gph.adj[index]:
        if visited[edge[0]] == False:
            DFSUtil(gph, edge[0], visited)
"""

"""
def RootVertex(gph):
    count = gph.count
    visited = [False] * count
    retVal = -1
    for i in range(count):
        if visited[i] == False:
            DFSUtil(gph, i, visited)
            retVal = i
    print "Root vertex is :: ", retVal

"""
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
"""

def TopologicalSortDFS(gph, index, visited, stk):
    visited[index] = True
    for edge in gph.adj[index]:
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

"""
g = Graph(6)
g.AddDirectedEdge(5, 2)
g.AddDirectedEdge(5, 0)
g.AddDirectedEdge(4, 0)
g.AddDirectedEdge(4, 1)
g.AddDirectedEdge(2, 3)
g.AddDirectedEdge(3, 1)
TopologicalSort(g)
"""

def PathExist(gph, source, destination):
    count = gph.count
    visited = [False] * count
    DFSRec(gph, source, visited)
    return visited[destination]

"""
"""

def DFSRec(gph, index, visited):
    visited[index] = True
    print index ,
    for edge in gph.adj[index]:
        destination = edge[0]
        if visited[destination] == False:
            DFSRec(gph, destination, visited)


def TransposeGraph(gph):
    count = gph.count
    g = Graph(count)
    for i in range(count):
        for edge in gph.adj[i]:
            destination = edge[0]
            g.AddDirectedEdge(destination, i)
    return g



# Kosaraju Algorithm
"""
Kosaraju’s Algorithm to find strongly connected directed graph based on DFS :
1)	Create a visited array of size V, and Initialize all vertices in visited array as False.
2)	Choose any vertex and perform a DFS traversal of graph. For all visited vertices mark them visited as True. 
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
    gReversed = TransposeGraph(gph)
    visited = [False] * count
    DFSRec(gReversed, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True
"""
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
"""


def DFSRec2(gph, index, visited, stk):
    visited[index] = True
    for edge in gph.adj[index]:
        destination = edge[0]
        if visited[destination] == False:
            DFSRec2(gph, destination, visited, stk)
    stk.append(index)

def stronglyConnectedComponent(gph):
    count = gph.count
    visited = [False] * count
    stk = []
    for i in range(count):
        if visited[i] == False:
            DFSRec2(gph, i, visited, stk)
    
    gReversed = TransposeGraph(gph)
    visited = [False] * count
    while len(stk) != 0:
        index = stk.pop()
        if visited[index] == False:
            stk2 = []
            DFSRec2(gReversed, index, visited, stk2)
            print stk2
"""
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

def isConnectedUndirected(gph):
    count = gph.count
    visited = [False] * count
    DFSRec(gph, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True
    
def DFSStack(gph, source, target):
    count = gph.count
    visited = [False] * count
    stk = []
    stk.append(source)
    visited[source] = True
    while len(stk) != 0:
        curr = stk.pop()
        print curr ,
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                stk.append(destination)
                visited[destination] = True
    return visited[target]
            
def DFS(gph, source, target):
    count = gph.count
    visited = [False] * count
    print "DFS : ",
    DFSRec(gph, source, visited)
    return visited[target]
 
def BFS(gph, source, target):
    count = gph.count
    visited = [False] * count
    visited[source] = True
    print "BFS : ",
    que = deque([])
    que.append(source)
    while len(que) != 0:
        curr = que.popleft()
        print curr ,
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                que.append(destination)
                visited[destination] = True
    return visited[target]


def BFSLevelNode(gph, source):
    count = gph.count
    visited = [False] * count
    visited[source] = True
    que = deque([])
    que.append((source, 0))
    print "\nNode  - Level"
    while len(que) != 0:
        node = que.popleft()
        curr = node[0]
        depth = node[1]
        print curr ," - ", depth
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                que.append((destination, depth+1))
                visited[destination] = True

def BFSDistance(gph, source, dest):
    count = gph.count
    visited = [False] * count
    visited[source] = True
    que = deque([])
    que.append((source, 0))
    while len(que) != 0:
        node = que.popleft()
        curr = node[0]
        depth = node[1]
        for edge in gph.adj[curr]:
            if edge[0] == dest:
                return depth
            if visited[edge[0]] == False:
                que.append((edge[0], depth+1))
                visited[edge[0]] = True
    return -1
"""
g = Graph(7)
g.AddUndirectedEdge(0, 1)
g.AddUndirectedEdge(0, 2)
g.AddUndirectedEdge(0, 4)
g.AddUndirectedEdge(1, 2)
g.AddUndirectedEdge(2, 5)
g.AddUndirectedEdge(3, 4)
g.AddUndirectedEdge(4, 5)
g.AddUndirectedEdge(4, 6)
print BFSDistance(g, 1, 3)
"""

def ShortestPath(gph, source):
    count = gph.count
    distance = [-1] * count
    path = [-1] * count
    que = deque([])
    que.append(source)
    distance[source] = 0
    while len(que) != 0:
        curr = que.popleft()
        for edge in gph.adj[curr]:
            destination = edge[0]
            if distance[destination] == -1:
                distance[destination] = distance[curr] + 1
                path[destination] = curr
                que.append(destination)
    
    for i in range(count):
        print(path[i] , "to" , i , "weight" , distance[i])

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
DFS(gph, 0)
BFS(gph, 0)
BFSLevelNode(gph, 0)
BellmanFordShortestPath(gph, 1)
Dijkstra(gph, 1)
Prims(gph)
print(PathExist(gph, 1, 5))
print(isConnectedUndirected(gph))
ShortestPath(gph, 1)
"""

"""
Given a directed graph, fidn transitive closure matrix or reachablity matrix
vertex v is reachable form vertex u if their is a path from u to v.
"""
def TransitiveClosureUtil(gph, source ,index, tc):
    if tc[source][index] == 1:
        return
    tc[source][index] = 1
    for edge in gph.adj[index]:
            TransitiveClosureUtil(gph, source, edge[0], tc)

def TransitiveClosure(gph):
    count = gph.count
    tc = [[0 for _ in range(count)] for _ in range(count)]
    for source in range(count):
        TransitiveClosureUtil(gph, source, source, tc)
    for row in tc:
        print row

"""
g = Graph(4)
g.AddDirectedEdge(0, 1)
g.AddDirectedEdge(0, 2)
g.AddDirectedEdge(1, 2)
g.AddDirectedEdge(2, 0)
g.AddDirectedEdge(2, 3)
g.AddDirectedEdge(3, 3)
g.Print()
TransitiveClosure(g)
"""
def countAllPathDFS(gph, visited, source ,dest):
    if source == dest:
        return 1

    count = 0
    visited[source] = 1
    for edge in gph.adj[source]:
        if visited[edge[0]] == 0:
            count += countAllPathDFS(gph, visited, edge[0], dest)
    visited[source] = 0
    return count

def countAllPath(gph, src ,dest):
    visited = [0]*gph.count
    return countAllPathDFS(gph, visited, src, dest)

def printAllPathDFS(gph, visited, source ,dest, path):
    path.append(source)
    if source == dest:
        print path
        return

    visited[source] = 1
    for edge in gph.adj[source]:
        if visited[edge[0]] == 0:
            printAllPathDFS(gph, visited, edge[0], dest, path)
    visited[source] = 0
    path.pop()

def printAllPath(gph, src ,dest):
    visited = [0]*gph.count
    path = []
    printAllPathDFS(gph, visited, src, dest, path)
"""
g = Graph(5)
g.AddDirectedEdge(0, 1)
g.AddDirectedEdge(0, 2)
g.AddDirectedEdge(2, 3)
g.AddDirectedEdge(1, 3)
g.AddDirectedEdge(3, 4)
g.AddDirectedEdge(1, 4)
print countAllPath(g, 0, 4)
printAllPath(g, 0, 4)
"""
def HeightTreeParentArr(arr):
    count = len(arr)
    gph = Graph(count)
    for i in range(len(arr)):
        if arr[i] != -1 :
            gph.AddDirectedEdge(arr[i], i)
        else:
            source = i

    visited = [False] * count
    visited[source] = True
    que = deque([])
    que.append((source, 0))
    maxHeight = 0
    while len(que) != 0:
        node = que.popleft()
        curr = node[0]
        height = node[1]
        if height > maxHeight:
            maxHeight = height
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                que.append((destination, height+1))
                visited[destination] = True
    return maxHeight

def getHeight(arr, height, index):
    if arr[index] == -1:
        return 0
    else:
        return getHeight(arr, height, arr[index]) + 1

def HeightTreeParentArr2(arr):
    count = len(arr)
    height = [-1] * count
    maxHeight = -1
    for i in range(len(arr)):
        height[i] = getHeight(arr, height, i)
        maxHeight = max(maxHeight, height[i])
    return maxHeight
"""
parentArray = [-1, 0, 1, 2, 3]
print HeightTreeParentArr(parentArray)
print HeightTreeParentArr2(parentArray)
parentArray = [-1, 0, 0, 0, 3, 1, 1, 2]
print HeightTreeParentArr(parentArray)
print HeightTreeParentArr2(parentArray)
"""

def BestFirstSearchPQ(gph, source, dest):
    previous = [-1] * gph.count
    dist = [sys.maxsize] * gph.count
    visited = [False] * gph.count
    pq = PriorityQueue()
    dist[source] = 0
    previous[source] = -1
    pq.Add(0, source)
    
    while pq.Size() != 0:
        val = pq.Pop()
        if val[1] == dest:
            return val[0]
        source = val[1]
        visited[source] = True
        for edge in gph.adj[source]:
            destination = edge[0]
            cost = edge[1]
            alt = cost + dist[source]
            if alt < dist[destination] and visited[destination] == False:
                dist[destination] = alt
                previous[destination] = source
                pq.Add(alt, destination)
    return -1



"""
Given a directed graph find if there is a cycle in it. 
"""
def isCyclePresentDFS(graph, index, visited, marked):
    visited[index] = True
    marked[index] = True

    for node in graph.adj[index]:
        dest = node[0]
        if marked[dest] == True:
            return True

        if visited[dest] == False:
            if isCyclePresentDFS(graph, dest, visited, marked) :
                return True
        
    marked[index] = False
    return False

def isCyclePresent(graph):
    count = graph.count
    visited = [False] * count
    marked = [False] * count
    for index in range(count):
        if visited[index] == False:
            if isCyclePresentDFS(graph, index, visited, marked) :
                return True
    return False


def isCyclePresentDFSColor(graph, index, visited):
    visited[index] = "Grey"

    for node in graph.adj[index]:
        dest = node[0]
        if visited[dest] == "Grey":
            return True
            
        if visited[dest] == "White":
            if isCyclePresentDFSColor(graph, dest, visited) :
                return True
        
    visited[index] = "Black"
    return False

def isCyclePresentColor(graph):
    count = graph.count
    visited = ["White"] * count
    for index in range(count):
        if visited[index] == "White":
            if isCyclePresentDFSColor(graph, index, visited) :
                return True
    return False

"""
g = Graph(5)
g.AddDirectedEdge(0, 1)
g.AddDirectedEdge(0, 2)
g.AddDirectedEdge(1, 3)
g.AddDirectedEdge(2, 3)
g.AddDirectedEdge(3, 4)
#g.AddDirectedEdge(4, 1)
print isCyclePresentColor(g)
"""

def isCyclePresentUndirectedDFS(graph, index, parentIndex, visited):
    visited[index] = True
    for node in graph.adj[index]:
        dest = node[0]
        if visited[dest] == False:
            if isCyclePresentUndirectedDFS(graph, dest, index, visited) :
                return True
        elif parentIndex != dest :
            return True
    return False


def isCyclePresentUndirected(graph):
    count = graph.count
    visited = [False] * count
    for index in range(count):
        if visited[index] == False:
            if isCyclePresentUndirectedDFS(graph, index, -1, visited) :
                return True
    return False
"""
g = Graph(6)
g.AddUndirectedEdge(0, 1)
g.AddUndirectedEdge(1, 2)
g.AddUndirectedEdge(3, 4)
g.AddUndirectedEdge(4, 2)
g.AddUndirectedEdge(2, 5)
#g.AddUndirectedEdge(4, 1)
#print isCyclePresentUndirected(g)
"""

def isConnected(graph):
    count = graph.count
    visited =[False]*count
 
    # Find a vertex with non-zero degree
    for i in range(count):
        if len(graph.adj[i]) > 1:
            # DFS traversal of graph from a vertex with non-zero degree
            DFSUtil(graph, i, visited)
            break

    # Check if all non-zero degree vertices are visited
    for i in range(count):
        if visited[i]==False and len(graph.adj[i]) > 0:
            return False
        
    return True

'''
The function returns one of the following values
Return 0 if graph is not Eulerian
Return 1 if graph has an Euler path (Semi-Eulerian)
Return 2 if graph has an Euler Circuit (Eulerian)
'''
def isEulerian(graph):
    count = graph.count
    # Check if all non-zero degree vertices are connected
    if isConnected(graph) == False:
        print "graph is not Eulerian"
        return 0
    else:
        # Count vertices with odd degree
        odd = 0
        for i in range(count):
            if len(graph.adj[i]) % 2 !=0:
                odd +=1

        if odd > 2:
            print "graph is not Eulerian"
            return 0
        elif odd == 2:
            print "graph is Semi-Eulerian"
            return 1
        elif odd == 0:
            print "graph is Eulerian"
            return 2

g1 = Graph(5)
g1.AddUndirectedEdge(1, 0)
g1.AddUndirectedEdge(0, 2)
g1.AddUndirectedEdge(2, 1)
g1.AddUndirectedEdge(0, 3)
g1.AddUndirectedEdge(3, 4)
isEulerian(g1)
 
g2 = Graph(5)
g2.AddUndirectedEdge(1, 0)
g2.AddUndirectedEdge(0, 2)
g2.AddUndirectedEdge(2, 1)
g2.AddUndirectedEdge(0, 3)
g2.AddUndirectedEdge(3, 4)
g2.AddUndirectedEdge(4, 0)
isEulerian(g2)
 
g3 = Graph(5)
g3.AddUndirectedEdge(1, 0)
g3.AddUndirectedEdge(0, 2)
g3.AddUndirectedEdge(2, 1)
g3.AddUndirectedEdge(0, 3)
g3.AddUndirectedEdge(3, 4)
g3.AddUndirectedEdge(1, 3)
isEulerian(g3)

def isStronglyConnected2(graph):
    count = graph.count
    visited = [False] * count
    
        # Find a vertex with non-zero degree
    for index in range(count):
        if len(graph.adj[index]) > 1:
            break
    # DFS traversal of graph from a vertex with non-zero degree
    DFSUtil(graph, index, visited)
            
    for i in range(count):
        if visited[i] == False and len(graph.adj[i]) > 0:
            return False

    gReversed = TransposeGraph(graph)
    visited = [False] * count
    DFSRec(gReversed, index, visited)
    
    for i in range(count):
        if visited[i] == False and len(graph.adj[i]) > 0:
            return False
    return True

def isEulerianCycle(graph):
    # Check if all non-zero degree vertices 
    # are connected
    if isStronglyConnected2(graph) == False:
        return False
    count = graph.count
    inDegree = [0] * count
    outDegree = [0] * count

    # Check if in degree and out degree of 
    # every vertex is same
    for i in range(count):
        outDegree[i] = len(graph.adj[i])
        for j in graph.adj[i]:
            inDegree[j[0]] += 1
        
    for i in range(count):
        if inDegree[i] != outDegree[i]:
            return False
    return True

g = Graph(5)
g.AddDirectedEdge(0, 1)
g.AddDirectedEdge(1, 2)
g.AddDirectedEdge(2, 0)
g.AddDirectedEdge(0, 4)
g.AddDirectedEdge(4, 3)
g.AddDirectedEdge(3, 0)
print isEulerianCycle(g)


