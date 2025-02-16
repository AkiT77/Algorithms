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

"""
class Graph:
    def __init__(self, V):
        self.vertices = [None] * V
        for index in range(V):
            self.vertices[index] = Vertex(index)

    def __str__(self):
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "," + str(vertex)
        return return_string

    #25
    def traverse(self):
        """
        Driver function that calls DFS until everything has been visited
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
                if edge.visited and edge != parent:
                    return True
                elif not edge.visited:
                    discovered.append((edge, u)) 
        return False

    # #27 Recursive way
    # def dfs_27(self, source, parent):
    #     source.visited = True
    #     for vertex in source.edges:
    #         if not vertex.visited and self.dfs_27(vertex, source):
    #             return True
    #         elif vertex != parent:
    #             return True
    #     return False

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

    #29
    def bfs_29(self, source):
        pass
    
class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = [] #To store the other vertices that connect from this vertex
        self.discovered = False
        self.visited = False
        self.component = None

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
    vertices = [0, 1, 2, 3, 4, 5]
    graph = Graph(V = len(vertices))


    