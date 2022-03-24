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
            print(f"Vertex {i} is connected to:", end=' ')
            for edge in self.adj[i]:
                print(f"{edge[0]}(cost:{edge[1]})", end=' ')
            print()

    def dfs_util(self, index, visited):
        visited[index] = True
        for edge in self.adj[index]:
            destination = edge[0]
            if visited[destination] == False:
                self.dfs_util(destination, visited)

    def dfs(self, source, target):
        visited = [False] * self.count
        self.dfs_util(source, visited)
        return visited[target]

    def dfs_stack(self, source, target):
        visited = [False] * self.count
        stk = []
        stk.append(source)
        visited[source] = True
        while len(stk) != 0:
            curr = stk.pop()
            for edge in self.adj[curr]:
                destination = edge[0]
                if visited[destination] == False:
                    stk.append(destination)
                    visited[destination] = True
        return visited[target]
        
    def bfs(self, source, target):
        visited = [False] * self.count
        visited[source] = True
        que = deque([])
        que.append(source)
        while len(que) != 0:
            curr = que.popleft()
            for edge in self.adj[curr]:
                destination = edge[0]
                if visited[destination] == False:
                    que.append(destination)
                    visited[destination] = True
        return visited[target]

    def topological_sort_dfs(self, index, visited, stk):
        visited[index] = True
        for edge in self.adj[index]:
            destination = edge[0]
            if visited[destination] == False:
                self.topological_sort_dfs(destination, visited, stk)
        stk.append(index)

    def topological_sort(self):
        count = self.count
        visited = [False] * count
        stk = []
        for i in range(count):
            if visited[i] == False:
                self.topological_sort_dfs(i, visited, stk)
        
        print("topological_sort::", end=' ')
        while len(stk) != 0:
            print(stk.pop(), end=' ') 
        print("")

    def path_exist(self, source, destination):
        count = self.count
        visited = [False] * count
        self.dfs_util(source, visited)
        return visited[destination]

    def count_all_path_dfs(self, visited, source ,dest):
        if source == dest:
            return 1

        count = 0
        visited[source] = 1
        for edge in self.adj[source]:
            if visited[edge[0]] == 0:
                count += self.count_all_path_dfs(visited, edge[0], dest)
        visited[source] = 0
        return count

    def count_all_path(self, src ,dest):
        visited = [0]*self.count
        return self.count_all_path_dfs(visited, src, dest)

    def print_all_path_dfs(self, visited, source ,dest, path):
        path.append(source)
        if source == dest:
            print(path)
            path.pop()
            return

        visited[source] = 1
        for edge in self.adj[source]:
            if visited[edge[0]] == 0:
                self.print_all_path_dfs(visited, edge[0], dest, path)
        visited[source] = 0
        path.pop()

    def print_all_path(self, src ,dest):
        visited = [0]*self.count
        path = []
        self.print_all_path_dfs(visited, src, dest, path)

    def root_vertex(self):
        count = self.count
        visited = [False] * count
        ret_val = -1
        for i in range(count):
            if visited[i] == False:
                self.dfs_util(i, visited)
                ret_val = i
                
        # ret_val may be the root vertex.
        visited = [False] * count
        self.dfs_util(i, visited)
        for i in range(count):
            if visited[i] == False:
                print("Disconnected graph!")
                return -1         
        print("Root vertex is ::", ret_val)
        return ret_val

    def transitive_closure_util(self, source ,index, tc):
        if tc[source][index] == 1:
            return
        tc[source][index] = 1
        for edge in self.adj[index]:
                self.transitive_closure_util(source, edge[0], tc)

    def transitive_closure(self):
        count = self.count
        tc = [[0 for _ in range(count)] for _ in range(count)]
        for source in range(count):
            self.transitive_closure_util(source, source, tc)
        for row in tc:
            print(row)
        return tc

    def bfs_distance(self, source, dest):
        count = self.count
        visited = [False] * count
        visited[source] = True
        que = deque([])
        que.append((source, 0))
        while len(que) != 0:
            node = que.popleft()
            curr = node[0]
            depth = node[1]
            for edge in self.adj[curr]:
                if edge[0] == dest:
                    return depth+1
                if visited[edge[0]] == False:
                    que.append((edge[0], depth+1))
                    visited[edge[0]] = True
        return -1

    def bfs_level_node(self, source):
        count = self.count
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
            for edge in self.adj[curr]:
                destination = edge[0]
                if visited[destination] == False:
                    que.append((destination, depth+1))
                    visited[destination] = True

    def is_cycle_present_dfs(self, index, visited, marked):
        visited[index] = True
        marked[index] = True

        for node in self.adj[index]:
            dest = node[0]
            if marked[dest] == True:
                return True

            if visited[dest] == False:
                if self.is_cycle_present_dfs(dest, visited, marked) :
                    return True
            
        marked[index] = False
        return False

    def is_cycle_present(self):
        count = self.count
        visited = [False] * count
        marked = [False] * count
        for index in range(count):
            if visited[index] == False:
                if self.is_cycle_present_dfs(index, visited, marked) :
                    return True
        return False

    def is_cycle_present_color_dfs(self, index, visited):
        visited[index] = "Grey"
        for node in self.adj[index]:
            dest = node[0]
            if visited[dest] == "Grey":
                return True
                
            if visited[dest] == "White":
                if self.is_cycle_present_color_dfs(dest, visited) :
                    return True     
        visited[index] = "Black"
        return False

    def is_cycle_present_color(self):
        count = self.count
        visited = ["White"] * count
        for index in range(count):
            if visited[index] == "White":
                if self.is_cycle_present_color_dfs(index, visited) :
                    return True
        return False

    def is_cycle_present_undirected_dfs(self, index, parentIndex, visited):
        visited[index] = True
        for node in self.adj[index]:
            dest = node[0]
            if visited[dest] == False:
                if self.is_cycle_present_undirected_dfs(dest, index, visited) :
                    return True
            elif parentIndex != dest :
                return True
        return False

    def is_cycle_present_undirected(self):
        count = self.count
        visited = [False] * count
        for index in range(count):
            if visited[index] == False:
                if self.is_cycle_present_undirected_dfs(index, -1, visited) :
                    return True
        return False

    def find2(self, parent,  index) :
        p = parent[index]
        while (p != -1) :
            index = p
            p = parent[index]
        return  index

    def union2(self, parent,  x,  y) :
        parent[y] = x

    def is_cycle_present_undirected2(self) :
        count = self.count
        parent = [-1] * count
        edge =  []
        flags = [[False] * count for _ in range(count)]

        for i in range(count) :
            ad = self.adj[i]
            for adn in ad :
                #  Using flags[][] list, if considered edge x to y, then ignore edge y to x.
                if (flags[adn[0]][i] == False) :
                    edge.append((i, adn[0]))
                    flags[i][adn[0]] = True

        for e in edge:
            x = self.find2(parent, e[0])
            y = self.find2(parent, e[1])
            if (x == y) :
                return  True
            self.union2(parent, x, y)
        return  False

    class Sets :
        def __init__(self, p,  r) :
            self.parent = p
            self.rank = r

    def find(self, sets,  index) :
        p = sets[index].parent
        while (p != index) :
            index = p
            p = sets[index].parent
        return  index

    #  consider x and y are roots of sets.
    def union(self, sets,  x,  y) :
        if (sets[x].rank < sets[y].rank) : 
            sets[x].parent = y
        elif (sets[y].rank < sets[x].rank) : 
            sets[y].parent = x
        else :
            sets[x].parent = y
            sets[y].rank += 1

    def is_cycle_present_undirected3(self) :
        count = self.count
        # Different subsets are created.
        sets = [None] * count
        for i in range(count) :
            sets[i] =self.Sets(i, 0)    

        edge =  []
        flags = [[False] * count for _ in range(count)]
        for i in range(count) :
            ad = self.adj[i]
            for adn in ad:
                #  Using flags[][] list, if considered edge x to y, 
                #  then ignore edge y to x.
                if (flags[adn[0]][i] == False) :
                    edge.append((i, adn[0]))
                    flags[i][adn[0]] = True

        for e in edge:
            x = self.find(sets, e[0])
            y = self.find(sets, e[1])
            if (x == y) :
                return  True
            self.union(sets, x, y)
        return  False

    def transpose_graph(self):
        count = self.count
        gph = Graph(count)
        for i in range(count):
            for edge in self.adj[i]:
                destination = edge[0]
                gph.add_directed_edge(destination, i)
        return gph

    def is_connected_undirected(self):
        count = self.count
        visited = [False] * count
        self.dfs_util(0, visited)
        for i in range(count):
            if visited[i] == False:
                return False
        return True

    def is_strongly_connected(self):
        count = self.count
        visited = [False] * count
        self.dfs_util(0, visited)
        for i in range(count):
            if visited[i] == False:
                return False
        graph_reversed = self.transpose_graph()
        visited = [False] * count
        graph_reversed.dfs_util(0, visited)
        for i in range(count):
            if visited[i] == False:
                return False
        return True

    def dfs_util2(self, index, visited, stk):
        visited[index] = True
        for edge in self.adj[index]:
            destination = edge[0]
            if visited[destination] == False:
                self.dfs_util2(destination, visited, stk)
        stk.append(index)

    def strongly_connected_component(self):
        count = self.count
        visited = [False] * count
        stk = []
        for i in range(count):
            if visited[i] == False:
                self.dfs_util2(i, visited, stk)
        
        graph_reversed = self.transpose_graph()
        visited = [False] * count
        while len(stk) != 0:
            index = stk.pop()
            if visited[index] == False:
                stk2 = []
                graph_reversed.dfs_util2(index, visited, stk2)
                print(stk2)

    def prims_mst(self):
        previous = [-1] * self.count
        distance = [sys.maxsize] * self.count
        visited = [False] * self.count
        
        source = 0
        distance[source] = 0
        previous[source] = source

        pq = PriorityQueue()
        for i in range(self.count):
            pq.add(sys.maxsize, i)
        pq.update_key(0, source)
        
        while pq.size() != 0:
            val = pq.pop()
            src = val[1]
            visited[src] = True

            for edge in self.adj[src]:
                destination = edge[0]
                cost = edge[1]
                if cost < distance[destination] and visited[destination] == False:
                    distance[destination] = cost
                    previous[destination] = src
                    pq.update_key(cost, destination)
        
        total_cost = 0
        print("Edges are : ", end="")
        for i in range(self.count):
            if distance[i] == sys.maxsize:
                print(f"({previous[i]}->{i} @ Unreachable )", end="")
            elif i != previous[i]:
                print(f"({previous[i]}->{i} @ {distance[i]}) ", end="")
                total_cost += distance[i]

        print("\nTotal MST cost:", total_cost)

    def kruskalMST(self) :
        count = self.count
        # Different subsets are created.
        sets = []
        for i in range(count) :
            sets.append(self.Sets(i, 0))    
            
        #  Edges are added to list and sorted.
        edges = []

        for i in range(count)  :
            for adn in self.adj[i]:
                edges.append((i, adn[0], adn[1]))
        E = len(edges)

        edges.sort(key=lambda edge : edge[2])
        sum = 0
        print("Edges are : ", end="")
        for i in range(E) :
            x = self.find(sets, edges[i][0])
            y = self.find(sets, edges[i][1])
            if (x != y) :
                print(f"({edges[i][0]}->{edges[i][1]} @ {edges[i][2]}) ", end ="")
                sum += edges[i][2]
                self.union(sets, x, y)
        print("\nTotal MST cost:", sum)

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

    def shortest_path(self, source):
        count = self.count
        distance = [sys.maxsize] * count
        previous = [-1] * count

        que = deque([])
        que.append(source)
        distance[source] = 0
        previous[source] = source

        while len(que) != 0:
            curr = que.popleft()
            for edge in self.adj[curr]:
                destination = edge[0]
                if distance[destination] == sys.maxsize:
                    distance[destination] = distance[curr] + 1
                    previous[destination] = curr
                    que.append(destination)

        self.print_path(previous, distance, count, source)

    def dijkstra(self, source):
        previous = [-1] * self.count
        distance = [sys.maxsize] * self.count
        visited = [False] * self.count

        distance[source] = 0
        previous[source] = 0
        pq = PriorityQueue()
        for i in range(self.count):
            pq.add(sys.maxsize, i)
        pq.update_key(0, source)
        
        while pq.size() != 0:
            val = pq.pop()
            src = val[1]
            visited[src] = True
            for edge in self.adj[src]:
                destination = edge[0]
                cost = edge[1]
                alt = cost + distance[src]
                if alt < distance[destination] and visited[destination] == False:
                    distance[destination] = alt
                    previous[destination] = src
                    pq.update_key(alt, destination)

        self.print_path(previous, distance, self.count, source)

    def bellman_ford_shortest_path(self, source):
        count = self.count
        distance = [sys.maxsize] * count
        previous = [-1] * count

        distance[source] = 0
        previous[source] = source

        # Outer loop will run (V-1) number of times. 
        # Inner for loop and loop runs combined will 
        # run for Edges number of times.
        # Which make the total complexity as O(V*E)
        for _ in range(count - 1):
            for j in range(count):
                for edge in self.adj[j]:
                    newDistance = distance[j] + edge[1]
                    if distance[edge[0]] > newDistance:
                        distance[edge[0]] = newDistance
                        previous[edge[0]] = j
        
        self.print_path(previous, distance, count, source)

    def floyd_warshall(self) :
        V = self.count
        distance = [[sys.maxsize] * (V) for _ in range(V)]
        previous = [[-1] * (V) for _ in range(V)]
        
        for i in range(V) : 
            previous[i][i] = i
        
        for i in range(V) :
            adl = self.adj[i]
            for adn in adl:
                previous[i][adn[0]] = i
                distance[i][adn[0]] = adn[1]

        #  Pick intermediate vertices.
        for k in range(V) :
            #  Pick source vertices one by one.
            for i in range(V) :
                #  Pick destination vertices.
                for j in range(V) :
                    #  If we have a shorter path from i to j via k.
                    #  then update dist[i][j] and  and path[i][j]
                    if (distance[i][k] + distance[k][j] < distance[i][j]) :
                        distance[i][j] = distance[i][k] + distance[k][j]
                        previous[i][j] = previous[k][j]
                #  dist[i][i] is 0 in the start.
                #  If there is a better path from i to i and is better path then we have -ve cycle.                //
                if (distance[i][i] < 0) :
                    print("Negative-weight cycle found.")
                    return
        self.print_solution(distance, previous, V)

    def print_solution(self, distance,  previous,  V) :
        print("Shortest Paths : ", end="")
        for u in range(V) :
            for v in range(V) :
                if (u != v and previous[u][v] != -1) :
                    print("(", end="")
                    self.print_path2(previous, u, v)
                    print(f" @ {distance[u][v]} ) ", end ="")
        print()

    def print_path2(self, previous,  u,  v) :
        if (previous[u][v] == u) :
            print(f"{u}->{v}", end ="")
            return
        self.print_path2(previous, u, previous[u][v])
        print(f"->{v}", end ="")


    def is_connected(self):
        count = self.count
        visited =[False]*count

        # Find a vertex with non-zero degree
        for i in range(count):
            if len(self.adj[i]) > 1:
                # dfs traversal of graph from a vertex with non-zero degree
                self.dfs_util(i, visited)
                break

        # Check if all non-zero degree vertices are visited
        for i in range(count):
            if visited[i]==False and len(self.adj[i]) > 0:
                return False
            
        return True

    def is_eulerian(self):
        count = self.count
        # Check if all non-zero degree vertices are connected
        if self.is_connected() == False:
            print("graph is not Eulerian")
            return 0
        else:
            # Count vertices with odd degree
            odd = 0
            for i in range(count):
                if len(self.adj[i]) % 2 !=0:
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

    def is_strongly_connected2(self):
        count = self.count
        visited = [False] * count
        
            # Find a vertex with non-zero degree
        for index in range(count):
            if len(self.adj[index]) > 1:
                break
        # dfs traversal of graph from a vertex with non-zero degree
        self.dfs_util(index, visited)
                
        for i in range(count):
            if visited[i] == False and len(self.adj[i]) > 0:
                return False

        graph_reversed = self.transpose_graph()
        visited = [False] * count
        graph_reversed.dfs_util(index, visited)
        
        for i in range(count):
            if visited[i] == False and len(self.adj[i]) > 0:
                return False
        return True

    def is_eulerian_cycle(self):
        # Check if all non-zero degree vertices 
        # are connected
        if self.is_strongly_connected2() == False:
            return False
        count = self.count
        inDegree = [0] * count
        outDegree = [0] * count

        # Check if in degree and out degree of 
        # every vertex is same
        for i in range(count):
            outDegree[i] = len(self.adj[i])
            for j in self.adj[i]:
                inDegree[j[0]] += 1
            
        for i in range(count):
            if inDegree[i] != outDegree[i]:
                return False
        return True

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
    print("Path between 0 & 6:", gph.dfs(0, 6))
    print("Path between 0 & 6:", gph.bfs(0, 6))
    print("Path between 0 & 6:", gph.dfs_stack(0, 6))

