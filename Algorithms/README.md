# Algorithms

# Table of Contents
- [Big O Notation](#big-o-notation)
- [Sorting](#sorting)
- [Searching](#searching)
- [Strings](#strings)
- [Recursive and Backtracking](#recursive-and-backtracking)
- [Divide and Conquer](#divide-and-conquer)
- [Tree Traversals](#tree-traversals)
- [Graph](#graph)
- [Dynamic Programming](#dynamic-programming)

## Big O Notation
Big O Notation is a mathematical notation used in computer science and algorithm analysis to describe the upper bound or worst-case time complexity of an algorithm. It provides a way to classify algorithms based on how their execution time grows in relation to the size of the input data. Understanding Big O Notation is crucial for evaluating algorithm efficiency and making informed decisions when choosing algorithms for specific tasks.

Big O Notation expresses the time complexity of an algorithm as a function of the input size (typically denoted as "n"). It allows us to answer questions like "How does the execution time of an algorithm scale as the input size increases?" By analyzing the Big O complexity of an algorithm, we can make informed decisions about which algorithm to choose for a particular problem.

### Common Notations
- O(1) - Constant Time Complexity: Algorithms with constant time complexity execute in the same amount of time regardless of the input size. They have a fixed number of operations.

- O(log n) - Logarithmic Time Complexity: Algorithms with logarithmic time complexity reduce the problem size by a constant factor in each step. They are efficient for large datasets.

- O(n) - Linear Time Complexity: Algorithms with linear time complexity have their execution time grow proportionally with the size of the input. Doubling the input size roughly doubles the execution time.

- O(n log n) - Linearithmic Time Complexity: Algorithms with linearithmic time complexity combine linear and logarithmic growth. They are efficient for many sorting and divide-and-conquer algorithms.

- O(n^2) - Quadratic Time Complexity: Algorithms with quadratic time complexity have their execution time grow with the square of the input size. They are less efficient and may become impractical for large inputs.

- O(n^k) - Polynomial Time Complexity: Algorithms with polynomial time complexity have their execution time grow with a power of the input size. The value of "k" determines the degree of the polynomial.

- O(2^n) - Exponential Time Complexity: Algorithms with exponential time complexity have execution times that grow exponentially with the input size. They are highly inefficient and impractical for large inputs.

## Sorting
Sorting is a fundamental operation in computer science and data processing. It involves arranging a collection of items or data elements in a specific order, typically in ascending or descending order. Sorting is a key step in various algorithms and applications, including searching, data analysis, and database management. This section explores different sorting algorithms, their characteristics, and their use cases.


### Bubble Sort
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, indicating that the list is sorted. Bubble Sort is easy to understand but not very efficient, especially for large lists.

#### Key Characteristics
1. Comparison-Based: Bubble Sort compares adjacent elements in the list and swaps them if they are out of order. This comparison and swapping process continues until the entire list is sorted.
2. In-Place Sorting: Bubble Sort operates on the original list and does not require additional memory for temporary data structures. It is an in-place sorting algorithm.
3. Stable Sorting: Bubble Sort is a stable sorting algorithm, meaning it maintains the relative order of equal elements. If two elements have the same value, their original order will be preserved in the sorted list.
4. Time Complexity: Bubble Sort has a worst-case and average-case time complexity of O(n^2), making it inefficient for large datasets. However, it has a best-case time complexity of O(n), which occurs when the list is already sorted.

Use Case: Bubble Sort is rarely used in practice due to its inefficiency for large datasets. It may be suitable for small lists or as a teaching example to illustrate sorting concepts.

Below is a Python implementation of bubble sort:

```Python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps are made in a pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made in a pass, the list is already sorted
        if not swapped:
            break
```

### Selection Sort
Selection Sort is a simple comparison-based sorting algorithm that divides the input list into two parts: the sorted portion and the unsorted portion. It repeatedly selects the smallest (or largest, depending on the desired order) element from the unsorted portion and moves it to the end of the sorted portion. Selection Sort is straightforward to implement but not very efficient for large lists.

#### Key Characteristics
1. Comparison-Based: Selection Sort selects the smallest (or largest) element by comparing elements in the unsorted portion of the list and moving the selected element to its correct position in the sorted portion.
2. In-Place Sorting: Selection Sort is an in-place sorting algorithm, as it sorts the original list without requiring additional memory for temporary data structures.
3. Not Stable: Selection Sort is not a stable sorting algorithm. It may change the relative order of equal elements.
4. Time Complexity: Selection Sort has a consistent time complexity of O(n^2), regardless of the input data. It is inefficient for large datasets but may perform better than Bubble Sort in some cases.

Use Cases: Selection Sort, like Bubble Sort, is not commonly used for large datasets. It can be suitable for small lists or as a simple sorting algorithm when stability is not a concern.

Below is a Python implementation of selection sort.
```Python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the smallest element with the current position
        arr[i], arr[min_index] = arr[min_index], arr[i]
```

### Insertion Sort
Insertion Sort is a simple comparison-based sorting algorithm that builds the final sorted list one element at a time. It takes each element from the unsorted portion of the list and inserts it into its correct position within the sorted portion. Insertion Sort is efficient for small datasets and is often used for partially sorted lists.

#### Key Characteristics
1. Comparison-Based: Insertion Sort compares each element with the elements in the sorted portion of the list and inserts it into the correct position.
2. In-Place Sorting: Insertion Sort is an in-place sorting algorithm, as it sorts the original list without requiring additional memory for temporary data structures.
3. Stable Sorting: Insertion Sort is a stable sorting algorithm, preserving the relative order of equal elements.
4. Time Complexity: The time complexity of Insertion Sort is O(n^2) in the worst and average cases. However, it can perform well for small datasets and lists that are already partially sorted, where its time complexity can be closer to O(n).

Use Cases: Insertion Sort is suitable for small lists or lists with only a few elements out of order. It is often used as a building block in more advanced sorting algorithms.

```Python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

### Merge Sort
Merge Sort is a divide-and-conquer sorting algorithm that recursively divides the input list into smaller sublists, sorts them, and then merges them back together to produce a sorted list. Merge Sort is known for its stability and consistent O(n log n) time complexity, making it efficient for large datasets.

#### Key Characteristics
1. Divide and Conquer: Merge Sort divides the input list into smaller sublists, sorts them independently, and then merges them back together to create a sorted list. This divide-and-conquer approach leads to its efficiency.
2. Stable Sorting: Merge Sort is a stable sorting algorithm, preserving the relative order of equal elements.
3. Efficient Time Complexity: Merge Sort has a time complexity of O(n log n) in the worst, average, and best cases, making it suitable for sorting large datasets.

Use Cases: Merge Sort is commonly used when a stable, efficient, and predictable sorting algorithm is needed, especially for large datasets. It is often used as the basis for external sorting algorithms.

Below in a Python implementation of Merge sort.
```Python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

### Quick Sort
Quick Sort is a divide-and-conquer sorting algorithm that selects a "pivot" element from the input list and partitions the list into two sublists: elements less than the pivot and elements greater than the pivot. It then recursively sorts the sublists. Quick Sort is known for its efficiency and is often used in practice.

#### Key Characteristics
1. Divide and Conquer: Quick Sort selects a pivot element, divides the list into smaller sublists, and sorts them independently. This divide-and-conquer approach contributes to its efficiency.
2. In-Place Sorting: Quick Sort can be implemented as an in-place sorting algorithm, which means it sorts the original list without requiring additional memory for temporary data structures. However, some implementations may use additional memory for stability.
3. Not Always Stable: Quick Sort is not a stable sorting algorithm. It may change the relative order of equal elements.
4. Efficient Time Complexity: Quick Sort has an average and best-case time complexity of O(n log n), making it highly efficient for large datasets. However, in the worst case, it can be O(n^2) if poorly chosen pivot elements cause unbalanced partitions.

Use Cases: Quick Sort is widely used for its efficiency and is the default sorting algorithm in many programming languages and libraries. It is suitable for sorting large datasets in-memory and out-of-memory.

Below is a Python implementation of quick sort:

```Python
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right
```

### Heap Sort
Heap Sort is a comparison-based sorting algorithm that leverages the properties of a binary heap data structure. It builds a max-heap (for ascending order) or a min-heap (for descending order) from the input list and repeatedly removes the root element (the maximum or minimum, depending on the heap type) to build the sorted list. Heap Sort is efficient and can achieve a consistent O(n log n) time complexity.

#### Key Characteristics
1. Heap Data Structure: Heap Sort relies on a binary heap data structure, which is a binary tree with specific properties (max-heap or min-heap). It uses the heap to efficiently find the maximum (for ascending order) or minimum (for descending order) element in the list.
2. In-Place Sorting: Heap Sort can be implemented as an in-place sorting algorithm, meaning it sorts the original list without requiring additional memory for temporary data structures.
3. Not Always Stable: Heap Sort is not a stable sorting algorithm. It may change the relative order of equal elements.
4. Efficient Time Complexity: Heap Sort has an average and worst-case time complexity of O(n log n), making it efficient for large datasets.

Use Cases: Heap Sort is often used when a stable sorting algorithm is not required, and efficiency is crucial. It is suitable for sorting large datasets and is used in various applications, including priority queues and scheduling algorithms.

```Python
def heap_sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root (max element) with the last element
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)
```

## Searching
Searching algorithms are essential in computer science and data processing to locate specific elements within a data structure, such as an array or list. These algorithms are designed to efficiently find the target element(s) within the data, and their choice depends on factors like data structure properties, data ordering, and efficiency requirements. This section explores different searching algorithms, their characteristics, and use cases.

### Linear Search
Linear Search, also known as Sequential Search, is a straightforward searching algorithm that iterates through the entire dataset from start to finish, checking each element one by one until the target element is found or the entire dataset has been scanned. It is suitable for unordered data but can be inefficient for large datasets.

#### Key Characteristics
1. Linear Time Complexity: Linear Search has a time complexity of O(n) in the worst-case scenario, where "n" is the size of the dataset. This means the algorithm's time requirements grow linearly with the dataset size.
2. Simple Implementation: Linear Search is easy to implement and does not require the data to be sorted. It is useful when the dataset lacks any specific ordering.

Use Cases: Linear Search is suitable for small datasets or scenarios where data is not ordered or indexed. It is also commonly used for searching in linked lists.

```Python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### Binary Search
Binary Search is a more efficient searching algorithm designed for ordered datasets. It repeatedly divides the dataset in half and compares the middle element with the target value. If the target is smaller, the algorithm continues searching in the lower half; if the target is larger, it searches in the upper half. Binary Search quickly narrows down the search space and is highly efficient for large ordered datasets.

#### Key Characteristics
1. Logarithmic Time Complexity: Binary Search has a time complexity of O(log n) in the worst-case scenario. It effectively reduces the search space by half in each step, making it suitable for large datasets.
2. Ordered Data Requirement: Binary Search requires the data to be sorted in ascending or descending order to work correctly. This requirement ensures that the algorithm can eliminate half of the remaining elements in each step.

Use Cases: Binary Search is ideal for searching in sorted arrays or lists. It is commonly used in searching applications and is a fundamental algorithm in computer science.

```Python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```


## Strings
String algorithms are specialized algorithms used for processing and manipulating strings, which are sequences of characters. These algorithms are crucial in various applications, such as text processing, pattern matching, and data parsing. This section explores different string algorithms, their characteristics, and use cases.

### Knuth-Morris-Pratt (KMP) Algorithm
The Knuth-Morris-Pratt (KMP) Algorithm is used for substring searching within a longer string. It efficiently finds all occurrences of a substring by avoiding unnecessary character comparisons.

#### Key Characteristics
1. Time Complexity: The KMP Algorithm achieves a time complexity of O(n + m), where "n" is the length of the text and "m" is the length of the substring to be searched.
2. Partial Match Table: KMP uses a precomputed partial match table to skip comparisons when a mismatch occurs. This enhances its efficiency.

Use Cases: KMP is suitable for searching substrings within texts, including applications like text editors, search engines, and string pattern matching.

```Python
def build_partial_match_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        table[i] = j
    return table

def kmp_search(text, pattern):
    partial_match_table = build_partial_match_table(pattern)
    matches = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = partial_match_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = partial_match_table[j - 1]
    return matches
```

### Boyer-Moore Algorithm
The Boyer-Moore Algorithm is another efficient substring searching algorithm. It uses a "bad character" and "good suffix" rule to skip unnecessary comparisons.

#### Key Characteristics
1. Time Complexity: The Boyer-Moore Algorithm achieves a time complexity of O(n + m) in practice. It is known for its speed in practical applications.
2. Heuristic Rules: Boyer-Moore uses heuristic rules to skip comparisons based on the last occurrence of characters in the substring and the text.

Use Cases: Boyer-Moore is widely used for searching substrings in text processing, including searching in large documents and string matching.

```Python
def build_bad_character_table(pattern):
    table = {}
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - 1 - i
    return table

def build_good_suffix_table(pattern):
    m = len(pattern)
    suffix_table = [-1] * m
    j = 0
    for i in range(m - 1, -1, -1):
        if is_suffix(pattern, i + 1):
            j = m - 1 - i
        suffix_table[i] = j
    return suffix_table

def is_suffix(pattern, p):
    j = len(pattern) - 1
    for i in range(p, -1, -1):
        if pattern[i] != pattern[j]:
            return False
        j -= 1
    return True

def boyer_moore_search(text, pattern):
    bad_character_table = build_bad_character_table(pattern)
    good_suffix_table = build_good_suffix_table(pattern)
    matches = []
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            matches.append(i)
            i += good_suffix_table[0]
        else:
            i += max(bad_character_table.get(text[i + j], 0), good_suffix_table[j])
    return matches
```

### String Reversal
String reversal is a common string manipulation task that involves reversing the order of characters in a string.

#### Key Characteristics
1. Time Complexity: String reversal can be achieved with a time complexity of O(n), where "n" is the length of the string.
2. In-Place vs. Out-of-Place: String reversal can be done in-place (modifying the original string) or out-of-place (creating a new reversed string).

Use Cases: String reversal is useful in various applications, including text processing, cryptography, and data transformation.

```Python
def reverse_string(input_string):
    return input_string[::-1]
```

### String Concatenation
String concatenation involves combining two or more strings into a single string.

#### Key Characteristics
1. Time Complexity: The time complexity is O(n), where "n" is the total length of the strings being concatenated.
2. In-Place vs. Out-of-Place: Some string concatenation methods modify the original string (in-place), while others create a new string (out-of-place).

Use Cases: String concatenation is essential for building longer strings from smaller components, such as in text generation, logging, and data serialization.

```Python
def concatenate_strings(strings):
    return ''.join(strings)

# Example usage
string_list = ['abc', 'def']
result = concatenate_strings(string_list)
print(result)  # Output: 'abcdef'
```

```Python
s = 'abc'
t = 'def'
result = s + t
print(result)  # Output: 'abcdef'
```

### Regular Expressions
Regular expressions (regex) are a powerful tool for string matching and pattern recognition. They allow you to define search patterns and perform complex string manipulations.

#### Key Characteristics
1. Versatility: Regular expressions support a wide range of string matching and manipulation tasks, from simple substring searches to complex pattern extractions.
2. Pattern Language: Regular expressions use a pattern language to specify search patterns, making them highly flexible.
3. Efficiency: The efficiency of regular expressions can vary based on the complexity of the pattern. Simple patterns can be matched quickly, but complex patterns may require more processing time.

Use Cases: Regular expressions are used in text processing, data validation, web scraping, and many other applications that involve string matching.

```Python
import re

# Example of using regular expressions
text = "Hello, my email is example@email.com"
pattern = r'\S+@\S+'
matches = re.findall(pattern, text)
print(matches)  # Output: ['example@email.com']
```

### Rabin-Karp Algorithm
The Rabin-Karp Algorithm is a string matching algorithm that uses hashing to find occurrences of a pattern in a text efficiently.

#### Key Characteristics
1. Time Complexity: Rabin-Karp has an average-case time complexity of O(n + m), where "n" is the length of the text and "m" is the length of the pattern. It is particularly efficient for large texts and patterns.
2. Hashing: Rabin-Karp uses rolling hashing to compute hash values for the text and the pattern. This allows for quick comparisons and shifts.

Use Cases: Rabin-Karp is used for pattern matching in text processing, plagiarism detection, and substring searching.

```Python
def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:m])
    matches = []

    for i in range(n - m + 1):
        if text_hash == pattern_hash and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            text_hash = (text_hash - ord(text[i])) // 256 + ord(text[i + m]) * (256 ** (m - 1))

    return matches
```

## Divide and Conquer
Divide and Conquer is a fundamental algorithmic technique that involves breaking down a complex problem into smaller, more manageable subproblems, solving these subproblems independently, and then combining their solutions to solve the original problem. This section explores different Divide and Conquer Algorithms, their characteristics, and use cases.

Divide and Conquer algorithms follow a three-step process: Divide, Conquer, and Combine. These algorithms are particularly effective when a problem can be divided into smaller, similar subproblems that can be solved independently.

You can refer to Merge Sort and Quick Sort above for examples of this.

## Recursive and Backtracking
Recursive algorithms are algorithms that solve problems by breaking them down into smaller, self-similar subproblems. Backtracking algorithms are a subset of recursive algorithms that systematically explore all possible solutions to a problem and backtrack when a solution is not feasible. This section explores different Recursive and Backtracking Algorithms, their characteristics, and use cases.

Recursive and Backtracking algorithms are particularly useful when a problem can be naturally divided into smaller, similar subproblems. Recursive algorithms solve these subproblems through recursive calls, while Backtracking algorithms explore possible solutions and backtrack when necessary.

### Factorial Calculation
Factorial Calculation is a recursive algorithm that calculates the factorial of a non-negative integer "n."

#### Key Characteristics
1. Time Complexity: Factorial Calculation has a time complexity of O(n) and a space complexity of O(n) due to recursive function calls.
2. Recursive Definition: The factorial of n (denoted as n!) is defined recursively as n! = n * (n-1)!

```Python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

### Fibonacci Sequence
The Fibonacci Sequence is a recursive algorithm that generates the nth Fibonacci number, where each number is the sum of the two preceding ones.

#### Key Characteristics
1. Time Complexity: The recursive Fibonacci algorithm has exponential time complexity (O(2^n)) due to redundant calculations.
2. Recursive Definition: The nth Fibonacci number is defined recursively as F(n) = F(n-1) + F(n-2).

```Python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

### Depth-First Search (DFS)
Depth-First Search is a recursive graph traversal algorithm that explores as far as possible along each branch before backtracking.

#### Key Characteristics
1. Time Complexity: DFS has a time complexity of O(V + E), where "V" is the number of vertices and "E" is the number of edges in the graph.
2. Stack-Based Recursion: DFS uses a stack-based recursive approach to explore vertices and their neighbors.

Below is the recursive implementation. I'll include the iterative stack approach in the graph algorithm section. 
``` Python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()

def dfs_recursive(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(neighbor)

# Example usage
dfs_recursive('A')
```

## Tree Traversals
Tree Traversal algorithms are used to visit and process all the nodes in a tree data structure systematically. These algorithms provide a way to explore the tree's structure and retrieve or manipulate data from each node. This section explores different Tree Traversal Algorithms, their characteristics, and use cases.

Tree Traversal algorithms are used to navigate and process tree structures, which consist of nodes connected by edges. These algorithms can be applied to various types of trees, including binary trees and general trees.

### Depth First Traversal
Depth-First Traversal algorithms explore the tree structure by visiting nodes along a path as deeply as possible before backtracking. There are three common depth-first traversals: Preorder, Inorder, and Postorder.

#### Preorder Traversal
Preorder Traversal visits nodes in the following order: root, left subtree, right subtree.

Usage: Preorder traversal is useful for making a copy of the tree (cloning), serializing the tree to a string, or evaluating expressions in expression trees.


Here is the recursive implementation in Python:
```Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root is None:
        return []
    result = [root.val]
    result.extend(preorder_traversal(root.left))
    result.extend(preorder_traversal(root.right))
    return result
```

Here is the non-recursive iteration using a stack:
```Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push the right child first (since it will be processed after the left child)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

### Inorder Traversal
Inorder Traversal visits nodes in the following order: left subtree, root, right subtree.

Usage: Inorder traversal is commonly used for sorting binary search trees (BSTs) and evaluating expressions represented as expression trees.

Here is the recursive implementation in Python
```Python
def inorder_traversal(root):
    if root is None:
        return []
    result = inorder_traversal(root.left)
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result
```

Here is the non-recursive implementation using a stack:
```Python
def inorder_traversal(root):
    if root is None:
        return []
    result = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result
```

### Postorder Traversal
Postorder Traversal visits nodes in the following order: left subtree, right subtree, root.

Usage: Postorder traversal is useful for deleting the tree (freeing memory) and evaluating postfix expressions.

Here is the recursive implementation in Python
```Python
def postorder_traversal(root):
    if root is None:
        return []
    result = postorder_traversal(root.left)
    result.extend(postorder_traversal(root.right))
    result.append(root.val)
    return result
```

Here in the non-recursive implementation in Python using a stack:

```Python
def postorder_traversal(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push the left child first (since it will be processed after the right child)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]  # Reverse the result to get postorder traversal
```

## Breadth-First Traversal
Breadth-First Traversal (BFS) explores the tree level by level, visiting all nodes at a given level before moving on to the next level.

Usage: BFS is commonly used for finding the shortest path between nodes in a tree, level-order traversal, and various graph algorithms.

```Python
from collections import deque

def breadth_first_traversal(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

## Graph

### Depth-First Search (DFS) 
DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking. We've already covered the recursive implementation above, so the non-recursive implementation of DFS uses a stack data structure to traverse the graph iteratively.


#### Key Characteristics
1. Time Complexity: The time complexity of the non-recursive DFS algorithm is O(V + E), where "V" is the number of vertices, and "E" is the number of edges in the graph.
2. Stack-Based Iteration: Non-recursive DFS uses a stack to simulate the recursive function call stack, ensuring that nodes are visited in the correct order.
3. Visited Set: To prevent revisiting nodes and to handle disconnected components, a "visited" set is maintained to keep track of visited nodes.
4. Stack Order: Nodes are pushed onto the stack in the reverse order of their neighbors to ensure that the leftmost neighbor is explored first.

Non-Recursive Python Implementation
```Python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def dfs_non_recursive(self, start):
        if start not in self.graph:
            return []
        
        result = []
        stack = [start]
        visited = set()

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Push neighbors onto the stack in reverse order to explore them in the correct order
                neighbors = self.graph[node][::-1]
                stack.extend(neighbors)
        
        return result

# Example usage:
graph = Graph()
graph.add_edge('A', ['B', 'C'])
graph.add_edge('B', ['D', 'E'])
graph.add_edge('C', ['F'])

dfs_result = graph.dfs_non_recursive('A')
print(dfs_result)  # Output: ['A', 'B', 'D', 'E', 'C', 'F']
```

### Breadth-First Search (BFS) Non-Recursive Implementation
Breadth-First Search (BFS) is a graph traversal algorithm that explores nodes level by level, visiting all nodes at a given level before moving on to the next level. The non-recursive implementation of BFS uses a queue data structure to traverse the graph iteratively.

#### Key Characteristics
1. Time Complexity: The time complexity of the non-recursive BFS algorithm is O(V + E), where "V" is the number of vertices, and "E" is the number of edges in the graph.
2. Queue-Based Iteration: Non-recursive BFS uses a queue to maintain the order of nodes to visit, ensuring that nodes at the current level are explored before moving to the next level.
3. Visited Set: Similar to non-recursive DFS, a "visited" set is maintained to prevent revisiting nodes and handle disconnected components.
4. Queue Order: Nodes are enqueued in the order of their neighbors to ensure that neighbors at the same level are visited in the correct order.

```Python
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def bfs_non_recursive(self, start):
        if start not in self.graph:
            return []
        
        result = []
        queue = deque([start])
        visited = set()

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Enqueue neighbors to explore them in the correct order
                neighbors = self.graph[node]
                queue.extend(neighbors)
        
        return result

# Example usage:
graph = Graph()
graph.add_edge('A', ['B', 'C'])
graph.add_edge('B', ['D', 'E'])
graph.add_edge('C', ['F'])

bfs_result = graph.bfs_non_recursive('A')
print(bfs_result)  # Output: ['A', 'B', 'C', 'D', 'E', 'F']
```

## Dynamic Programming
Dynamic Programming is a powerful technique used to solve optimization problems by breaking them down into smaller overlapping subproblems and storing their solutions to avoid redundant computations. DP algorithms are commonly used in various fields such as computer science, economics, and engineering to find optimal solutions efficiently.

There are two key characteristics to look out for:
1. Optimal Substructure: DP problems exhibit optimal substructure, meaning that the optimal solution to the problem can be constructed from the optimal solutions of its subproblems. This property allows for a recursive approach to solving the problem.
2. Overlapping Subproblems: DP problems have subproblems that are solved multiple times with the same inputs. DP algorithms store the solutions to these subproblems in a table or cache to avoid redundant calculations, which significantly improves efficiency.

There are two implementations of Dynamic Programming:
1. Memoization (Top-Down)
2. Tabulation (Bottom-Up)

### Memoization (Top-Down):
One approach to DP is memoization, where the recursive algorithm is enhanced with a data structure (usually a dictionary or array) to store the results of subproblems as they are computed. When a subproblem is encountered again, its solution is retrieved from the data structure rather than recalculating it.

### Tabulation (Bottom-Up):
Another approach is tabulation, where DP solutions are built iteratively from the smallest subproblems to the original problem. Tabulation typically uses an array or table to store intermediate results and builds up to the final solution.

### Approach to Solving
1. Understand the Problem
Before diving into the problem-solving process, it's essential to thoroughly understand the problem statement, including its constraints and the optimization goal. Identify what needs to be optimized (e.g., maximum/minimum value, longest/shortest path, etc.).

2. Identify the States
States represent the subproblems that need to be solved to reach the overall solution. States can be thought of as parameters that uniquely define the current problem's state. These states are often related to the problem's variables or dimensions. Key points to consider:
  1. What variables or parameters uniquely define the current state of the problem?
  2. Are there multiple dimensions or variables involved?
  3. Are there any constraints on the states?

3. Define the Recurrence Relation
The recurrence relation defines how the solution to the current state can be expressed in terms of the solutions to smaller subproblems. It is typically a mathematical equation that relates the current state to one or more previous states. Key considerations:
  1. Express the current state in terms of one or more previous states (subproblems).
  2. Understand how the optimization goal (e.g., maximizing/minimizing) is reflected in the recurrence relation.
  3. Consider the problem's constraints and ensure they are satisfied in the relation.

4. Specify the Base Cases
Base cases are the smallest subproblems for which the solutions are known without further recursion. They serve as stopping conditions for the recursive process. Pay attention to:
  1. Identify the simplest cases where no further recursion is needed.
  2. Ensure that base cases provide meaningful solutions.
  3. Base cases are often related to specific states where no further optimization is possible.

5. Choose Memoization or Tabulation
A common approach is to design memoization first, since many people find this more intuitive.

Decide whether to use memoization (top-down) or tabulation (bottom-up) to implement the DP solution. Each approach has its strengths:
  - Memoization: Use memoization when it's more intuitive to solve the problem recursively. It involves caching subproblem solutions as they are computed. Make sure to check the cache before computing a subproblem.
  - Tabulation: Use tabulation when efficiency is a concern or when the problem naturally lends itself to iterative calculation. In tabulation, you build up solutions iteratively from smaller subproblems.

### 1D Dynamic Programming
In 1D DP, the state space is represented using a one-dimensional array or list. Each element of the array corresponds to a unique state. Typically, in 1D DP, you are solving problems that involve a sequence or a single dimension of choices or decisions.

#### Key Characteristics of 1D DP:
1. Single Dimension: The state space consists of a single dimension, often representing positions or indices in a sequence.
2. State Transition: The transition from one state to another depends on a recurrence relation that considers only the previous state(s).

Examples: Problems that can be solved with 1D DP include calculating Fibonacci numbers, finding the longest increasing subsequence, and solving problems that involve a linear sequence.

### 2D (or Multi-Dimensional) Dynamic Programming
In 2D (or multi-dimensional) DP, the state space is represented using a two-dimensional or multi-dimensional array or matrix. Each combination of indices in the array corresponds to a unique state. Problems that involve making multiple choices or decisions with more complex dependencies often require 2D or multi-dimensional DP.

#### Key Characteristics of 2D DP:
1. Multiple Dimensions: The state space consists of two or more dimensions, each representing different aspects of the problem or different choices or decisions.
2. State Transition: The transition from one state to another depends on a recurrence relation that considers multiple previous states, often from different dimensions.

Examples: Problems that can be solved with 2D DP include finding the shortest path in a grid, solving knapsack problems, and optimizing problems with multiple constraints.
