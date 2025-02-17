"""
Depth-First Search (DFS)
1.  Data Structure: 
    Stack (Last In, First Out).
    Here, we use pop(), to make it LIFO
2.  Approach: 
    DFS explores as far as possible along each branch before backtracking. It uses a stack to keep track of the nodes to visit next. In a recursive implementation, 
    the function call stack itself serves this purpose.
3.  Traversal Order: 
    DFS dives deep into each branch before visiting siblings.
4.  DFS can be used to explore all possible paths in a maze or puzzle, 
    ensuring all solutions are found.

Breadth-First Search (BFS)
1.  Data Structure: 
    Queue (First In, First Out)
    Here, we use pop(0), to make it FIFO
2.  Approach: 
    BFS explores all the neighbors at the present depth level before moving on to nodes at the next depth level. 
    It uses a queue to keep track of the nodes to visit in a first-in, first-out (FIFO) manner.
3.  Traversal Order: 
    BFS visits all nodes level by level, starting from the root.
4.  BFS can be used in social networks to recommend friends by finding nodes (users) within a certain distance (degree of separation).

The complexity regarding bfs and dfs algorithm:
    Complexity:
        Time Complexity (Best, Worst, Average): O(V + E)
        -   The algorithm visits every vertex and edge exactly once.
        -   V: Vertices
        -   E: Edge
        -   Note: If using Adjacency Matrix instead of Adjacency List, the time complexity will be O(V^2).

        Space Complexity:  O(V)
        
        Auxiliary Space:  O(V)
        -   The space complexity is determined by the space required for the DFS.

"""
class Graph:
    def __init__(self, V):
        self.vertices = [None] * V
        for index in range(V):
            self.vertices[index] = Vertex(index)

    #25
    """
    Even though DFS will visit all vertices and edges in a single connected component, 
    it may not cover the entire graph if there are multiple disconnected components. 
    The second loop ensures that every vertex in the graph is visited by restarting the DFS from any vertex that hasn't been visited, 
    thus covering all components of the graph.
    """
    def traverse(self):
        """
        Driver function that calls DFS until everything has been visited

        Parameters:
            -
            
        Returns:
            -
        """
        for vertex in self.vertices:
            vertex.visited = False
        
        for vertex in self.vertices:
            if not vertex.visited:
                self.dfs_25(vertex)

    #25
    def dfs_25(self, source):
        """
        Generic depth first search
        Function for DFS, starting from the source

        Parameters:
            source (int): The source vertex
        
        Returns:
            array[int]: The visited list by order.
        """
        return_dfs = []
        discovered = [] #Implement this as a Stack.
        discovered.append(source) 
        while len(discovered) > 0:
            u = discovered.pop()
            if not u.visited: 
                u.visited = True
                return_dfs.append(u)
                for edge in u.edges:
                    v = edge.v
                    if v.discovered == False:
                        discovered.push(v)
                        v.discovered = True
        return return_dfs  

    #26
    def connected_component(self):
        """
        Driver function that finds each connected component
        """
        for vertex in self.vertices:
            vertex.component = None
        number_components = 0
        for vertex in self.vertices:
            if vertex.component == None:
                number_components += 1
                self.dfs_26(vertex, number_components)
        components = []
        for vertex in self.vertices:
            components.append(vertex.component)
        return number_components, components  

    #26
    def dfs_26(self, source, comp_num):
        """
        Function for DFS, starting from the source
        
        Parameters:
            source (int): The source vertex
        
        Returns:
            array[int]: The visited list by order.
        """
        return_dfs = []
        discovered = [] #Implement this as a Stack.
        discovered.append(source) 
        while len(discovered) > 0:
            u = discovered.pop()
            if not u.visited: 
                u.visited = True
                u.component = comp_num #For 26 usage
                return_dfs.append(u)
                for edge in u.edges:
                    v = edge.v
                    if v.discovered == False:
                        discovered.push(v)
                        v.discovered = True
        return return_dfs     
    
    #27
    def has_cycle(self):
        for vertex in self.vertices:
            vertex.visited = False
        for vertex in self.vertices:
            if not vertex.visited and self.dfs(vertex, None) == True:
                return True
        return False
        
    #27
    def dfs_27(self, source):
        """
        Function for DFS, starting from the source
        """
        discovered = [] #Implement this as a Stack.
        discovered.append((source, None)) 
        while len(discovered) > 0:
            (u, parent) = discovered.pop()
            u.visited = True
            for edge in u.edges:
                v = edge.v
                if v.visited and edge != parent:
                    return True
                elif not v.visited:
                    discovered.append((v, u)) 
        return False

    #27 Recursive way
    def dfs_27(self, source, parent):
        source.visited = True
        for edge in source.edges:
            v = edge.v
            if not v.visited and self.dfs_27(v, source):
                return True
            elif v != parent:
                return True
        return False

    #28
    def bfs(self, source):
        """
        Generic breadth first search
        Function for BFS, starting from the source
        """
        return_bfs = []
        discovered = [] #Implement this as a Queue.
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

    #29 Single-source shortest paths in an unweighted graph
    def bfs_29(self, source):
        """
        Computes the shortest paths from the source vertex s to every other reachable vertex in the graph.
        """
        discovered = [None] * len(self.vertices)
        discovered.append(source)
        source.distance = 0
        while len(discovered) > 0:
            u = discovered.pop(0)
            for edge in u.edges:
                v = edge.v
                if v.distance == 'int':
                    v.distance = u.distance + 1
                    v.parent = u
                    discovered.append(edge)
    
    #30 Reconstruct shortest path
    def get_path(self, source, destination):
        path = [destination]
        while source != destination:
            path.append(destination.parent)
            destination = destination.parent
        path = path.reverse()
        return path

class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = [] #To store the other vertices that connect from this vertex
        self.discovered = False
        self.visited = False
        self.component = None
        self.distance = 'inf'
        self.parent = None

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
        self.v = v
        self.w = w
        
if __name__ == "__main__":
    vertices = [0, 1, 2, 3, 4, 5]
    graph = Graph(V = len(vertices))


    