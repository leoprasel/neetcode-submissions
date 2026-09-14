class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_value_stack or self.min_value_stack[-1] > val:
            self.min_value_stack.append(val)
        else:
            self.min_value_stack.append(self.min_value_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_value_stack.pop()        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_value_stack[-1]
        
