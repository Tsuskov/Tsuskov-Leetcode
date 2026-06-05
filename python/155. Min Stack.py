class MinStack:

    def __init__(self):
        self.s1 = []  # Main stack to store all elements
        self.min_stack = []  # Auxiliary stack to store the minimum values

    def push(self, val: int) -> None: # O(1)
        self.s1.append(val) # Push the value to the main stack
        if not self.min_stack or val < self.min_stack[-1][0]: # If the min_stack is empty or the value is less than the top value of the min_stack
            self.min_stack.append([val, 1]) # Push the value to the min_stack
        elif val == self.min_stack[-1][0]: # If the value is equal to the top value of the min_stack
            self.min_stack[-1][1] += 1 # Increment the count of the top value of the min_stack

    def pop(self) -> None: # O(1)
        if not self.s1: # If the stack is empty
            return # Return
        
        top_val = self.s1.pop() # Pop the top value from the main stack
        if top_val == self.min_stack[-1][0]: # If the top value is equal to the top value of the min_stack
            self.min_stack[-1][1] -= 1  # Decrement the count of the top value of the min_stack
            if self.min_stack[-1][1] == 0: # If the count of the top value of the min_stack is 0
                self.min_stack.pop() # Pop the top value from the min_stack

    def top(self) -> int: # O(1)
        if not self.s1: # If the stack is empty
            raise IndexError("Stack is empty")  # Raise an IndexError
        return self.s1[-1] # Return the top value of the main stack

    def getMin(self) -> int: # O(1)
        if not self.min_stack: # If the min_stack is empty
            raise IndexError("Min stack is empty") # Raise an IndexError
        return self.min_stack[-1][0] # Return the top value of the min_stack