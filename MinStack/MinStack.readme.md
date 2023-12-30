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


Solution 

we can use an auxiliary stack to keep track of the minimum element at each step. The idea is to maintain a stack that stores pairs of elements (current_element, current_min)

So something similar to the two sum approach,where additional information is kept to efficiently solve a particular problem. In the case of the Min Stack, we use an auxiliary stack (min_stack) to keep track of the minimum element at each step, allowing us to quickly retrieve the minimum element in constant time.

class MinStack:
    def __init__(self):
        # Initialize main stack and min stack
        self.main_stack = []
        self.min_stack = []

    def push(self, x):
        # If the stack is empty, push x onto both stacks
        if not self.main_stack:
            self.main_stack.append(x)
            self.min_stack.append(x)
        else:
            # Compare with the current minimum
            current_min = self.min_stack[-1]
            if x <= current_min:
                # Push x and the new minimum onto both stacks
                self.main_stack.append(x)
                self.min_stack.append(x)
            else:
                # Push only x onto the main stack, maintain current minimum on min stack
                self.main_stack.append(x)
                self.min_stack.append(current_min)

    def pop(self):
        # Pop from both stacks
        if self.main_stack:
            self.main_stack.pop()
            self.min_stack.pop()

    def top(self):
        # Retrieve the top element from the main stack
        if self.main_stack:
            return self.main_stack[-1]
        return None  # Stack is empty

    def get_min(self):
        # Retrieve the top element from the min stack
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Stack is empty
