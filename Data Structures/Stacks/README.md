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