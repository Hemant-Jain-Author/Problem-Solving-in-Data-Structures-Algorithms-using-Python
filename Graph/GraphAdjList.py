import heapq
import sys
from collections import deque

class Graph(object):
    def __init__(self, cnt):
        self.count = cnt
        self.adj = [[] for _ in range(cnt)]
    
    def add_directed_edge(self, source, destination, cost=1):
        edge = (destination, cost)
        self.adj[source].append(edge)
    
    def add_undirected_edge(self, source, destination, cost=1):
        self.add_directed_edge(source, destination, cost)
        self.add_directed_edge(destination, source, cost)

    def print(self):
        for i in range(self.count):
            print("Vertex", i, "is connected to:", end=' ')
            for edge in self.adj[i]:
                print(edge[0], "(cost:", edge[1], ")", end=' ')
            print()

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
        # this is a dummy function actual implimentation 
        # tbd
        heapq.heappush(self.que, (key, value))

    def pop(self):
        val = heapq.heappop(self.que)
        return val

    def size(self):
        return len(self.que)

def dfs_util(gph, index, visited):
    visited[index] = True
    for edge in gph.adj[index]:
        destination = edge[0]
        if visited[destination] == False:
            dfs_util(gph, destination, visited)


def dfs_stack(gph, source, target):
    count = gph.count
    visited = [False] * count
    stk = []
    stk.append(source)
    visited[source] = True
    while len(stk) != 0:
        curr = stk.pop()
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                stk.append(destination)
                visited[destination] = True
    return visited[target]
            
def dfs(gph, source, target):
    count = gph.count
    visited = [False] * count
    dfs_util(gph, source, visited)
    return visited[target]
 
def bfs(gph, source, target):
    count = gph.count
    visited = [False] * count
    visited[source] = True
    que = deque([])
    que.append(source)
    while len(que) != 0:
        curr = que.popleft()
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                que.append(destination)
                visited[destination] = True
    return visited[target]

# Testing code
def test2():
    gph =  Graph(8)
    gph.add_undirected_edge(0, 1)
    gph.add_undirected_edge(0, 2)
    gph.add_undirected_edge(0, 3)
    gph.add_undirected_edge(1, 4)
    gph.add_undirected_edge(2, 5)
    gph.add_undirected_edge(3, 6)
    gph.add_undirected_edge(4, 7)
    gph.add_undirected_edge(5, 7)
    gph.add_undirected_edge(6, 7)
    print("Path between 0 & 6:", dfs(gph, 0, 6))
    print("Path between 0 & 6:", bfs(gph, 0, 6))
    print("Path between 0 & 6:", dfs_stack(gph, 0, 6))

"""
Path between 0 & 6: True
Path between 0 & 6: True
Path between 0 & 6: True
"""

def topological_sort_dfs(gph, index, visited, stk):
    visited[index] = True
    for edge in gph.adj[index]:
        destination = edge[0]
        if visited[destination] == False:
            topological_sort_dfs(gph, destination, visited, stk)
    stk.append(index)

def topological_sort(gph):
    stk = []
    count = gph.count
    visited = [False] * count
    for i in range(count):
        if visited[i] == False:
            topological_sort_dfs(gph, i, visited, stk)
    print("topological_sort::", end=' ')
    while len(stk) != 0:
        print(stk.pop(), end=' ') 
    print("")

# Testing code
def test3():
    gph = Graph(9)
    gph.add_directed_edge(0, 2)
    gph.add_directed_edge(1, 2)
    gph.add_directed_edge(1, 3)
    gph.add_directed_edge(1, 4)
    gph.add_directed_edge(3, 2)
    gph.add_directed_edge(3, 5)
    gph.add_directed_edge(4, 5)
    gph.add_directed_edge(4, 6)
    gph.add_directed_edge(5, 7)
    gph.add_directed_edge(6, 7)
    gph.add_directed_edge(7, 8)
    topological_sort(gph)

