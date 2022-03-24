import math
import sys

def tsp(graph,  n) :
    visited = [False] * n
    path = [0] * (n+1)
    visited[0] = True
    ans = [0]*2
    ans[0] = sys.maxsize # Path cost.
    tsp_util(graph, n, path, 1, 0, visited, ans)
    return  ans

def tsp_util(graph,  n,  path,  path_size,  path_cost,  visited,  ans) :
    if ans[0] < path_cost : # Ignore useless paths.
        return;
    
    curr = path[path_size - 1]
    if path_size == n :
        if graph[curr][0] > 0  and ans[0] > path_cost + graph[curr][0] :
            path[path_size] = 0
            ans[0] = path_cost + graph[curr][0]
            ans[1] = list_to_string(path)
        return;

    for i in range(0, n):
        if (visited[i] == False and graph[curr][i] > 0) :
            visited[i] = True
            path[path_size] = i
            tsp_util(graph, n, path, path_size + 1, path_cost + graph[curr][i], visited, ans)
            visited[i] = False

def list_to_string(lst): 
    str1 = "" 
    for ele in lst: 
        str1 += str(ele)
        str1 += " "  
    return str1 

# Testing Code
n = 4
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
ans = tsp(graph, n)
print(f"TSP path: {ans[1]}, cost: {ans[0]}")

"""
TSP path: 0 1 3 2 0 , cost: 80
"""