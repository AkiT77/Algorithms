"""
Incremental connectivity problem:
    1.  The situation where edges are only added to a graph, not deleted.
    2.  Functions:
            1.  CONNECTED(u, v): Check whether the vertices u and v are connected.
            2.  LINK(u, v): Add an edge between the vertices u and v.

Union-Find and Disjoint-Set Data Structure:
    1.  Collection of n elements: 
            We start with n elements, each in its own separate set.
    2.  Single set per element: 
            Initially, every element belongs to its own individual set.
    3.  Merge sets (Union): 
            The union operation merges two sets, so both elements end up in the same set.
    4.  Representative: 
            Each set has a representative (an arbitrary element from the set) used to identify the set.
    5.  Find operation: 
            The find operation checks which set an element belongs to by identifying its representative. If two elements share the same representative, 
            they are in the same set.
    6.  Functions:
            1.  Find: This operation tells us which set an element belongs to by finding its representative.
            2.  Union: This operation merges two sets into one by linking their representatives.

Disjoint set forests:
    1.  Each set is a tree, with each node representing an element. 
        The root of the tree is the representative of the set.
    2.  Parent Pointers: 
            Only store a pointer to the parent of each node. 
            For root nodes, the parent points to itself.
    3.  Functions:
            1.  FIND(u): To find the representative of u, just follow the parent pointers until you hit the root.
            2.  UNION(u, v): To merge sets containing u and v, check if they're already in the same set. If not, link one root to the other, combining the two trees.

"""
def connected_function(u, v):
    """
    Check whether the vertices u and v are connected.
    """
    return #to checking whether they have the same representative


class Union:
    def __init__(self, n):
        parent = []
        rank = [0] * len(n)

    """
    Algorithms 34 Union-find using disjoint-set forests (without optimisations)
    """
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.find(self.parent[x])

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    """
    Algorithm 35 The FIND operation using path compression.
    Path compression speeds up FIND by making every node on the path point directly to the root. 
    This flattens the tree, reducing its height and speeding up future queries. It minimizes long chains, 
    making FIND operations faster over time.
    """
    def find(self, x):
        """
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    """
    In union by rank, each tree has a rank that bounds its height. 
    When merging two trees, the tree with the smaller rank becomes a child of the one with the larger rank. 
    This keeps the trees more balanced and reduces their height. 
    """
    def union_36(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
