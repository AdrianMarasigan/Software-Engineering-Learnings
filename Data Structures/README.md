# Data Structures
This section provides an in-depth understanding of fundamental data structures commonly used in computer science and software engineering. Each data structure plays a crucial role in organizing and manipulating data efficiently, making it essential for both beginners and experienced developers.
# Table of Contents
- [Arrays](https://github.com/c0olade/Software-Engineering-Journey/tree/main/Data%20Structures/Arrays)
- [Linked Lists](https://github.com/c0olade/Software-Engineering-Journey/tree/main/Data%20Structures/Linked%20Lists)
- [Stacks](https://github.com/c0olade/Software-Engineering-Journey/tree/main/Data%20Structures/Stacks)
- [Queues](https://github.com/c0olade/Software-Engineering-Journey/tree/main/Data%20Structures/Queues)
- [Hash Sets](https://github.com/c0olade/Software-Engineering-Journey/tree/main/Data%20Structures/Hash%20Sets)
- [Hash Maps (Hash Tables)](https://github.com/c0olade/Software-Engineering-Journey/tree/main/Data%20Structures/Hash%20Maps%20(Hash%20Tables))
- [Trees](https://github.com/c0olade/Software-Engineering-Journey/tree/main/Data%20Structures/Trees)
- [Graphs](https://github.com/c0olade/Software-Engineering-Journey/tree/main/Data%20Structures/Graphs)


# Arrays
An array is a fundamental data structure that stores a collection of elements, such as numbers, characters, or other data types, in a contiguous block of memory. Arrays are widely used because they provide efficient access to individual elements based on their index or position within the array.

I'll be using Python to compare arrays to lists as I am learning in Python. This for reference only and will not be a tutorial on how to use lists in Python.

## Key Characteristics
1. Indexing: Each element in an array is identified by an index or position. Indices are "zero-indexed" which means that the first element in the data structure is located at index 0. In a zero-indexed structure, the indexing starts from zero and proceeds to higher integer values for subsequent elements.starting from 0 for the first element. You can access elements in an array by specifying their index.

```Python
my_array = [1,2,3,4,5]
# Accessing elements by index
first_element = my_array[0]  # 1
third_element = my_array[2]  # 3
```

2. Homogeneous: Arrays are typically homogeneous, which means they store elements of the same data type. For example, you can have an array of integers, an array of floating-point numbers, or an array of characters.

```Python
# Example of an array of integers
int_array = [1, 2, 3, 4, 5]

# Example of an array of floating-point numbers
float_array = [0.1, 0.2, 0.3, 0.4, 0.5]

# Example of an array of characters
char_array = ['a', 'b', 'c', 'd', 'e']
```

In Python, lists are not homogeneous, which means they can store elements of different data types within the same list. This is one of the characteristics that distinguishes Python lists from traditional arrays in some other programming languages, which are typically homogeneous and store elements of the same data type.

```Python
my_list = [1, 'Hello', 3.14, True]

# Elements in the list have different data types:
# - Integer (1)
# - String ('Hello')
# - Floating-point number (3.14)
# - Boolean (True)
```

3. Fixed Size: In many programming languages, arrays have a fixed size, meaning you need to specify the number of elements the array can hold when you create it. Once created, the size of the array generally cannot be changed.

In Python, lists are not a fixed size, unlike arrays in some other programming languages. Python lists are dynamic and resizable, meaning you can add or remove elements from a list without specifying an initial fixed size, and the size of the list can change as needed during the program's execution.

```Python
# Creating an empty list
my_list = []

# Adding elements to the list (list grows dynamically)
my_list.append(10)      # [10]
my_list.append(20)      # [10, 20]
my_list.append(30)      # [10, 20, 30]

# Removing elements from the list (list size can shrink)
my_list.pop()           # Removes the last element, leaving [10, 20]
```

4. Contiguous Memory: The elements of an array are stored in contiguous (adjacent) memory locations. This property allows for efficient memory access because elements are stored close together. It is also inherent in how Python implements lists (which are similar to arrays). The elements of a list are stored in contiguous memory locations automatically by the Python interpreter.

5. Random Access: Arrays offer constant-time (O(1)) access to individual elements. You can directly access any element by its index, making it efficient for tasks like searching and retrieving data.

```Python
my_array = [10, 20, 30, 40, 50]
third_element = my_array[2]  # Accessing the third element (30) directly by index
```

6. Iterating: You can easily iterate through the elements of an array using loops, such as for loops, to perform operations on each element.

```Python
my_array = [10, 20, 30, 40, 50]
for element in my_array:
    print(element)  # Iterating through the elements of the array
```

7. Common Operations: Arrays support common operations like adding elements at the end (if the array is resizable), inserting elements at a specific position, deleting elements, and searching for elements.

In Python, lists (which are similar to arrays) support common operations like adding elements, inserting elements, deleting elements, and searching for elements.

```Python
my_list = [1, 2, 3]

# Adding elements at the end
my_list.append(4)  # [1, 2, 3, 4]

# Inserting elements at a specific position
my_list.insert(1, 10)  # [1, 10, 2, 3, 4]

# Deleting elements
my_list.remove(2)  # [1, 10, 3, 4]

# Searching for elements
index = my_list.index(3)  # 2 (index of element 3)
```

8. Multidimensional Arrays: Some programming languages support multidimensional arrays, which are arrays of arrays. For example, a 2D array is an array of arrays, forming a grid or matrix.

Python does not have built-in support for true multidimensional arrays, but you can simulate them using lists of lists. Here's an example of a 2D array (a list of lists):

```Python
# Creating a 2D array (list of lists)
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a 2D array
element = grid[0][0]  # Accessing the element at the first row, first column (1)
```

# Linked Lists
A linked list is a linear data structure consisting of a sequence of elements, where each element points to the next element in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory locations; instead, they use nodes to connect elements together.

Linked lists are versatile data structures and are used in various applications and algorithms, such as implementing stacks, queues, and hash tables, as well as solving problems related to dynamic data storage and management.

## Key Characteristics
1. Dynamic Size: Linked lists do not have a fixed size, and elements can be dynamically added or removed without the need to specify a fixed size beforehand.

2. Insertion and Deletion: Linked lists support efficient insertion and deletion of elements at the beginning, end, or a specific position in the list.

3. Traversal: You can traverse a linked list by following the references from one node to the next, making it easy to iterate through the elements.

4. Random Access: Unlike arrays, linked lists do not provide constant-time (O(1)) random access to elements. Accessing an element at a specific index requires traversing the list from the beginning, which takes O(n) time in the worst case, where n is the number of elements.

5. Memory Efficiency: Linked lists can be more memory-efficient than arrays in some scenarios, as nodes can be allocated dynamically and do not require contiguous memory.

6. Common Operations: Linked lists support common operations like reversing the list, finding the middle element, merging two lists, detecting cycles (in the case of circular linked lists), and more.

## Node Structure
Each node consists of two parts: a data element and a reference (or pointer) to the next node in the sequence. 

```Python
class Node:
    def __init__(self, data):
        self.data = data  # Data element
        self.next = None  # Reference to the next node
```

It's important to note that nodes may contain additional information, depending on the use case.

### Singly Linked List
In a singly linked list, each node points to the next node in the sequence, forming a unidirectional chain of nodes. The last node typically points to None to indicate the end of the list.

```Python
# Creating a simple singly linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
```

### Doubly Linked List
In a doubly linked list, each node has references to both the next node and the previous node in the sequence, allowing for bidirectional traversal.

```Python
class DoublyNode:
    def __init__(self, data):
        self.data = data       # Data element
        self.next = None       # Reference to the next node
        self.prev = None       # Reference to the previous node
```

### Circular Linked List
In a circular linked list, the last node points back to the first node, forming a closed loop.

```Python
# Creating a simple circular linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
node3.next = node1  # Circular reference
```

## Linked List Uses
### Dynamic Memory Allocation
In Python, linked lists can be particularly useful when you need to allocate and deallocate memory dynamically, and they provide flexibility in managing memory efficiently. You can reference the Singly Linked List example above to see this.

### Insertions and Deletions
Linked lists excel at efficient insertions and deletions. In Python, you can insert a new node at the beginning or in the middle of the list by adjusting references, and you can remove nodes by updating references as well.

```Python
# Inserting a new node at the beginning
new_node = Node(5)
new_node.next = node1
node1 = new_node

# Deleting a node
node2 = node2.next
```

# Stacks
A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, which means that the last item added to the stack is the first one to be removed. Stacks are commonly used for managing function calls, tracking state changes, and performing operations in reverse order.

## Key Characteristics
1. LIFO (Last-In-First-Out) Order: Items are added and removed from the top of the stack. The last item pushed onto the stack is the first one to be popped off.

```Python
# Creating a stack and performing push and pop operations
stack = []
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack

top_item = stack.pop()  # Pop the top item (2)
```

2. Push and Pop Operations: Stacks support two primary operations—push (to add an item to the top of the stack) and pop (to remove the top item).

```Python
# Creating a stack and performing push and pop operations
stack = []
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack

top_item = stack.pop()  # Pop the top item (2)
```

3. Constant-Time Operations: Push and pop operations on stacks have constant-time (O(1)) complexity because they involve only the top of the stack.

```Python
# Creating a stack and performing push and pop operations
stack = []
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack

top_item = stack.pop()  # Pop the top item (2)
```

## Use Cases
- Managing function call execution and handling return values (call stack).
- Parsing expressions and evaluating them (expression evaluation).
- Tracking state changes in algorithms (backtracking).
- Undo/redo functionality in applications (e.g., text editors).

# Queues
A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle, which means that the first item added to the queue is the first one to be removed. Queues are commonly used for managing tasks with ordered processing and scheduling.

## Key Characteristics
1. FIFO (First-In-First-Out) Order: Items are added at the rear of the queue and removed from the front. The first item enqueued is the first one dequeued.

```Python
# Creating a queue and performing enqueue and dequeue operations
queue = []
queue.append(1)  # Enqueue 1 at the rear of the queue
queue.append(2)  # Enqueue 2 at the rear of the queue

front_item = queue.pop(0)  # Dequeue the front item (1)
```

2. Enqueue and Dequeue Operations: Queues support two primary operations—enqueue (to add an item to the rear of the queue) and dequeue (to remove the front item).

```Python
# Creating a queue and performing enqueue and dequeue operations
queue = []
queue.append(1)  # Enqueue 1 at the rear of the queue
queue.append(2)  # Enqueue 2 at the rear of the queue

front_item = queue.pop(0)  # Dequeue the front item (1)
```

It's worth mentioning Python's collections module provides a deque (double-ended queue) data structure, which is commonly used for implementing queues. 

```Python
from collections import deque

# Creating a queue using a deque
queue = deque()

# Enqueue operation (adding elements to the rear of the queue)
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # Output: deque([1, 2, 3])

# Dequeue operation (removing elements from the front of the queue)
front_item = queue.popleft()  # Dequeue the front item (1)

print(front_item)  # Output: 1
print(queue)       # Output: deque([2, 3])
```

3. Constant-Time Operations: Enqueue and dequeue operations on queues have constant-time (O(1)) complexity because they involve only the front and rear of the queue.

```Python
# Creating a queue and performing enqueue and dequeue operations
queue = []
queue.append(1)  # Enqueue 1 at the rear of the queue
queue.append(2)  # Enqueue 2 at the rear of the queue

front_item = queue.pop(0)  # Dequeue the front item (1)
```

## Use Cases:
- Task scheduling and resource allocation (job queues).
- Implementing breadth-first search in graphs (graph traversal).
- Handling requests in web servers (request processing).
- Print job management in printers (print queues).

# Hash Sets
A hash set is a collection of unique values, where each value is hashed to a unique location within the set. Hash sets are commonly used when you need to check for the presence of an element or store a collection of distinct elements efficiently.

## Key Characteristics
1. Uniqueness: Hash sets contain only unique elements. Duplicates are automatically eliminated.

```Python
# Creating a hash set with unique elements
unique_set = set()

# Adding elements to the set (duplicates are automatically eliminated)
unique_set.add(10)
unique_set.add(20)
unique_set.add(10)  # Duplicate element, not added

print(unique_set)  # Output: {10, 20}
```

2. Hashing: Elements are hashed to determine their storage location within the set. A good hash function minimizes collisions, where different elements map to the same location.

```Python
# Custom hash function for integers
def custom_hash(x):
    return x % 5  # Example hash function

# Creating a hash set with a custom hash function
hash_set = set()

# Adding elements to the set (hashing determines storage location)
hash_set.add(10)  # Hashes to 0
hash_set.add(20)  # Hashes to 0 (collision)
hash_set.add(30)  # Hashes to 1

print(hash_set)  # Output: {10, 30, 20}
```

3. Constant-Time Operations: On average, hash sets provide constant-time (O(1)) operations for insertion, deletion, and lookup.
```Python
# Creating a hash set
my_set = set()

# Insertion (constant-time average)
my_set.add(10)
my_set.add(20)

# Lookup (constant-time average)
element_exists = 10 in my_set  # True

# Deletion (constant-time average)
my_set.remove(20)

print(my_set)         # Output: {10}
print(element_exists)  # Output: True
```

4. Dynamic Sizing: Hash sets can dynamically resize to accommodate more elements efficiently.

```Python
# Creating a hash set with elements
my_set = set([10, 20, 30])

# Inserting elements (dynamic resizing)
my_set.add(40)  # Resizing may occur here if the load factor threshold is reached

print(my_set)  # Output: {10, 20, 30, 40}
```


## Use Cases
- Checking for the presence of an element in a large collection (e.g., membership test).
- Removing duplicates from a list or collection of data.
- Efficiently storing a collection of unique values without manual checks for uniqueness.

# Hash Maps (Hash Tables)
A hash map, also known as a hash table, is a data structure that associates keys with values. Each key is hashed to determine its storage location, and the associated value is stored at that location. Hash maps are widely used for efficient data retrieval and storage, with keys serving as unique identifiers.

## Key Characteristics
1. Key-Value Pairs: Hash maps store data as key-value pairs, where each key is associated with a specific value.

```Python
# Creating a hash map with key-value pairs
my_dict = {}

# Adding key-value pairs to the hash map
my_dict['apple'] = 5
my_dict['banana'] = 3
my_dict['cherry'] = 8

print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 8}
```

2. Hashing: Similar to hash sets, hash maps use hashing to determine the storage location of keys and values.

```Python
# Custom hash function for strings
def custom_hash(key):
    hash_value = 0
    for char in key:
        hash_value += ord(char)  # Sum of ASCII values of characters
    return hash_value

# Creating a hash map with a custom hash function
custom_map = {}

# Adding key-value pairs (hashing determines storage location)
custom_map['cat'] = 'meow'  # Hashes to 314
custom_map['dog'] = 'woof'  # Hashes to 316

print(custom_map)  # Output: {'cat': 'meow', 'dog': 'woof'}
```

3. Constant-Time Operations: On average, hash maps provide constant-time (O(1)) operations for insertion, deletion, and lookup based on keys.

```Python
# Creating a hash map
my_dict = {'apple': 5, 'banana': 3, 'cherry': 8}

# Lookup (constant-time average)
value = my_dict['banana']  # Retrieving the value associated with 'banana'

# Insertion (constant-time average)
my_dict['date'] = 6  # Adding a new key-value pair

# Deletion (constant-time average)
del my_dict['apple']  # Removing the 'apple' key-value pair

print(my_dict)  # Output: {'banana': 3, 'cherry': 8, 'date': 6}
```

4. Dynamic Sizing: Hash maps can dynamically resize to accommodate more key-value pairs efficiently.

```Python
# Creating a hash map with elements
my_dict = {'apple': 5, 'banana': 3, 'cherry': 8}

# Inserting elements (dynamic resizing)
my_dict['date'] = 6  # Resizing may occur here if the load factor threshold is reached

print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 6}
```

Python's built-in dictionary (dict) handles the details of hashing, collision resolution, and resizing, making it easy to work with hash maps while benefiting from the characteristics mentioned above.

## Use Cases
- Implementing data caches, such as in-memory caching of database query results.
- Efficiently looking up values associated with specific keys, as in dictionaries.
- Storing and retrieving key-value pairs for rapid access to data.

# Trees
Trees are hierarchical data structures that are widely used in computer science and software engineering for organizing and managing data in a hierarchical manner. They have a root node at the top and consist of nodes connected by edges, forming branches and leaves.

## Key Characteristics
1. Hierarchy: Trees organize data in a hierarchical structure with a root node at the top and child nodes branching out from the root. This hierarchical structure allows for the representation of complex relationships among elements. Child nodes can further branch out into their own child nodes, creating a tree-like structure that reflects parent-child relationships.

2. Hierarchical Relations: Trees represent hierarchical relationships between elements. For example, in a file system, directories and subdirectories are organized in a tree structure where each directory can contain files and other subdirectories. This hierarchical representation is essential for organizing and accessing data efficiently.


## Tree Structure
A tree can be implemented with data and its children. In Python, a common way to represent a tree is by defining a TreeNode class that contains data and references to its child nodes.

```Python
# Implementation of TreeNode Class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
```

The key parts of the tree structure are:

1. Root Node: The root node is the topmost node in the tree and serves as the starting point for traversing the tree's structure. It represents the overall entity or concept that the tree represents.

```Python
# Creating a tree with a root node
root = TreeNode("A")
```

2. Parent and Child Nodes: Nodes in a tree are connected in a hierarchical manner, forming a parent-child relationship. Each node (except for the root) has a parent node and may have zero or more child nodes. This parent-child relationship defines the structure of the tree and allows for the organization of data into meaningful categories.
Python

```Python
# Creating a tree with parent and child nodes
root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
root.children.append(child1)
root.children.append(child2)
```

3. Leaf Nodes: Leaf nodes are nodes in the tree that have no child nodes. They are the endpoints of branches in the tree and represent individual data elements or entities. Leaf nodes are essential for representing the lowest-level data in the hierarchical structure.

```Python
# Creating a tree with leaf nodes
root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
root.children.append(child1)
root.children.append(child2)
```

## Use Cases
- Representing hierarchical data: Trees are used to represent hierarchical structures such as file systems, organization charts, and family trees. They provide an intuitive way to organize and navigate complex relationships within data.
- Implementing specialized data structures: Trees are used to implement data structures like binary trees, binary search trees (BSTs), and AVL trees. These structures enable efficient searching, sorting, and data retrieval operations.
- Parsing and compilation: Trees are employed in parsing expressions and representing abstract syntax trees (ASTs) in compilers and interpreters. They help in analyzing and processing code or expressions.
- Machine learning and decision trees: Trees are used in machine learning for building decision trees, which are used in classification and regression tasks. Decision trees help make informed decisions based on input data.

# Graphs
Graphs are versatile data structures used in computer science and various fields to represent complex relationships and connections between data elements. Unlike trees, graphs do not have a hierarchical structure and can capture a wide range of relationships.

## Key Characteristics
1. Nodes and Edges: Graphs consist of two main components - nodes (vertices) and edges. Nodes represent individual data elements, while edges represent connections or relationships between nodes.

2. Edges May Have Weights: Edges in a graph can have associated weights or costs, which can represent distances, costs, or any other quantitative information related to the relationship between nodes.

3. Directed vs. Undirected: Graphs can be either directed or undirected. In a directed graph, edges have a direction, indicating a one-way relationship from one node to another. In an undirected graph, edges have no direction, representing a two-way relationship between nodes.

### Graph Structure
Graphs can be implemented with nodes and edges, and they can be represented as adjacency lists or adjacency matrices.

```Python
# Example of a graph using an adjacency list representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B'],
    'D': ['B']
}
```

The key parts of the graph structure are:

1. Nodes (Vertices): Nodes in a graph represent data elements, entities, or points of interest. Each node can have a unique label or identifier to distinguish it from other nodes.
2. Edges: Edges in a graph represent relationships or connections between nodes. They can be directed (with a specific direction) or undirected (bidirectional). Edges can also have associated weights or costs, which can be used for various applications, such as route planning or network optimization.
3. Directed and Undirected Graphs: The nature of edges determines whether a graph is directed or undirected. In directed graphs, edges have a direction, indicating a one-way relationship. In undirected graphs, edges have no direction, representing mutual connections between nodes.

## Use Cases
- Graphs are used in a wide range of applications across different fields due to their ability to model complex relationships and connections. Some common use cases include:
- Social networks: Graphs are used to model connections between users in social networks. Each user is a node, and relationships (friendship, follow, etc.) are represented as edges.
- Transportation and route planning: Graphs are used to model road networks, flight routes, and public transportation systems. Nodes represent locations (e.g., cities or airports), and edges represent routes or connections between them.
- Network topology: In computer networks, graphs are used to represent the topology of a network. Nodes represent devices (e.g., routers or switches), and edges represent connections between them.
- Recommendation systems: Graphs can model user preferences and item relationships in recommendation systems. Nodes represent users and items, and edges represent user interactions or item similarities.
- Graph algorithms: Many algorithms, such as breadth-first search (BFS) and depth-first search (DFS), are applied to graphs to solve various problems, including pathfinding, connectivity analysis, and network flow optimization.
