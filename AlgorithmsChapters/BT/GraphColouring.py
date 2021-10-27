#  Check if the whole graph is coloured properly.
def is_safe2(graph,  colour,  V) :
    for i in range(V) :
        for j in range(i+1, V):
            if (graph[i][j] and colour[j] == colour[i]) :
                return  False    
    return  True

def graph_colouring_util2(graph,  V,  m,  colour,  i) :
    if (i == V) :
        if (is_safe2(graph, colour, V)) :
            print("Assigned colours are::", colour)
            return True
        return  False

    #  Assign each colour from 1 to m
    for j in range(1, m+1):
        colour[i] = j
        if (graph_colouring_util2(graph, V, m, colour, i + 1)) :
            return  True
    return  False

def graph_colouring2(graph,  V,  m) :
    colour = [0] * V
    if (graph_colouring_util2(graph, V, m, colour, 0)) :
        return  True
    return  False

#  Is it safe to colour vth vertice with c colour.
def is_safe(graph,  V,  colour,  v,  c) :
    i = 0
    for i in range(0, V) :
        if (graph[v][i] == True and c == colour[i]) :
                return  False    
    return  True

def graph_colouring_util(graph,  V,  m,  colour,  i) :
    if (i == V) :
        print("Assigned colours are::", colour)
        return  True
    for j in range(1, m+1):
        if (is_safe(graph, V, colour, i, j)) :
            colour[i] = j
            if (graph_colouring_util(graph, V, m, colour, i + 1)) :
                return  True
    return  False

def graph_colouring(graph,  V,  m) :
    colour = [0] * V
    if (graph_colouring_util(graph, V, m, colour, 0)) :
        return  True
    return  False

# Testing Code.
graph = [[False, True, False, False, True],
[True, False, True, False, True], 
[False, True, False, True, True], 
[False, False, True, False, True],
[True, True, True, True, False]]

V = 5  #  Number of vertices
m = 4  #  Number of colours

if (not graph_colouring(graph, V, m)) : 
    print("Solution does not exist")
if (not graph_colouring2(graph, V, m)) : 
    print("Solution does not exist")

"""
Assigned colours are:: [1, 2, 1, 2, 3]
Assigned colours are:: [1, 2, 1, 2, 3]
"""