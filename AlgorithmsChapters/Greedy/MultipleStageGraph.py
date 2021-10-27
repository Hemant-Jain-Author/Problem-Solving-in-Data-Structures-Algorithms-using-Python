
import sys

INF = 99999
  
#  Returns shortest distance from 0 to N-1.
def graph_shortest_dist(graph,  n) :
    #  dist[i] is going to store shortest
    #  distance from node i to node n-1.
    dist = [INF] * n
    path = [0] * n
    dist[0] = 0
    path[0] = -1

    #  Calculating shortest path for the nodes
    for i in range(n) : #  Check all nodes of next 
        for j in range(i, n) :
            if (graph[i][j] == INF) : #  Reject if no edge exists
                j += 1
                continue
            value = graph[i][j] + dist[i]
            if (dist[j] > value) :
                dist[j] = value
                path[j] = i

    value = n - 1
    print("Path:", end =" ")
    while (value != -1) :
        print(str(value), end =" ")
        value = path[value]
    print()
    return  dist[n - 1]

#  Driver code
#  Graph stored in the form of an adjacency Matrix
graph = [[INF, 1, 2, 5, INF, INF, INF, INF], 
[INF, INF, INF, INF, 4, 11, INF, INF], 
[INF, INF, INF, INF, 9, 5, 16, INF], 
[INF, INF, INF, INF, INF, INF, 2, INF], 
[INF, INF, INF, INF, INF, INF, INF, 18], 
[INF, INF, INF, INF, INF, INF, INF, 13], 
[INF, INF, INF, INF, INF, INF, INF, 2], 
[INF, INF, INF, INF, INF, INF, INF, INF]]
print("Shortest Distance:", graph_shortest_dist(graph, 8))

"""
Path: 7 6 3 0 
Shortest Distance: 9
"""