class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        #nums[i] + nums[j] + nums[k] == 0
        #nums[i] == - nums[j] - nums[k]
        #-nums[i] == nums[j] + nums[k]
        #nums = [-1,-1,0,1,2,-4]
        answers = set()

        for i in range(len(s_nums)):
            k = len(s_nums)-1
            j = 0
            
            while j != k:
                if i == j or i == k or j == k:
                    j += 1
                elif s_nums[i] * -1 > s_nums[j] + s_nums[k]:
                    j += 1
                elif s_nums[i] * -1 < s_nums[j] + s_nums[k]:
                    k -= 1
                elif s_nums[i] * -1 == s_nums[j] + s_nums[k]:
                    answers.add(tuple(sorted([s_nums[i],s_nums[j],s_nums[k]])))
                    k -= 1
        return list(answers)
