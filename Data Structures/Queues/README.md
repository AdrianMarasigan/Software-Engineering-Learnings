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