"""
Path between 0 & 6: True
Path between 0 & 6: True
Path between 0 & 6: True
"""

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
    gph.topological_sort()

# topological_sort:: 1 4 6 3 5 7 8 0 2 

# Testing code
def test4():
    gph = Graph(5)
    gph.add_directed_edge(0, 1, 1)
    gph.add_directed_edge(0, 2, 1)
    gph.add_directed_edge(2, 3, 1)
    gph.add_directed_edge(1, 3, 1)
    gph.add_directed_edge(3, 4, 1)
    gph.add_directed_edge(1, 4, 1)
    print("path_exist::", gph.path_exist(0, 4))
    print("Path Count::", gph.count_all_path(0, 4))
    gph.print_all_path(0, 4)

"""
path_exist :: True
Path Count :: 3
[0, 1, 3, 4]
[0, 1, 4]
[0, 2, 3, 4]
"""

# Testing code
def test5():
    gph = Graph(7)
    gph.add_directed_edge(0, 1)
    gph.add_directed_edge(0, 2)
    gph.add_directed_edge(1, 3)
    gph.add_directed_edge(4, 1)
    gph.add_directed_edge(6, 4)
    gph.add_directed_edge(5, 6)
    gph.add_directed_edge(5, 2)
    gph.add_directed_edge(6, 0)
    gph.root_vertex()

