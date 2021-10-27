import heapq
import sys
from collections import deque

class Graph(object):
    def __init__(self, cnt):
        self.count = cnt
        self.adj = [[0 for _ in range(cnt)] for _ in range(cnt)]
        
    def add_directed_edge(self, source, destination, cost=1):
        self.adj[source][destination] = cost
    
    def add_undirected_edge(self, source, destination, cost=1):
        self.add_directed_edge(source, destination, cost)
        self.add_directed_edge(destination, source, cost)

    def print(self):
        for i in range(self.count):
            print("Vertex", i, "is connected to:", end=' ')
            for j in range(self.count):
                if self.adj[i][j] != 0:
                    print( "(", j,",", self.adj[i][j],")", end =" ")
            print("")

# Testing code
def test1():
    graph = Graph(4)
    graph.add_undirected_edge(0, 1)
    graph.add_undirected_edge(0, 2)
    graph.add_undirected_edge(1, 2)
    graph.add_undirected_edge(2, 3)
    graph.print()


"""
Vertex 0 is connected to: 1 (cost: 1 ) 2 (cost: 1 ) 
Vertex 1 is connected to: 0 (cost: 1 ) 2 (cost: 1 ) 
Vertex 2 is connected to: 0 (cost: 1 ) 1 (cost: 1 ) 3 (cost: 1 ) 
Vertex 3 is connected to: 2 (cost: 1 ) 
"""

class PriorityQueue(object):
    def __init__(self):
        self.que = []
        self.count = 0
    
    def add(self, key, value):
        heapq.heappush(self.que, (key, value))
    
    def update_key(self, key, value):
        heapq.heappush(self.que, (key, value))

    def pop(self):
        val = heapq.heappop(self.que)
        return val

    def size(self):
        return len(self.que)
    
def print_path(count, previous, dist):
    for i in range(count):
        if dist[i] == sys.maxsize:
            print("node id" , i , "prev" , previous[i] , "distance : Unreachable")
        else:
            print("node id" , i , "prev" , previous[i] , "distance :" , dist[i])


def dijkstra(gph, source):
    previous = [-1] * gph.count
    dist = [sys.maxsize] * gph.count
    visited = [False] * gph.count
    dist[source] = 0
    previous[source] = -1
    
    pq = PriorityQueue()
    for i in range(gph.count):
        pq.add(sys.maxsize, i)
    pq.update_key(0, source)
    
    while pq.size() != 0:
        val = pq.pop()
        source = val[1]
        visited[source] = True
        
        for dest in range(gph.count):
            alt = gph.adj[source][dest] + dist[source]
            if gph.adj[source][dest] > 0 and alt < dist[dest] and visited[dest] == False:
                dist[dest] = alt
                previous[dest] = source
                pq.update_key(alt, dest)
    print_path(gph.count, previous,dist)


def prims(gph):
    previous = [-1] * gph.count
    dist = [sys.maxsize] * gph.count
    visited = [False] * gph.count
    source = 0
    dist[source] = 0
    previous[source] = -1
    pq = PriorityQueue()
    
    for i in range(gph.count):
        pq.add(sys.maxsize, i)
    pq.update_key(0, source)
    
    while pq.size() != 0:
        val = pq.pop()
        source = val[1]
        visited[source] = True
        
        for dest in range(gph.count):
            alt = gph.adj[source][dest]
            if gph.adj[source][dest] > 0 and alt < dist[dest] and visited[dest] == False:
                dist[dest] = alt
                previous[dest] = source
                pq.update_key(alt, dest)
    
    print_path(gph.count, previous,dist)

# Testing code
def test2():
    graph = Graph(9)
    graph.add_undirected_edge(0, 1, 4)
    graph.add_undirected_edge(0, 7, 8)
    graph.add_undirected_edge(1, 2, 8)
    graph.add_undirected_edge(1, 7, 11)
    graph.add_undirected_edge(2, 3, 7)
    graph.add_undirected_edge(2, 8, 2)
    graph.add_undirected_edge(2, 5, 4)
    graph.add_undirected_edge(3, 4, 9)
    graph.add_undirected_edge(3, 5, 14)
    graph.add_undirected_edge(4, 5, 10)
    graph.add_undirected_edge(5, 6, 2)
    graph.add_undirected_edge(6, 7, 1)
    graph.add_undirected_edge(6, 8, 6)
    graph.add_undirected_edge(7, 8, 7)
    dijkstra(graph, 0)
    prims(graph)


