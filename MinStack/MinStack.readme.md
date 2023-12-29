Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) — Pushes the element x onto the stack.
pop() — Removes the element on the top of the stack.
top() — Retrieves the element on the top of the stack.
get_min() — Retrieves the minimum element in the stack.


Example 

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
min_stack.get_min()  # Returns -3
min_stack.pop()
min_stack.top()      # Returns 0
min_stack.get_min()  # Returns -2