# Root vertex is :: 5

# Testing code
def test6():
    gph = Graph(4)
    gph.add_directed_edge(0, 1)
    gph.add_directed_edge(0, 2)
    gph.add_directed_edge(1, 2)
    gph.add_directed_edge(2, 0)
    gph.add_directed_edge(2, 3)
    gph.add_directed_edge(3, 3)
    gph.transitive_closure()

"""
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
[0, 0, 0, 1]
"""

# Testing code
def test7():
    gph = Graph(7)
    gph.add_undirected_edge(0, 1)
    gph.add_undirected_edge(0, 2)
    gph.add_undirected_edge(0, 4)
    gph.add_undirected_edge(1, 2)
    gph.add_undirected_edge(2, 5)
    gph.add_undirected_edge(3, 4)
    gph.add_undirected_edge(4, 5)
    gph.add_undirected_edge(4, 6)
    print(gph.bfs_distance(1, 6))
    gph.bfs_level_node(1)

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

# Testing code
def test8():
    gph = Graph(6)
    gph.add_undirected_edge(0, 1)
    gph.add_undirected_edge(1, 2)
    gph.add_undirected_edge(3, 4)
    gph.add_undirected_edge(4, 2)
    gph.add_undirected_edge(2, 5)
    print("Is cycle present:", gph.is_cycle_present_undirected())
    print("Is cycle present:", gph.is_cycle_present_undirected2())
    print("Is cycle present:", gph.is_cycle_present_undirected3())

    gph.add_undirected_edge(3, 5)
    print("Is cycle present:", gph.is_cycle_present_undirected())
    print("Is cycle present:", gph.is_cycle_present_undirected2())
    print("Is cycle present:", gph.is_cycle_present_undirected3())

    print("is_connected_undirected :", gph.is_connected_undirected())

