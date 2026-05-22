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
                if not stack or stack.pop() != bracket_hash[char]:
                    return False
            else:
                stack.append(char) 
        return not stack


