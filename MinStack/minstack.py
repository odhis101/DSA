class MinStack:
    def __init__(self):
        # Initialize main stack and min stack
        self.main_stack = []
        self.min_stack = []

    def push(self, x):
        if not self.main_stack:
            self.main_stack.append(x)
            self.min_stack.append(x)
        else:
            current_min = self.min_stack[-1]
            if x <= current_min:
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

# Example Usage:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # Output: -3
min_stack.pop()
print(min_stack.top())      # Output: 0
print(min_stack.get_min())  # Output: -2
