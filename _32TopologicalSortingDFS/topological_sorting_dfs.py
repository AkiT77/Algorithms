"""
Topological Sorting Using DFS Steps:
1.  DFS Traversal:
-   Perform a Depth-First Search (DFS) starting from a vertex v.
-   Visit all vertices dependent on v.
2.  Topological Order:
-   Add each vertex to an array after completing DFS for all its descendants.
"""
class Graph:
    def __init__(self, V):
        self.vertices = [None] * V
        for index in range(V):
            self.vertices[index] = Vertex(index)

    # Algorithm 32 Topological sorting using DFS
    def topological_sort_dfs(self):
        """    
        Parameters:
            source (int): The source vertex
        
        Returns:
            array[int]: The visited list by order.

        Complexity:
            Time Complexity (Best, Worst, Average): O(V + E)
                -   The algorithm visits every vertex and edge exactly once.
                -   V: Vertices
                -   E: Edge
                -   Note: If using Adjacency Matrix instead of Adjacency List, the time complexity will be O(V^2).

            Space Complexity:  O(V)
                
            Auxiliary Space:  O(V)
                -    appending V items to an array
        """
        sorted_order = []
        for vertex in self.vertices:
            vertex.visited = False

        for vertex in self.vertices:
            if not vertex.visited:
                self.dfs_32(vertex, sorted_order)

        return sorted_order

    def dfs_32(self, source, sorted_order):
        """    
        Computing topological orderings.

        Parameters:
            source (int): The source vertex
            sorted_order(array[int]): An array to store the visited list by topological ordering
        
        Returns:
            array[int]: The visited list by order.

        Complexity:
            Time Complexity (Best, Worst, Average): O(V + E)
                -   The algorithm visits every vertex and edge exactly once.
                -   V: Vertices
                -   E: Edge
                -   Note: If using Adjacency Matrix instead of Adjacency List, the time complexity will be O(V^2).

            Space Complexity:  O(V)
                
            Auxiliary Space:  O(V)
                -    appending V items to an array
        """
        discovered = []  
        discovered.append(source)

        while discovered:
            u = discovered.pop()
            if not u.visited:
                u.visited = True 

                for edge in u.edges:
                    v = edge.v
                    if not v.visited:
                        discovered.append(v)  

                # Once all neighbors are visited, add the node to the sorted order
                sorted_order.append(u.id)  

class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = [] #To store the other vertices that connect from this vertex
        self.discovered = False
        self.visited = False

    def add_edges(self, vertex):
        self.edges.append(vertex)

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        
if __name__ == "__main__":
    pass