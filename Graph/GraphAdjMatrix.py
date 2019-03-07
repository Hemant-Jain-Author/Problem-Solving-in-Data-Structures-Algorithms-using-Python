#!/usr/bin/env python
import heapq
import sys
from collections import deque

class Graph(object):
    def __init__(self, cnt):
        self.count = cnt
        self.adj = [[0 for _ in range(cnt)] for _ in range(cnt)]
        
    def AddDirectedEdge(self, source, destination, cost=1):
        self.adj[source][destination] = cost
    
    def AddUndirectedEdge(self, source, destination, cost=1):
        self.AddDirectedEdge(source, destination, cost)
        self.AddDirectedEdge(destination, source, cost)

    def Print(self):
        for i in range(self.count):
            print("Vertex " , i , " is connected to : ", end=' ')
            for j in range(self.count):
                if self.adj[i][j] != 0:
                    print(j ,"")
            print("")

graph = Graph(4)
graph.AddUndirectedEdge(0, 1)
graph.AddUndirectedEdge(0, 2)
graph.AddUndirectedEdge(1, 2)
graph.AddUndirectedEdge(2, 3)
graph.Print()
"""
Vertex  0  is connected to :  1 2
Vertex  1  is connected to :  0 2
Vertex  2  is connected to :  0 1 3
Vertex  3  is connected to :  2
"""
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
    
def printPath(count, previous, dist):
    for i in range(count):
        if dist[i] == sys.maxsize:
            print("node id" , i , "prev" , previous[i] , "distance : Unreachable")
        else:
            print("node id" , i , "prev" , previous[i] , "distance :" , dist[i])




def Dijkstra(gph, source):
    previous = [-1] * gph.count
    dist = [sys.maxsize] * gph.count
    visited = [False] * gph.count
    dist[source] = 0
    previous[source] = -1
    
    pq = PriorityQueue()
    for i in range(gph.count):
        pq.Add(sys.maxsize, i)
    pq.UpdateKey(0, source)
    
    while pq.Size() != 0:
        val = pq.Pop()
        source = val[1]
        visited[source] = True
        
        for dest in range(gph.count):
            alt = gph.adj[source][dest] + dist[source]
            if gph.adj[source][dest] > 0 and alt < dist[dest] and visited[dest] == False:
                dist[dest] = alt
                previous[dest] = source
                pq.UpdateKey(alt, dest)
    printPath(graph.count, previous,dist)


def Prims(gph):
    previous = [-1] * gph.count
    dist = [sys.maxsize] * gph.count
    visited = [False] * gph.count
    source = 0
    dist[source] = 0
    previous[source] = -1
    pq = PriorityQueue()
    for i in range(gph.count):
        pq.Add(sys.maxsize, i)
    pq.UpdateKey(0, source)
    
    while pq.Size() != 0:
        val = pq.Pop()
        source = val[1]
        visited[source] = True
        
        for dest in range(gph.count):
            alt = gph.adj[source][dest]
            if gph.adj[source][dest] > 0 and alt < dist[dest] and visited[dest] == False:
                dist[dest] = alt
                previous[dest] = source
                pq.UpdateKey(alt, dest)
    
    printPath(graph.count, previous,dist)

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
#Dijkstra(graph, 0)
Prims(graph)
# graph.Print()
"""
def HamiltonianCycleUtil(graph , path, added):
    # Base case: full length path is found 
    # this last check can be modified to make it a path.
    if len(path) == graph.count:
        if graph.adj[ path[-1] ][ path[0] ] == 1:
            path.append(path[0])
            return True
        else:
            return False
    
    for vertex in range(graph.count):
        # there is a path from last element and next vertex 
        if graph.adj[path[-1]][vertex] == 1 and added[vertex] == False:
            path.append(vertex)
            added[vertex] = True
            if HamiltonianCycleUtil(graph, path, added):
                return True
            # backtracking
            path.pop()
            added[vertex] = False
    return False

def HamiltonianCycle(graph):
    path = []
    path.append(0)
    added = [False]*graph.count
    added[0] = True
    if HamiltonianCycleUtil(graph, path, added):
        print("Hamiltonian Cycle found", path)
        return True
    print("Hamiltonian Cycle not found")
    return False

def HamiltonianPathUtil(graph , path, added):
    # Base case: full length path is found 
    if len(path) == graph.count:
            return True
    
    for vertex in range(graph.count):
        # there is a path from last element and next vertex 
        # and next vertex is not already included in path.
        if graph.adj[path[-1]][vertex] == 1 and added[vertex] == False:
            path.append(vertex)
            added[vertex] = True
            if HamiltonianPathUtil(graph, path, added):
                return True
            # backtracking
            path.pop()
            added[vertex] = False
    return False

def HamiltonianPath(graph):
    path = []
    path.append(0)
    added = [False]*graph.count
    added[0] = True
    if HamiltonianPathUtil(graph, path, added):
        print("Hamiltonian Path found", path)
        return True
    print("Hamiltonian Path not found")
    return False
"""
graph = Graph(5)
graph.adj = [ [0, 1, 0, 1, 0], 
                [1, 0, 1, 1, 0], 
                [0, 1, 0, 0, 1,],
                [1, 1, 0, 0, 1], 
                [0, 1, 1, 1, 0] ]
print HamiltonianPath(graph)

g2 = Graph(5)
g2.adj = [ [0, 1, 0, 1, 0], 
            [1, 0, 1, 1, 0], 
            [0, 1, 0, 0, 1,], 
            [1, 1, 0, 0, 0], 
            [0, 1, 1, 0, 0] ]
 
print HamiltonianPath(g2)
"""