def ispossible(node,graph,color,col):
    for u,v in graph:
        if u==node and color[v]==col:
            return False
        if v==node and color[u]==col:
            return False

    return True

def rec(node,graph,m,N,color):
    if node==N:
        return True

    for i in range(m):
        if ispossible(node,graph,color,i):
            color[node]=i
            if rec(node+1,graph,m,N,color):
                return True
            color[node]=0

    return False

def graphColoring(graph,m,N):
    color=[0]*N

    if rec(0,graph,m,N,color):
        return True
    return False

def main():
    N = 4  # Number of nodes
    m = 3  # Maximum number of colors

    Edges = {(0, 1),(1, 2),(2, 3),(3, 0),(0, 2)}

    # Output if the graph can be colored with at most m colors
    print(graphColoring(Edges, m, N))

main()