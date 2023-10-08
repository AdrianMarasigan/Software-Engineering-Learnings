# Nodes (Vertices)
# Nodes in a graph represent data elements, entities, or points of interest.
# Each node can have a unique label or identifier to distinguish it from other nodes.

class Node:
    def __init__(self, label):
        self.label = label

# Edges
# Edges in a graph represent relationships or connections between nodes.
# They can be directed (with a specific direction) or undirected (bidirectional).
# Edges can also have associated weights or costs.

class Edge:
    def __init__(self, start, end, weight=None, directed=False):
        self.start = start
        self.end = end
        self.weight = weight
        self.directed = directed

# Directed and Undirected Graphs
# The nature of edges determines whether a graph is directed or undirected.
# In directed graphs, edges have a direction, indicating a one-way relationship.
# In undirected graphs, edges have no direction, representing mutual connections between nodes.

class Graph:
    def __init__(self):
        self.nodes = {}  # A dictionary to store nodes and their neighbors

    def add_node(self, node):
        if node.label not in self.nodes:
            self.nodes[node.label] = []

    def add_edge(self, edge):
        if edge.start.label in self.nodes and edge.end.label in self.nodes:
            self.nodes[edge.start.label].append(edge)

    def __str__(self):
        graph_str = ""
        for node, edges in self.nodes.items():
            graph_str += f"{node}: "
            for edge in edges:
                if edge.directed:
                    graph_str += f"({edge.end.label}, {edge.weight}) "
                else:
                    graph_str += f"{edge.end.label} "
            graph_str += "\n"
        return graph_str

# Example usage:
# Create nodes
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")

# Create edges (unweighted and undirected)
edge1 = Edge(node_a,