# topologicalSort ::  1 4 6 3 5 7 8 0 2

def path_exist(gph, source, destination):
    count = gph.count
    visited = [False] * count
    dfs_util(gph, source, visited)
    return visited[destination]

def count_all_path_dfs(gph, visited, source ,dest):
    if source == dest:
        return 1

    count = 0
    visited[source] = 1
    for edge in gph.adj[source]:
        if visited[edge[0]] == 0:
            count += count_all_path_dfs(gph, visited, edge[0], dest)
    visited[source] = 0
    return count

def count_all_path(gph, src ,dest):
    visited = [0]*gph.count
    return count_all_path_dfs(gph, visited, src, dest)

def print_all_path_dfs(gph, visited, source ,dest, path):
    path.append(source)
    if source == dest:
        print(path)
        path.pop()
        return

    visited[source] = 1
    for edge in gph.adj[source]:
        if visited[edge[0]] == 0:
            print_all_path_dfs(gph, visited, edge[0], dest, path)
    visited[source] = 0
    path.pop()

def print_all_path(gph, src ,dest):
    visited = [0]*gph.count
    path = []
    print_all_path_dfs(gph, visited, src, dest, path)

# Testing code
def test4():
    gph = Graph(5)
    gph.add_directed_edge(0, 1, 1)
    gph.add_directed_edge(0, 2, 1)
    gph.add_directed_edge(2, 3, 1)
    gph.add_directed_edge(1, 3, 1)
    gph.add_directed_edge(3, 4, 1)
    gph.add_directed_edge(1, 4, 1)
    print("path_exist::", path_exist(gph, 0, 4))
    print("Path Count::", count_all_path(gph, 0, 4))
    print_all_path(gph, 0, 4)

"""
path_exist ::  True
Path Count ::  3
[0, 1, 3, 4]
[0, 1, 4]
[0, 2, 3, 4]
"""

def dfs_util(gph, index, visited):
    visited[index] = True
    for edge in gph.adj[index]:
        if visited[edge[0]] == False:
            dfs_util(gph, edge[0], visited)

def root_vertex(gph):
    count = gph.count
    visited = [False] * count
    retVal = -1
    for i in range(count):
        if visited[i] == False:
            dfs_util(gph, i, visited)
            retVal = i
    print("Root vertex is :: ", retVal)

# Testing code
def test5():
    g = Graph(7)
    g.add_directed_edge(0, 1)
    g.add_directed_edge(0, 2)
    g.add_directed_edge(1, 3)
    g.add_directed_edge(4, 1)
    g.add_directed_edge(6, 4)
    g.add_directed_edge(5, 6)
    g.add_directed_edge(5, 2)
    g.add_directed_edge(6, 0)
    root_vertex(g)

# Root vertex is ::  5


def transitive_closure_util(gph, source ,index, tc):
    if tc[source][index] == 1:
        return
    tc[source][index] = 1
    for edge in gph.adj[index]:
            transitive_closure_util(gph, source, edge[0], tc)

def transitive_closure(gph):
    count = gph.count
    tc = [[0 for _ in range(count)] for _ in range(count)]
    for source in range(count):
        transitive_closure_util(gph, source, source, tc)
    for row in tc:
        print(row)
    return tc

# Testing code
def test6():
    g = Graph(4)
    g.add_directed_edge(0, 1)
    g.add_directed_edge(0, 2)
    g.add_directed_edge(1, 2)
    g.add_directed_edge(2, 0)
    g.add_directed_edge(2, 3)
    g.add_directed_edge(3, 3)
    transitive_closure(g)

"""
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
[0, 0, 0, 1]
"""


def bfs_distance(gph, source, dest):
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
                return depth+1
            if visited[edge[0]] == False:
                que.append((edge[0], depth+1))
                visited[edge[0]] = True
    return -1