"""
Is cycle present: False
Is cycle present: False
Is cycle present: False
Is cycle present: True
Is cycle present: True
Is cycle present: True

is_connected_undirected : True
"""

# Testing code
def test9():
    gph = Graph(5)
    gph.add_directed_edge(0, 1)
    gph.add_directed_edge(0, 2)
    gph.add_directed_edge(1, 3)
    gph.add_directed_edge(2, 3)
    gph.add_directed_edge(3, 4)
    print("Cycle present:", gph.is_cycle_present())
    print("Cycle present:", gph.is_cycle_present_color())
    gph.add_directed_edge(4, 1)
    print("Cycle present:", gph.is_cycle_present())
    print("Cycle present:", gph.is_cycle_present_color())

"""
Cycle present: False
Cycle present: False
Cycle present: True
Cycle present: True
"""

# Testing code
def test10():
    gph = Graph(4)
    gph.add_directed_edge(0, 1)
    gph.add_directed_edge(0, 2)
    gph.add_directed_edge(1, 2)
    gph.add_directed_edge(2, 3)
    gph2 = gph.transpose_graph()
    gph2.print()

"""
Vertex 0 is connected to: 
Vertex 1 is connected to: 0(cost:1) 
Vertex 2 is connected to: 0(cost:1) 1(cost:1) 
Vertex 3 is connected to: 2(cost:1)   
"""

