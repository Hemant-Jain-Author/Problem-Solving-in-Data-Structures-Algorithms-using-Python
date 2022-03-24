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
            print(f"Vertex {i} is connected to:", end=' ')
            for j in range(self.count):
                if self.adj[i][j] != 0:
                    print(f"{j}(cost:{self.adj[i][j]})", end =" ")
            print()

    def print_path_util(self, previous, source, dest) :
        if (dest == source) :
            print(source, end="")
        else :
            self.print_path_util(previous, source, previous[dest])
            print(f"->{dest}", end="")

    def print_path(self, previous, dist, count, source) :
        print("Shortest Paths : ", end="")
        for i in range(count) :
            if (dist[i] == sys.maxsize) :
                print(f"({source}->{i} @ Unreachable)", end="")
            elif(i != previous[i]) :
                print("(", end="")
                self.print_path_util(previous, source, i)
                print(f" @ {dist[i]}) ", end="")
        print()

    def dijkstra(self, source):
        previous = [-1] * self.count
        dist = [sys.maxsize] * self.count
        visited = [False] * self.count
        dist[source] = 0
        previous[source] = 0
        
        pq = PriorityQueue()
        for i in range(self.count):
            pq.add(sys.maxsize, i)
        pq.update_key(0, source)
        
        while pq.size() != 0:
            val = pq.pop()
            src = val[1]
            visited[src] = True
            
            for dest in range(self.count):
                alt = self.adj[src][dest] + dist[src]
                if self.adj[src][dest] > 0 and alt < dist[dest] and visited[dest] == False:
                    dist[dest] = alt
                    previous[dest] = src
                    pq.update_key(alt, dest)


        self.print_path(previous, dist, self.count, source)

    def prims_mst(self):
        previous = [-1] * self.count
        dist = [sys.maxsize] * self.count
        visited = [False] * self.count
        source = 0
        dist[source] = 0
        previous[source] = 0
        pq = PriorityQueue()
        
        for i in range(self.count):
            pq.add(sys.maxsize, i)
        pq.update_key(0, source)
        
        while pq.size() != 0:
            val = pq.pop()
            source = val[1]
            visited[source] = True
            
            for dest in range(self.count):
                alt = self.adj[source][dest]
                if self.adj[source][dest] > 0 and alt < dist[dest] and visited[dest] == False:
                    dist[dest] = alt
                    previous[dest] = source
                    pq.update_key(alt, dest)
        
        total_cost = 0
        print("Edges are : ", end="")
        for i in range(self.count):
            if dist[i] == sys.maxsize:
                print("(", previous[i], "->", i , "@ Unreachable )", end="")
            elif i != previous[i]:
                print("(", previous[i], "->", i , "@" , dist[i], ")", end="")
                total_cost += dist[i]
        print("\nTotal MST cost: ", total_cost)


    def hamiltonian_cycle_util(self, path, added):
        # Base case: full length path is found 
        # this last check can be modified to make it a path.
        if len(path) == self.count:
            if self.adj[ path[-1] ][ path[0] ] == 1:
                path.append(path[0])
                return True
            else:
                return False
        
        for vertex in range(self.count):
            # there is a path from last element and next vertex 
            if self.adj[path[-1]][vertex] == 1 and added[vertex] == False:
                path.append(vertex)
                added[vertex] = True
                if self.hamiltonian_cycle_util(path, added):
                    return True
                # backtracking
                path.pop()
                added[vertex] = False
        return False

    def hamiltonian_cycle(self):
        path = []
        path.append(0)
        added = [False]*self.count
        added[0] = True
        if self.hamiltonian_cycle_util(path, added):
            print("Hamiltonian Cycle found", path)
            return True
        print("Hamiltonian Cycle not found")
        return False

    def hamiltonian_path_util(self , path, added):
        # Base case: full length path is found 
        if len(path) == self.count:
                return True
        
        for vertex in range(self.count):
            # there is a path from last element and next vertex 
            # and next vertex is not already included in path.
            if self.adj[path[-1]][vertex] == 1 and added[vertex] == False:
                path.append(vertex)
                added[vertex] = True
                if self.hamiltonian_path_util(path, added):
                    return True
                # backtracking
                path.pop()
                added[vertex] = False
        return False

    def hamiltonian_path(self):
        path = []
        path.append(0)
        added = [False]*self.count
        added[0] = True
        if self.hamiltonian_path_util(path, added):
            print("Hamiltonian Path found", path)
            return True
        print("Hamiltonian Path not found")
        return False


