class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        nums.sort()
        for i in range(len(nums)):
            if i == len(nums) -1:
                return False
            if nums[i] == nums[i+1]:
                return True