# Testing code
def test11():
    # Create a graph given in the above diagram
    gph = Graph(5)
    gph.add_directed_edge(0, 1)
    gph.add_directed_edge(1, 2)
    gph.add_directed_edge(2, 3)
    gph.add_directed_edge(3, 0)
    gph.add_directed_edge(2, 4)
    gph.add_directed_edge(4, 2)
    print("is_strongly_connected :", gph.is_strongly_connected())
    
    g2 = Graph(4)
    g2.add_directed_edge(0, 1)
    g2.add_directed_edge(1, 2)
    g2.add_directed_edge(2, 3)
    print("is_strongly_connected :", g2.is_strongly_connected())

"""
is_strongly_connected : True
is_strongly_connected : False
"""

# Testing code
def test12():
    gph = Graph(7)
    gph.add_directed_edge(0, 1)
    gph.add_directed_edge(1, 2)
    gph.add_directed_edge(2, 0)
    gph.add_directed_edge(2, 3)
    gph.add_directed_edge(3, 4)
    gph.add_directed_edge(4, 5)
    gph.add_directed_edge(5, 3)
    gph.add_directed_edge(5, 6)
    gph.strongly_connected_component()

"""
[1, 2, 0]
[4, 5, 3]
[6]
"""

# Testing code
def test13():
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
    gph.prims_mst()
    gph.kruskalMST()
    gph.dijkstra(0)

