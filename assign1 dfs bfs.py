no_of_nodes = int(input("Enter the number of nodes: "))

graph = {}

for i in range(no_of_nodes):
    node = input("Enter the node name: ")
    graph[node] = []
    no_of_neighbours = int(input("Enter the number of neighbors: "))
    lst = []
    for j in range(no_of_neighbours):
        neighbour = input("Enter the neighbor: ")
        lst.append(neighbour)
    graph[node] = lst

print(graph)

visited = set()

def dfs(graph, vertex, visited, goal):
    if vertex not in visited:
        visited.add(vertex)
        print(vertex)
        if vertex == goal:
            print("Goal node reached:", goal)
            return True
        for neighbor in graph[vertex]:
            if dfs(graph, neighbor, visited, goal):
                return True
    return False

visited1 = set()

def bfs(graph, vertex, visited1, goal):
    visited1.add(vertex)
    queue = []
    queue.append(vertex)

    while queue:
        v = queue.pop(0)
        print(v)
        if v == goal:
            print("Goal node reached:", goal)
            return True
        for neighbor in graph[v]:
            if neighbor not in visited1:
                visited1.add(neighbor)
                queue.append(neighbor)

v = input("Enter the starting vertex name: ")
goal_node = input("Enter the goal node name: ")

if v in graph:
    print("DFS:")
    if not dfs(graph, v, visited, goal_node):
        print("Goal node not found starting from node:", v)

    print("BFS:")
    if not bfs(graph, v, visited1, goal_node):
        print("Goal node not found starting from node:", v)
else:
    print("Starting vertex not found in the graph.")