def bfs_level_node(gph, source):
    count = gph.count
    visited = [False] * count
    visited[source] = True
    que = deque([])
    que.append((source, 0))
    print("\nNode  - Level")
    while len(que) != 0:
        node = que.popleft()
        curr = node[0]
        depth = node[1]
        print(curr ," - ", depth)
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                que.append((destination, depth+1))
                visited[destination] = True

# Testing code
def test7():
    g = Graph(7)
    g.add_undirected_edge(0, 1)
    g.add_undirected_edge(0, 2)
    g.add_undirected_edge(0, 4)
    g.add_undirected_edge(1, 2)
    g.add_undirected_edge(2, 5)
    g.add_undirected_edge(3, 4)
    g.add_undirected_edge(4, 5)
    g.add_undirected_edge(4, 6)
    print(bfs_distance(g, 1, 6))
    bfs_level_node(g, 1)


# 3
"""
Node  - Level
1  -  0
0  -  1
2  -  1
4  -  2
5  -  2
3  -  3
6  -  3
"""

def is_cycle_present_undirected_dfs(graph, index, parentIndex, visited):
    visited[index] = True
    for node in graph.adj[index]:
        dest = node[0]
        if visited[dest] == False:
            if is_cycle_present_undirected_dfs(graph, dest, index, visited) :
                return True
        elif parentIndex != dest :
            return True
    return False


def is_cycle_present_undirected(graph):
    count = graph.count
    visited = [False] * count
    for index in range(count):
        if visited[index] == False:
            if is_cycle_present_undirected_dfs(graph, index, -1, visited) :
                return True
    return False




def find2(parent,  index) :
    p = parent[index]
    while (p != -1) :
        index = p
        p = parent[index]
    return  index

def union2(parent,  x,  y) :
    parent[y] = x

def is_cycle_present_undirected2(gph) :
    count = gph.count
    parent = [-1] * count
    edge =  []
    flags = [[False] * count for _ in range(count)]
    i = 0
    while (i < count) :
        ad = gph.adj[i]
        for adn in ad :
            #  Using flags[][] list, if considered edge x to y, then ignore edge y to x.
            if (flags[adn[0]][i] == False) :
                edge.append((i, adn[0]))
                flags[i][adn[0]] = True
        i += 1
    for e in edge:
        x = find2(parent, e[0])
        y = find2(parent, e[1])
        if (x == y) :
            return  True
        union2(parent, x, y)
    return  False

class Sets :
    def __init__(self, p,  r) :
        self.parent = p
        self.rank = r

def find(sets,  index) :
    p = sets[index].parent
    while (p != index) :
        index = p
        p = sets[index].parent
    return  index

#  consider x and y are roots of sets.
def union(sets,  x,  y) :
    if (sets[x].rank < sets[y].rank) : 
        sets[x].parent = y
    elif (sets[y].rank < sets[x].rank) : 
        sets[y].parent = x
    else :
        sets[x].parent = y
        sets[y].rank += 1


def is_cycle_present_undirected3(gph) :
    count = gph.count
    # Different subsets are created.
    sets = [None] * count
    i = 0
    while (i < count) :
        sets[i] = Sets(-1, 0)    
        i += 1
    edge =  []
    flags = [[False] * count for _ in range(count)]
    i = 0
    while (i < count) :
        ad = gph.adj[i]
        for adn in ad:
            #  Using flags[][] list, if considered edge x to y, 
            #  then ignore edge y to x.
            if (flags[adn[0]][i] == False) :
                edge.append((i, adn[0]))
                flags[i][adn[0]] = True
        i += 1
    for e in edge:
        x = find(sets, e[0])
        y = find(sets, e[1])
        if (x == y) :
            return  True
        union(sets, x, y)
    return  False

