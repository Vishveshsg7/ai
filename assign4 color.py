def is_safe(graph,v,pos,c):
    for i in range(len(graph)):
        if graph[v][i]==1 and pos[i] == c:
            return False

    return True

def graph_coloring(graph,m,v,pos):
    if v == len(graph):
        return True
    
    for c in range(1,m+1):
        if is_safe(graph,v,pos,c):
            pos[v]=c
            if graph_coloring(graph,m,v+1,pos):
                return True
            pos[v]=0

    return False

def graph_solution(graph,m):
    pos = [0] * len(graph)
    if not graph_coloring(graph,m,0,pos):
        print("Solution does not exist")
    else:
        print("Solution exists:",pos)

if __name__ == '__main__':
    no_of_vertices=int(input("Enter the numbe of vertices"))

    graph=[]
    print("ENter the vlaues for graph 1 for connected and 0 for not connected")
    for _ in range(no_of_vertices):
        row = list(map(int,input().split()))
        graph.append(row)

    no_of_colors=int(input("Enter the number of colors:"))

    graph_solution(graph,no_of_colors)
