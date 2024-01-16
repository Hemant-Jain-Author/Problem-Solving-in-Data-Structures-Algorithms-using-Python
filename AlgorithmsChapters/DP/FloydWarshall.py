import math
import sys

INF = sys.maxsize

def floyd_warshall(graph,  V) :
    dist = [[0] * V for _ in range(V)]
    for i in range(0, V) :
        for j in range(0, V) :
            dist[i][j] = graph[i][j]    
    
    #  Pick intermediate vertices.
    for k in range(0, V) :
        #  Pick source vertices one by one.
        for i in range(0, V) :
            #  Pick destination vertices.
            for j in range(0, V) :
                #  If we have shorter path from i to j via k.
                #  then update dist[i][j]
                if (dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]) :
                    dist[i][j] = dist[i][k] + dist[k][j]

    print_solution(dist, V) #  Print the shortest distance matrix

def print_solution(dist,  V) :
    for i in range(0, V) :
        for j in range(0, V) :
            if (dist[i][j] == INF) : 
                print("INF", end =" ")
            else :
                print(dist[i][j], end =" ")
        print()

#  Testing code
graph = [
    [0, 2, 4, INF, INF, INF, INF], 
    [2, 0, 4, 1, INF, INF, INF], 
    [4, 4, 0, 2, 8, 4, INF], 
    [INF, 1, 2, 0, 3, INF, 6], 
    [INF, INF, 6, 4, 0, 3, 1], 
    [INF, INF, 4, INF, 4, 0, 2], 
    [INF, INF, INF, 4, 2, 3, 0]]

floyd_warshall(graph, 7)

"""
0 2 4 3 6 8 7 
2 0 3 1 4 7 5 
4 3 0 2 5 4 6 
3 1 2 0 3 6 4 
7 5 6 4 0 3 1 
8 7 4 6 4 0 2 
7 5 6 4 2 3 0 
"""
