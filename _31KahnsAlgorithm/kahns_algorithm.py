"""
Topological sorting is an algorithm used to order tasks or nodes in a directed acyclic graph,
such that for every directed edge from node U to node V, U comes before V in the ordering.
Kahn;s algorithm Steps:
1.  Calculate In Degree for each Vertex.
2.  Initialise the queue
    -   Add all vertices with no incoming edges(in degree == 0) to a queue
3.   Process the queue.
4.  Cycle detection
    -   If the topological order list contains all vertices, 
        no cycles detected, topological sort is successful.
"""
class Graph:
    def __init__(self, V):
        self.vertices = [None] * V
        for index in range(V):
            self.vertices[index] = Vertex(index)

    #31
    def kahn_algo(self):
        """
        Complexity:
            Time Complexity (Best, Worst, Average): O(V + E)
            -   Each vertex is visited once, 
                and each edge is considered once during the iteration(while loop).
            -   V: Vertices
            -   E: Edge

            Space Complexity:  O(V)
            
            Auxiliary Space:  O(V)
            -   The space complexity is determined by the space required for the queue, array list.
        """
        sorted_list = []
        process = []
        in_degree = [0] *len(self.vertices)

        for vertex in self.vertices:
            for edge in vertex.edges:
                v = edge.v
                in_degree[v.id] += 1

        for vertex in self.vertices:
            if in_degree[vertex.id] == 0:
                process.append(vertex)
            
        while len(process) > 0:
            vertex_u = process.pop()
            sorted_list.append(vertex_u)
            for edge in vertex_u.edges:
                v = edge.v
                in_degree[v.id] -= 1
                if in_degree[v.id] == 0:
                    process.append(v)
        
        # Check if the topological sort was successful
        if len(sorted_list) == len(self.vertices):
            return sorted_list
        else:
            return "Cycle detected, topological sort not possible."

class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = [] #To store the other vertices that connect from this vertex
    def add_edges(self, vertex):
        self.edges.append(vertex)

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        
if __name__ == "__main__":
    pass