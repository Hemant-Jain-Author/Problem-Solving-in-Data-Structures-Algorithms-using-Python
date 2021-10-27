import math
import sys

#  Function to find the minimum weight Hamiltonian Cycle
def tsp_util(graph,  n,  path,  path_size,  path_cost,  visited,  ans) :
    curr = path[n - 1]
    if (path_size == n and graph[curr][0] > 0) :
        ans = min(ans,path_cost + graph[curr][0])
        return  ans

    for i in range(0, n):
        if (visited[i] == False and graph[curr][i] > 0) :
            visited[i] = True
            path[path_size] = i
            ans = tsp_util(graph, n, path, path_size + 1, path_cost + graph[curr][i], visited, ans)
            visited[i] = False
    return  ans

def tsp(graph,  n) :
    visited = [False] * n
    path = [0] * n
    visited[0] = True
    ans = tsp_util(graph, n, path, 1, 0, visited, sys.maxsize)
    return  ans

# Testing Code
n = 4
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print("TSP path cost:", tsp(graph, n))

"""
TSP path cost: 65
"""