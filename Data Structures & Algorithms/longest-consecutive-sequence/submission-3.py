class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        highest_answer = 0
        for num in nums:
            if num -1 not in nums_set:
                answer = 0
                while num + answer in nums_set:
                    answer += 1
                if answer > highest_answer:
                    highest_answer = answer
        return highest_answer