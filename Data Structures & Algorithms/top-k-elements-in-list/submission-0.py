class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_group = {} #value -> count
        for num in nums:
            if num not in nums_group:
                nums_group[num] = 1
            else:    
                nums_group[num] = nums_group[num] + 1
        
        sorted_nums_group = dict(sorted(nums_group.items(), key=lambda item: item[1], reverse=True)[:k])

        return list(sorted_nums_group.keys())