def is_connected_undirected(gph):
    count = gph.count
    visited = [False] * count
    dfs_util(gph, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True

# Testing code
def test8():
    g = Graph(6)
    g.add_undirected_edge(0, 1)
    g.add_undirected_edge(1, 2)
    g.add_undirected_edge(3, 4)
    g.add_undirected_edge(4, 2)
    g.add_undirected_edge(2, 5)
    #g.add_undirected_edge(3, 5)
    print(is_cycle_present_undirected(g))
    print(is_cycle_present_undirected2(g))
    print(is_cycle_present_undirected3(g))
    print("is_connected_undirected : ", is_connected_undirected(g))

"""
False
is_connected_undirected :  True
"""

def is_cycle_present_dfs(graph, index, visited, marked):
    visited[index] = True
    marked[index] = True

    for node in graph.adj[index]:
        dest = node[0]
        if marked[dest] == True:
            return True

        if visited[dest] == False:
            if is_cycle_present_dfs(graph, dest, visited, marked) :
                return True
        
    marked[index] = False
    return False

def is_cycle_present(graph):
    count = graph.count
    visited = [False] * count
    marked = [False] * count
    for index in range(count):
        if visited[index] == False:
            if is_cycle_present_dfs(graph, index, visited, marked) :
                return True
    return False


def is_cycle_present_color_dfs(graph, index, visited):
    visited[index] = "Grey"
    for node in graph.adj[index]:
        dest = node[0]
        if visited[dest] == "Grey":
            return True
            
        if visited[dest] == "White":
            if is_cycle_present_color_dfs(graph, dest, visited) :
                return True     
    visited[index] = "Black"
    return False

def is_cycle_present_color(graph):
    count = graph.count
    visited = ["White"] * count
    for index in range(count):
        if visited[index] == "White":
            if is_cycle_present_color_dfs(graph, index, visited) :
                return True
    return False

# Testing code
def test9():
    g = Graph(5)
    g.add_directed_edge(0, 1)
    g.add_directed_edge(0, 2)
    g.add_directed_edge(1, 3)
    g.add_directed_edge(2, 3)
    g.add_directed_edge(3, 4)
    # g.add_directed_edge(4, 1)
    print(is_cycle_present(g))
    print(is_cycle_present_color(g))

# False
# False

def transpose_graph(gph):
    count = gph.count
    g = Graph(count)
    for i in range(count):
        for edge in gph.adj[i]:
            destination = edge[0]
            g.add_directed_edge(destination, i)
    return g

# Testing code
def test10():
    g = Graph(4)
    g.add_directed_edge(0, 1)
    g.add_directed_edge(0, 2)
    g.add_directed_edge(1, 2)
    g.add_directed_edge(2, 3)
    g = transpose_graph(g)
    g.print()


"""
Vertex 0 is connected to: 
Vertex 1 is connected to: 0 (cost: 1 ) 
Vertex 2 is connected to: 0 (cost: 1 ) 1 (cost: 1 ) 
Vertex 3 is connected to: 2 (cost: 1 )  
"""

def is_strongly_connected(gph):
    count = gph.count
    visited = [False] * count
    dfs_util(gph, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    graph_reversed = transpose_graph(gph)
    visited = [False] * count
    dfs_util(graph_reversed, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True

# Testing code
def test11():
    # Create a graph given in the above diagram
    g1 = Graph(5)
    g1.add_directed_edge(0, 1)
    g1.add_directed_edge(1, 2)
    g1.add_directed_edge(2, 3)
    g1.add_directed_edge(3, 0)
    g1.add_directed_edge(2, 4)
    g1.add_directed_edge(4, 2)
    print(is_strongly_connected(g1))
    
    g2 = Graph(4)
    g2.add_directed_edge(0, 1)
    g2.add_directed_edge(1, 2)
    g2.add_directed_edge(2, 3)
    print(is_strongly_connected(g2))

"""
True
False
"""

def dfs_util2(gph, index, visited, stk):
    visited[index] = True
    for edge in gph.adj[index]:
        destination = edge[0]
        if visited[destination] == False:
            dfs_util2(gph, destination, visited, stk)
    stk.append(index)

def strongly_connected_component(gph):
    count = gph.count
    visited = [False] * count
    stk = []
    for i in range(count):
        if visited[i] == False:
            dfs_util2(gph, i, visited, stk)
    
    graph_reversed = transpose_graph(gph)
    visited = [False] * count
    while len(stk) != 0:
        index = stk.pop()
        if visited[index] == False:
            stk2 = []
            dfs_util2(graph_reversed, index, visited, stk2)
            print(stk2)

# Testing code
def test12():
    graph = Graph(7)
    graph.add_directed_edge(0, 1)
    graph.add_directed_edge(1, 2)
    graph.add_directed_edge(2, 0)
    graph.add_directed_edge(2, 3)
    graph.add_directed_edge(3, 4)
    graph.add_directed_edge(4, 5)
    graph.add_directed_edge(5, 3)
    graph.add_directed_edge(5, 6)
    strongly_connected_component(graph)

"""
[1, 2, 0]
[4, 5, 3]
[6]
"""

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
        for edge in gph.adj[source]:
            destination = edge[0]
            cost = edge[1]
            alt = cost + dist[source]
            if alt < dist[destination] and visited[destination] == False:
                dist[destination] = alt
                previous[destination] = source
                pq.update_key(alt, destination)

    
    for i in range(gph.count):
        if dist[i] == sys.maxsize:
            print("node id", i, "prev", previous[i], "distance: Unreachable")
        else:
            print("node id", i, "prev", previous[i], "distance:", dist[i])


def primsMST(gph):
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

        for edge in gph.adj[source]:
            destination = edge[0]
            cost = edge[1]
            if cost < dist[destination] and visited[destination] == False:
                dist[destination] = cost
                previous[destination] = source
                pq.update_key(cost, destination)
    
    total_cost = 0

    for i in range(gph.count):
        if dist[i] == sys.maxsize:
            print("node id" , i , "prev" , previous[i] , "distance : Unreachable")
        else:
            print("node id" , i , "prev" , previous[i] , "distance :" , dist[i])
            total_cost += dist[i]

    print("Total MST cost: ", str(total_cost))

# Testing code
def test13():
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
    primsMST(graph)
    kruskalMST(graph)
    #dijkstra(graph, 0)


""" primsMST
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




def kruskalMST(gph) :
    count = gph.count
    # Different subsets are created.
    sets = []
    for i in range(count) :
        sets.append(Sets(i, 0))    
        
    #  Edges are added to list and sorted.
    edges = []

    for i in range(count)  :
        for adn in gph.adj[i]:
            edges.append((i, adn[0], adn[1]))
    E = len(edges)

    edges.sort(key=lambda edge : edge[2])
    sum = 0
    output =  []
    i = 0
    while (i < E) :
        x = find(sets, edges[i][0])
        y = find(sets, edges[i][1])
        if (x != y) :
            print("(", edges[i][0], "," , edges[i][1], ",", edges[i][2], ")", end ="")
            sum += edges[i][2]
            output.append(edges[i])
            union(sets, x, y)
        i += 1
    print("\nTotal MST cost: ", str(sum))
   

def shortest_path(gph, source):
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

# Testing code
def test14():
    gph = Graph(9)
    gph.add_directed_edge(0, 1, 4)
    gph.add_directed_edge(0, 7, 8)
    gph.add_directed_edge(1, 2, 8)
    gph.add_directed_edge(1, 7, 11)
    gph.add_directed_edge(2, 3, 7)
    gph.add_directed_edge(2, 8, 2)
    gph.add_directed_edge(2, 5, 4)
    gph.add_directed_edge(3, 4, 9)
    gph.add_directed_edge(3, 5, 14)
    gph.add_directed_edge(4, 5, 10)
    gph.add_directed_edge(5, 6, 2)
    gph.add_directed_edge(6, 7, 1)
    gph.add_directed_edge(6, 8, 6)
    gph.add_directed_edge(7, 8, 7)
    shortest_path(gph, 0)


"""
-1 to 0 weight 0
0 to 1 weight 1
1 to 2 weight 2
2 to 3 weight 3
3 to 4 weight 4
2 to 5 weight 3
5 to 6 weight 4
0 to 7 weight 1
7 to 8 weight 2
"""

def bellman_ford_shortest_path(gph, source):
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
        print(path[i] , "to" , i , "weight" , distance[i])

# Testing code
def test15():
    g = Graph(5)
    g.add_directed_edge(0, 1, 3)
    g.add_directed_edge(0, 4, 2)
    g.add_directed_edge(1, 2, 1)
    g.add_directed_edge(2, 3, 1)
    g.add_directed_edge(4, 1, -2)
    g.add_directed_edge(4, 3, 1)
    bellman_ford_shortest_path(g, 0)

"""
-1 to 0 weight 0
4 to 1 weight 0
1 to 2 weight 1
2 to 3 weight 2
0 to 4 weight 2
"""

def height_tree_parent_arr(arr):
    count = len(arr)
    gph = Graph(count)
    for i in range(len(arr)):
        if arr[i] != -1 :
            gph.add_directed_edge(arr[i], i)
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

def get_height(arr, height, index):
    if arr[index] == -1:
        return 0
    else:
        return get_height(arr, height, arr[index]) + 1

def height_tree_parent_arr2(arr):
    count = len(arr)
    height = [-1] * count
    maxHeight = -1
    for i in range(len(arr)):
        height[i] = get_height(arr, height, i)
        maxHeight = max(maxHeight, height[i])
    return maxHeight

# Testing code
def test16():
    parentArray = [-1, 0, 1, 2, 3]
    print(height_tree_parent_arr(parentArray))
    print(height_tree_parent_arr2(parentArray))
    parentArray = [-1, 0, 0, 0, 3, 1, 1, 2]
    print(height_tree_parent_arr(parentArray))
    print(height_tree_parent_arr2(parentArray))


"""
4
4
2
2
"""

def is_connected(graph):
    count = graph.count
    visited =[False]*count
 
    # Find a vertex with non-zero degree
    for i in range(count):
        if len(graph.adj[i]) > 1:
            # dfs traversal of graph from a vertex with non-zero degree
            dfs_util(graph, i, visited)
            break

    # Check if all non-zero degree vertices are visited
    for i in range(count):
        if visited[i]==False and len(graph.adj[i]) > 0:
            return False
        
    return True


def is_eulerian(graph):
    count = graph.count
    # Check if all non-zero degree vertices are connected
    if is_connected(graph) == False:
        print("graph is not Eulerian")
        return 0
    else:
        # Count vertices with odd degree
        odd = 0
        for i in range(count):
            if len(graph.adj[i]) % 2 !=0:
                odd +=1

        if odd > 2:
            print("graph is not Eulerian")
            return 0
        elif odd == 2:
            print("graph is Semi-Eulerian")
            return 1
        elif odd == 0:
            print("graph is Eulerian")
            return 2

# Testing code
def test17():
    g1 = Graph(5)
    g1.add_undirected_edge(1, 0)
    g1.add_undirected_edge(0, 2)
    g1.add_undirected_edge(2, 1)
    g1.add_undirected_edge(0, 3)
    g1.add_undirected_edge(3, 4)
#    g1.add_undirected_edge(4, 0)
#    g1.add_undirected_edge(1, 3)
    is_eulerian(g1)

# graph is Semi-Eulerian

def is_strongly_connected2(graph):
    count = graph.count
    visited = [False] * count
    
        # Find a vertex with non-zero degree
    for index in range(count):
        if len(graph.adj[index]) > 1:
            break
    # dfs traversal of graph from a vertex with non-zero degree
    dfs_util(graph, index, visited)
            
    for i in range(count):
        if visited[i] == False and len(graph.adj[i]) > 0:
            return False

    graph_reversed = transpose_graph(graph)
    visited = [False] * count
    dfs_util(graph_reversed, index, visited)
    
    for i in range(count):
        if visited[i] == False and len(graph.adj[i]) > 0:
            return False
    return True

def is_eulerian_cycle(graph):
    # Check if all non-zero degree vertices 
    # are connected
    if is_strongly_connected2(graph) == False:
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

# Testing code
def test18():
    g = Graph(5)
    g.add_directed_edge(0, 1)
    g.add_directed_edge(1, 2)
    g.add_directed_edge(2, 0)
    g.add_directed_edge(0, 4)
    g.add_directed_edge(4, 3)
    g.add_directed_edge(3, 0)
    print(is_eulerian_cycle(g))

# True

def best_first_search_pq(gph, source, dest):
    previous = [-1] * gph.count
    dist = [sys.maxsize] * gph.count
    visited = [False] * gph.count
    pq = PriorityQueue()
    dist[source] = 0
    previous[source] = -1
    pq.add(0, source)
    
    while pq.size() != 0:
        val = pq.pop()
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
                pq.add(alt, destination)
    return -1


def root_vertex(gph):
    count = gph.count
    visited = [False] * count
    retVal = -1
    for i in range(count):
        if visited[i] == False:
            dfs_util(gph, i, visited)
            retVal = i
    print("Root vertex is :: ", retVal)

# Testing code
def test19():
    g = Graph(7)
    g.add_directed_edge(0, 1)
    g.add_directed_edge(0, 2)
    g.add_directed_edge(1, 3)
    g.add_directed_edge(4, 1)
    g.add_directed_edge(6, 4)
    g.add_directed_edge(5, 6)
    g.add_directed_edge(5, 2)
    g.add_directed_edge(6, 0)
    root_vertex(g)


"""
Root vertex is ::  5
"""

def floydWarshall(gph) :
    V = gph.count
    INF = sys.maxsize
    dist = [[INF] * (V) for _ in range(V)]
    path = [[-1] * (V) for _ in range(V)]
    
    i = 0
    while (i < V) : 
        path[i][i] = 0
        i += 1
    
    i = 0
    while (i < V) :
        adl = gph.adj[i]
        for adn in adl:
            path[i][adn[0]] = i
            dist[i][adn[0]] = adn[1]
        i += 1
    #  Pick intermediate vertices.
    k = 0
    while (k < V) :
        #  Pick source vertices one by one.
        i = 0
        while (i < V) :
            #  Pick destination vertices.
            j = 0
            while (j < V) :
                #  If we have a shorter path from i to j via k.
                #  then update dist[i][j] and  and path[i][j]
                if (dist[i][k] + dist[k][j] < dist[i][j]) :
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]
                j += 1
            #  dist[i][i] is 0 in the start.
            #  If there is a better path from i to i and is better path then we have -ve cycle.                //
            if (dist[i][i] < 0) :
                print("Negative-weight cycle found.")
                return
            i += 1
        k += 1
    printSolution(dist, path, V)
    
def printSolution(cost,  path,  V) :
    u = 0
    while (u < V) :
        v = 0
        while (v < V) :
            if (u != v and path[u][v] != -1) :
                print("Shortest Path from %d to %d " % (u,v),end ="", sep ="")
                print("Cost:" + str(cost[u][v]) + " Path:", end ="")
                printPath(path, u, v)
                print()
            v += 1
        u += 1

def printPath(path,  u,  v) :
    if (path[u][v] == u) :
        print(str(u) + " " + str(v) + " ", end ="")
        return

    printPath(path, u, path[u][v])
    print(str(v) + " ", end ="")

def test20() :
    gph = Graph(4)
    gph.add_directed_edge(0, 0, 0)
    gph.add_directed_edge(1, 1, 0)
    gph.add_directed_edge(2, 2, 0)
    gph.add_directed_edge(3, 3, 0)
    gph.add_directed_edge(0, 1, 5)
    gph.add_directed_edge(0, 3, 10)
    gph.add_directed_edge(1, 2, 3)
    gph.add_directed_edge(2, 3, 1)
    floydWarshall(gph)

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
test12()
test13()
test14()
test15()
test16()
test17()
test18()
test19()
test20()