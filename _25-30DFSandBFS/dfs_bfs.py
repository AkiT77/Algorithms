class Graph:
    def __init__(self, V):
        self.vertices = [None] * len(V)
        for index in range(V):
            self.vertices[index] = Vertex(V[index])

    def __str__(self):
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "," + str(vertex)
        return return_string
    
    def bfs(self, source):
        """
        Function for BFS, starting from the source
        """
        return_bfs = []
        discovered = []
        discovered.append(source)
        while len(discovered) > 0:
            u = discovered.pop(0)
            u.visited = True
            return_bfs.append(u)
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True
        return return_bfs
    
    def dfs(self, source):
        """
        Function for DFS, starting from the source
        """
        return_dfs = []
        discovered = []
        discovered.push(source) #
        while len(discovered) > 0:
            u = discovered.pop(0)
            u.visited = True
            return_dfs.append(u)
            for edge in u.edges:
                v = edge.v
                if v.discovered == False:
                    discovered.push(v)
                    v.discovered = True
        return return_dfs   

class Vertex:
    def __init__(self):
        self.id = id
        self.edges = [] #To store the other vertices that connect from this vertex
        self.discovered = False
        self.visited = False

    def __str__(self):
        return_string = str(self.id)
        return return_string
    
    def added_to_queue(self):
        self.discovered = True

    def visit_node(self):
        self.visited = True

    def add_edges(self, vertex):
        self.edges.append(vertex)

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = V
        self.w = w
        
if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]


    