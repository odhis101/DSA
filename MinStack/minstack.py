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