""" prims_mst
Edges are : (0->1 @ 4) (1->2 @ 8) (2->3 @ 7) (3->4 @ 9) (2->5 @ 4) (5->6 @ 2) (6->7 @ 1) (2->8 @ 2) 
Total MST cost: 37
"""
""" kruskalMST
Edges are : (6->7 @ 1) (2->8 @ 2) (5->6 @ 2) (0->1 @ 4) (2->5 @ 4) (2->3 @ 7) (0->7 @ 8) (3->4 @ 9) 
Total MST cost: 37
"""
"""dijkstra
Shortest Paths : (0->1 @ 4) (0->1->2 @ 12) (0->1->2->3 @ 19) 
                (0->7->6->5->4 @ 21) (0->7->6->5 @ 11) 
                (0->7->6 @ 9) (0->7 @ 8) (0->1->2->8 @ 14) 
"""

# Testing code
def test14():
    gph = Graph(9)
    gph.add_directed_edge(0, 1)
    gph.add_directed_edge(0, 7)
    gph.add_directed_edge(1, 2)
    gph.add_directed_edge(1, 7)
    gph.add_directed_edge(2, 3)
    gph.add_directed_edge(2, 8)
    gph.add_directed_edge(2, 5)
    gph.add_directed_edge(3, 4)
    gph.add_directed_edge(3, 5)
    gph.add_directed_edge(4, 5)
    gph.add_directed_edge(5, 6)
    gph.add_directed_edge(6, 7)
    gph.add_directed_edge(6, 8)
    gph.add_directed_edge(7, 8)
    gph.shortest_path(0)

