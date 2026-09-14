class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if token == '+':
                    result = a + b 
                if token == '-':
                    result = a - b
                if token == '*':
                    result = a * b
                if token == '/':
                    result = a / b
                
                stack.append(result)
        return int(stack[-1])