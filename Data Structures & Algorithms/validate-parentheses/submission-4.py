class Solution:
    def isValid(self, s: str) -> bool:
        bracket_hash = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []

        for char in s:
            if char in bracket_hash:
                if stack and stack[-1] == bracket_hash[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False