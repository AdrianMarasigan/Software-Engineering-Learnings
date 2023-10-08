# Node in a Tree
# Nodes in a tree represent data elements, entities, or points of interest.
# Each node can have a unique label or identifier to distinguish it from other nodes.

class TreeNode:
    def __init__(self, label, data=None):
        self.label = label  # Unique label for the node
        self.data = data    # Data associated with the node
        self.children = []  # List of child nodes

# Creating a Tree
# A tree can be constructed by creating nodes and connecting them.


# Create nodes
root = TreeNode("A", data="Root Data")
node_b = TreeNode("B", data="Node B Data")
node_c = TreeNode("C", data="Node C Data")

# Connect nodes to form the tree structure
root.children.append(node_b)
root.children.append(node_c)

# Example usage:
# Accessing data and children of nodes
print("Root Label:", root.label)
print("Root Data:", root.data)

for child in root.children:
    print(f"Child Label: {child.label}, Child Data: {child.data}")

# Output:
# Root Label: A
# Root Data: Root Data
# Child Label: B, Child Data: Node B Data
# Child Label: C, Child Data: Node C Data
