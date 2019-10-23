#import numpy as np

class Garbage:
    def __init__(self, edges, k):
        self.edges = edges
        self.nr_nodes = len(edges)
        self.k = k

    # Create the adjacency matrix from the input
    def create_graph(self,input):
        print(input)

    # Compute degree of node
    def degree_of(self,node):
        return sum(self.edges[node])

    # Find index of node with smallest degree
    def smallest_degree(self, max_set):
        smallest = max_set[0] #??
        smallest_degree = 5 # maximum degree
        for node in max_set:
            # Only consider nodes still in the set, also no nodes without neighbours
            if self.degree_of(node)>0 and self.degree_of(node)<smallest_degree:
                smallest=node
                smallest_degree = self.degree_of(smallest)
        return smallest

    # Check if a set is independent
    def independent(self,set):
        independent = True
        for a in set:
            for b in set:
                if self.edges[a][b] != 0:
                    independent = False
        return independent

    # Find the neighbours of a node
    def find_neighbours(self,node):
        neighbours = []
        for index, edge in enumerate(self.edges[node]):
            if edge != 0:
                neighbours.append(index)
        return neighbours

    # Remove entries in the adjacency matrix for all nodes in 'nodes'
    def remove_nodes(self,nodes):
        for node in range(self.nr_nodes):
            if node in nodes:
                self.edges[node] = [0 for n in range(self.nr_nodes)] # np.zeros(self.nr_nodes) # Remove entire row
            else:
                for n in nodes:
                    self.edges[node][n] = 0
                #self.edges[node][nodes] = 0 # Remove connections with nodes

    # Approximate the maximum independent set
    def approximate(self):
        max_set = [item for item in range(self.nr_nodes)] # np.arange(self.nr_nodes)
        while not self.independent(max_set):
            smallest = self.smallest_degree(max_set)
            neighbours = self.find_neighbours(smallest)
            #print("smallest node: ", smallest, neighbours)
            max_set = [element for element in max_set if element not in neighbours]
            #print("New max set: ",max_set)
            self.remove_nodes(neighbours)
            #print(self.edges)
        return max_set


def gather_input():
    first_line = input()
    n, m, k = first_line.split()
    n, m, k = int(n), int(m), int(k)
    edges = [[0 for i in range(m)] for j in range(m)] # np.zeros((m,m))
    for i in range(n):
        line = input()
        a, b = line.split()
        a, b = int(a)-1, int(b)-1
        edges[a][b] = 1
        edges[b][a] = 1
    return edges, k

edges, k = gather_input() #np.array([[0,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,0]])
g = Garbage(edges, k)
max_set = g.approximate()
#print("Maximum independent set found: ", max_set)
#print("Size of set: ", len(max_set))
if(len(max_set)>=k):
    print("possible")
else:
    print("impossible")
