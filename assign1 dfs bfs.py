no_of_nodes = int(input("Enter number of nodes: "))

graph = {}

for i in range(no_of_nodes):
    node = input("Enter node name: ")
    graph[node] = []
    no_of_neighb = int(input("Enter number of neighbours: "))
    lst = []
    for j in range(no_of_neighb):
        neighbour = input("Enter neighbour: ")
        lst.append(neighbour)
    graph[node] = lst
    
print(graph)

visited = set()

def dfs(graph,vertex,visited):
    if vertex not in visited:
        visited.add(vertex)
        print(vertex)
        for neighbour in graph[vertex]:
            dfs(graph,neighbour,visited)
            
v = input("Enter vertex name: ")

if v in graph:
    dfs(graph,v,visited)



################################################

graph = {
    '1' : ['2'],
    '2' : ['1','3','4'],
    '3' : ['2','5'],
    '4' : ['2'],
    '5' : ['3']
}

visited = set()

def bfs(graph,vertex,visited):
    visited.add(vertex)
    queue = []
    queue.append(vertex)
    
    while queue:
        v = queue.pop(0)
        print(v)
        
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

bfs(graph,'4',visited)