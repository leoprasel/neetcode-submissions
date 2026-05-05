class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False