# Testing code
def test1():
    gph = Graph(4)
    gph.add_undirected_edge(0, 1)
    gph.add_undirected_edge(0, 2)
    gph.add_undirected_edge(1, 2)
    gph.add_undirected_edge(2, 3)
    gph.print()

"""
Vertex 0 is connected to: 1(cost:1) 2(cost:1) 
Vertex 1 is connected to: 0(cost:1) 2(cost:1) 
Vertex 2 is connected to: 0(cost:1) 1(cost:1) 3(cost:1) 
Vertex 3 is connected to: 2(cost:1) 
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

# Testing code
def test2():
    gph = Graph(9)
    gph.add_undirected_edge(0, 1, 4)
    gph.add_undirected_edge(0, 7, 8)
    gph.add_undirected_edge(1, 2, 8)
    gph.add_undirected_edge(1, 7, 11)
    gph.add_undirected_edge(2, 3, 7)
    gph.add_undirected_edge(2, 8, 2)
    gph.add_undirected_edge(2, 5, 4)
    gph.add_undirected_edge(3, 4, 9)
    gph.add_undirected_edge(3, 5, 14)
    gph.add_undirected_edge(4, 5, 10)
    gph.add_undirected_edge(5, 6, 2)
    gph.add_undirected_edge(6, 7, 1)
    gph.add_undirected_edge(6, 8, 6)
    gph.add_undirected_edge(7, 8, 7)
    gph.dijkstra(0)
    gph.prims_mst()


""" prims_mst
Edges are : ( 0 -> 1 @ 4 )( 1 -> 2 @ 8 )( 2 -> 3 @ 7 )( 3 -> 4 @ 9 )( 2 -> 5 @ 4 )( 5 -> 6 @ 2 )( 6 -> 7 @ 1 )( 2 -> 8 @ 2 )
Total MST cost:  37
"""
"""dijkstra
Shortest Paths : (0->1 @ 4) (0->1->2 @ 12) (0->1->2->3 @ 19) (0->7->6->5->4 @ 21) (0->7->6->5 @ 11) (0->7->6 @ 9) (0->7 @ 8) (0->1->2->8 @ 14) 
"""

# Testing code
def test3():
    gph = Graph(5)
    gph.adj = [ [0, 1, 0, 1, 0], 
                [1, 0, 1, 1, 0], 
                [0, 1, 0, 0, 1,],
                [1, 1, 0, 0, 1], 
                [0, 1, 1, 1, 0] ]
    print(gph.hamiltonian_path())

    g2 = Graph(5)
    g2.adj = [ [0, 1, 0, 1, 0], 
               [1, 0, 1, 1, 0], 
               [0, 1, 0, 0, 1,], 
               [1, 1, 0, 0, 0], 
               [0, 1, 1, 0, 0] ]
    
    print(g2.hamiltonian_path())


"""
Hamiltonian Path found [0, 1, 2, 4, 3]
True
Hamiltonian Path found [0, 3, 1, 2, 4]
True
"""

# Testing code
def test4():
    gph = Graph(5)
    gph.adj = [ [0, 1, 0, 1, 0], 
                [1, 0, 1, 1, 0], 
                [0, 1, 0, 0, 1],
                [1, 1, 0, 0, 1], 
                [0, 1, 1, 1, 0] ]
    print(gph.hamiltonian_cycle())

    g2 = Graph(5)
    g2.adj = [ [0, 1, 0, 1, 0], 
               [1, 0, 1, 1, 0], 
               [0, 1, 0, 0, 1], 
               [1, 1, 0, 0, 0], 
               [0, 1, 1, 0, 0] ]
    
    print(g2.hamiltonian_cycle())


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