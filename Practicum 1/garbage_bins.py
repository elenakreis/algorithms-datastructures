import numpy as np

def gather_input():
    first_line = input()
    n, m, k = first_line.split()
    n, m, k = int(n), int(m), int(k)
    edges = np.zeros((m,m))
    for i in range(n):
        line = input()
        a, b = line.split()
        a, b = int(a)-1, int(b)-1
        edges[a][b] = 1
        edges[b][a] = 1
    return edges, n, m, k

# Create the adjacency matrix from the input
def create_graph(input):
    print(input)

# Compute degree of node
def degree_of(node):
    return sum(edges[node])

# Find index of node with smallest degree
def smallest_degree(max_set):
    smallest = max_set[0] #??
    smallest_degree = 5 # maximum degree
    for node in range(nr_nodes):
        # Only consider nodes still in the set, also no nodes without neighbours
        if node in max_set and degree_of(node)>0 and degree_of(node)<smallest_degree:
            smallest=node
            smallest_degree = degree_of(smallest)
    return smallest

# Check if a set is independent
def independent(set):
    independent = True
    for a in set:
        for b in set:
            if edges[a][b] != 0:
                independent = False
    return independent

# Find the neighbours of a node
def find_neighbours(node):
    neighbours = []
    for index, edge in enumerate(edges[node]):
        if edge != 0:
            neighbours.append(index)
    return neighbours

# Remove entries in the adjacency matrix for all nodes in 'nodes'
def remove_nodes(nodes):
    for node in range(nr_nodes):
        if node in nodes:
            edges[node] = np.zeros(nr_nodes) # Remove entire row
        else:
            edges[node][nodes] = 0 # Remove connections with nodes

# Approximate the maximum independent set
def approximate():
    max_set = np.arange(nr_nodes)
    while not independent(max_set):
        smallest = smallest_degree(max_set)
        neighbours = find_neighbours(smallest)
        print("smallest node: ", smallest, neighbours)
        max_set = [element for element in max_set if element not in neighbours]
        print("New max set: ",max_set)
        remove_nodes(neighbours)
        print(edges)
    return max_set


edges, n, m, k = gather_input() #np.array([[0,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,0]])
nr_nodes = len(edges)
print(edges)
max_set = approximate()
print("Maximum independent set found: ", max_set)
print("Size of set: ", len(max_set))
if(len(max_set)>=k):
    print("Possible")
else:
    print("Impossible")
