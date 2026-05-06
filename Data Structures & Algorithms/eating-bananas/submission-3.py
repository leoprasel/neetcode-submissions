class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #binary search on k possibilities
        import math
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right)//2 #k

            hours = sum(math.ceil(p/mid) for p in piles)
            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