""" prims
node id 0 prev -1 distance : 0
node id 1 prev 0 distance : 4
node id 2 prev 1 distance : 8
node id 3 prev 2 distance : 7
node id 4 prev 3 distance : 9
node id 5 prev 2 distance : 4
node id 6 prev 5 distance : 2
node id 7 prev 6 distance : 1
node id 8 prev 2 distance : 2
"""

"""dijkstra
node id 0 prev -1 distance : 0
node id 1 prev 0 distance : 4
node id 2 prev 1 distance : 12
node id 3 prev 2 distance : 19
node id 4 prev 5 distance : 21
node id 5 prev 6 distance : 11
node id 6 prev 7 distance : 9
node id 7 prev 0 distance : 8
node id 8 prev 2 distance : 14
"""

def hamiltonian_cycle_util(graph , path, added):
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
            if hamiltonian_cycle_util(graph, path, added):
                return True
            # backtracking
            path.pop()
            added[vertex] = False
    return False

def hamiltonian_cycle(graph):
    path = []
    path.append(0)
    added = [False]*graph.count
    added[0] = True
    if hamiltonian_cycle_util(graph, path, added):
        print("Hamiltonian Cycle found", path)
        return True
    print("Hamiltonian Cycle not found")
    return False

def hamiltonian_path_util(graph , path, added):
    # Base case: full length path is found 
    if len(path) == graph.count:
            return True
    
    for vertex in range(graph.count):
        # there is a path from last element and next vertex 
        # and next vertex is not already included in path.
        if graph.adj[path[-1]][vertex] == 1 and added[vertex] == False:
            path.append(vertex)
            added[vertex] = True
            if hamiltonian_path_util(graph, path, added):
                return True
            # backtracking
            path.pop()
            added[vertex] = False
    return False

def hamiltonian_path(graph):
    path = []
    path.append(0)
    added = [False]*graph.count
    added[0] = True
    if hamiltonian_path_util(graph, path, added):
        print("Hamiltonian Path found", path)
        return True
    print("Hamiltonian Path not found")
    return False

# Testing code
def test3():
    graph = Graph(5)
    graph.adj = [ [0, 1, 0, 1, 0], 
                    [1, 0, 1, 1, 0], 
                    [0, 1, 0, 0, 1,],
                    [1, 1, 0, 0, 1], 
                    [0, 1, 1, 1, 0] ]
    print(hamiltonian_path(graph))

    g2 = Graph(5)
    g2.adj = [ [0, 1, 0, 1, 0], 
                [1, 0, 1, 1, 0], 
                [0, 1, 0, 0, 1,], 
                [1, 1, 0, 0, 0], 
                [0, 1, 1, 0, 0] ]
    
    print(hamiltonian_path(g2))


"""
Hamiltonian Path found [0, 1, 2, 4, 3]
True
Hamiltonian Path found [0, 3, 1, 2, 4]
True
"""

# Testing code
def test4():
    graph = Graph(5)
    graph.adj = [ [0, 1, 0, 1, 0], 
                    [1, 0, 1, 1, 0], 
                    [0, 1, 0, 0, 1],
                    [1, 1, 0, 0, 1], 
                    [0, 1, 1, 1, 0] ]
    print(hamiltonian_cycle(graph))

    g2 = Graph(5)
    g2.adj = [ [0, 1, 0, 1, 0], 
                [1, 0, 1, 1, 0], 
                [0, 1, 0, 0, 1], 
                [1, 1, 0, 0, 0], 
                [0, 1, 1, 0, 0] ]
    
    print(hamiltonian_cycle(g2))


"""
Hamiltonian Cycle found [0, 1, 2, 4, 3, 0]
True
Hamiltonian Cycle not found
False
"""

test1()
test2()
test3()
test4()