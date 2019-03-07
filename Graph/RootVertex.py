"""
Given a directed graph find a root. 
A root vertex is a vertex from which all other vertex is visited

Hint: root vertex can be find by DFS similar to topology sort. But in place of storing in stack we just 
need to take care of the topmost vertex which can be a root vertex.
"""

class Graph(object):
    class Edge(object):
        def __init__(self, dst, cst=1):
            self.destination = dst
            self.cost = cst
            self.__next__ = None

    def __init__(self, cnt):
        self.count = cnt
        self.array2 = [list]*cnt
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
                print("Vertex " , i , " is connected to : ", end=' ')
                while ad != None:
                    print(ad.destination, end=' ')
                    ad = ad.__next__
                print("")
            i += 1

def DFSUtil(gph, index, visited):
    head = gph.array[index]
    visited[index] = True
    while head != None:
        if visited[head.destination] == False:
            DFSUtil(gph, head.destination, visited)
        head = head.__next__

def RootVertex(gph):
    count = gph.count
    visited = [False] * count
    retVal = -1
    for i in range(count):
        if visited[i] == False:
            DFSUtil(gph, i, visited)
            retVal = i
    print("Root vertex is :: ", retVal)

g = Graph(7)
g.AddDirectedEdge(0, 1)
g.AddDirectedEdge(0, 2)
g.AddDirectedEdge(1, 3)
g.AddDirectedEdge(4, 1)
g.AddDirectedEdge(6, 4)
g.AddDirectedEdge(5, 6)
g.AddDirectedEdge(5, 2)
g.AddDirectedEdge(6, 0)
RootVertex(g)