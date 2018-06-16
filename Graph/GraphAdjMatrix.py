#!/usr/bin/env python
import heapq
import sys
from collections import deque

class Graph(object):
    def __init__(self, cnt):
        self.count = cnt
        self.array = [[0 for _ in range(cnt)] for _ in range(cnt)]
        
    def AddEdge(self, source, destination, cost=1):
        self.array[source][destination] = cost
    
    def AddBiEdge(self, source, destination, cost=1):
        self.AddEdge(source, destination, cost)
        self.AddEdge(destination, source, cost)

    def Print(self):
        for i in range(self.count):
            print "Vertex " , i , " is connected to : ",
            for j in range(self.count):
                if self.array[i][j] != 0:
                    print j ,
            print("")


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
        visited[source] = True
        
        for dest in range(gph.count):
            alt = gph.array[source][dest] + dist[source]
            if gph.array[source][dest] > 0 and alt < dist[dest] and visited[dest] == False:
                dist[dest] = alt
                previous[dest] = source
                pq.UpdateKey(alt, dest)
            
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
        
        for dest in range(gph.count):
            alt = gph.array[source][dest]
            if gph.array[source][dest] > 0 and alt < dist[dest] and visited[dest] == False:
                dist[dest] = alt
                previous[dest] = source
                pq.UpdateKey(alt, dest)
            
    for i in range(gph.count):
        if dist[i] == sys.maxsize:
            print("node id" , i , "prev" , previous[i] , "distance : Unreachable")
        else:
            print("node id" , i , "prev" , previous[i] , "distance :" , dist[i])

graph = Graph(9)
graph.AddBiEdge(0, 1, 4)
graph.AddBiEdge(0, 7, 8)
graph.AddBiEdge(1, 2, 8)
graph.AddBiEdge(1, 7, 11)
graph.AddBiEdge(2, 3, 7)
graph.AddBiEdge(2, 8, 2)
graph.AddBiEdge(2, 5, 4)
graph.AddBiEdge(3, 4, 9)
graph.AddBiEdge(3, 5, 14)
graph.AddBiEdge(4, 5, 10)
graph.AddBiEdge(5, 6, 2)
graph.AddBiEdge(6, 7, 1)
graph.AddBiEdge(6, 8, 6)
graph.AddBiEdge(7, 8, 7)
#Dijkstra(graph, 0)
Prims(graph)
# graph.Print()