"""
Shortest Paths : (0->1 @ 1) (0->1->2 @ 2) (0->1->2->3 @ 3) 
                (0->1->2->3->4 @ 4) (0->1->2->5 @ 3) 
                (0->1->2->5->6 @ 4) (0->7 @ 1) (0->7->8 @ 2) 
"""

# Testing code
def test15():
    gph = Graph(5)
    gph.add_directed_edge(0, 1, 3)
    gph.add_directed_edge(0, 4, 2)
    gph.add_directed_edge(1, 2, 1)
    gph.add_directed_edge(2, 3, 1)
    gph.add_directed_edge(4, 1, -2)
    gph.add_directed_edge(4, 3, 1)
    gph.bellman_ford_shortest_path(0)

"""
Shortest Paths : (0->4->1 @ 0) (0->4->1->2 @ 1) 
                (0->4->1->2->3 @ 2) (0->4 @ 2) 
"""

# Testing code
def test16():
    parentArray = [-1, 0, 1, 2, 3]
    print("Height :", height_tree_parent_arr(parentArray))
    print("Height :", height_tree_parent_arr2(parentArray))
    parentArray = [-1, 0, 0, 0, 3, 1, 1, 2]
    print("Height :", height_tree_parent_arr(parentArray))
    print("Height :", height_tree_parent_arr2(parentArray))

"""
Height : 4
Height : 4
Height : 2
Height : 2
"""

# Testing code
def test17():
    gph = Graph(5)
    gph.add_undirected_edge(1, 0)
    gph.add_undirected_edge(0, 2)
    gph.add_undirected_edge(2, 1)
    gph.add_undirected_edge(0, 3)
    gph.add_undirected_edge(3, 4)
    gph.is_eulerian()
    gph.add_undirected_edge(4, 0)
    gph.is_eulerian()

"""
graph is Semi-Eulerian
graph is Eulerian
"""

# Testing code
def test18():
    gph = Graph(5)
    gph.add_directed_edge(0, 1)
    gph.add_directed_edge(1, 2)
    gph.add_directed_edge(2, 0)
    gph.add_directed_edge(0, 4)
    gph.add_directed_edge(4, 3)
    gph.add_directed_edge(3, 0)
    print(gph.is_eulerian_cycle())

# True

def test19() :
    gph = Graph(4)
    gph.add_directed_edge(0, 0, 0)
    gph.add_directed_edge(1, 1, 0)
    gph.add_directed_edge(2, 2, 0)
    gph.add_directed_edge(3, 3, 0)
    gph.add_directed_edge(0, 1, 5)
    gph.add_directed_edge(0, 3, 10)
    gph.add_directed_edge(1, 2, 3)
    gph.add_directed_edge(2, 3, 1)
    gph.floyd_warshall()

"""
Shortest Paths : (0->1 @ 5 ) (0->1->2 @ 8 ) (0->1->2->3 @ 9 ) 
                 (1->2 @ 3 ) (1->2->3 @ 4 ) (2->3 @ 1 ) 
"""


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
