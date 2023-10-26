class Graph():
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]for row in range(vertices)]
   
    def isSafe(self, v, color, c):
        for i in range(self.v):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True
    
    def graphColorUtil(self, m, color, v):
        if v == self.v:
            return True
        for c in range(1,m+1):
            if self.isSafe(v, color, c)==True:
                color[v]=c
                if self.graphColorUtil(m, color, v+1) == True:
                    return True
                colour[v]=0
    def graphColoring(self,m):
        color = [0]*self.v
        if self.graphColorUtil(m, color, 0)==None:
            return False
     
        print("Solution exists and the following are the assigned colors: ")
        for c in color:
            print(c, end=' ')
        return True

if __name__ == '__main__':
    vertices = int(input("Enter the number of vertices: "))
    graph = []
    print("Enter the adjacency matrix: ")
    for i in range(vertices):
        temp = list(map(int,input().split()))
        graph.append(temp)
    g = Graph(vertices)
    g.graph = graph
    m=3
   
    g.graphColoring(m)
