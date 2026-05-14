class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        seen = {}
        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            seen[c] = right
            best = max(best, right - left + 1)
        return best