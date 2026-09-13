class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                if nums[l] < nums[mid]:
                    # left half sorted, and target > nums[mid] (its max) -> can't be there
                    l = mid + 1
                elif nums[r] < target:
                    # right half sorted, target > nums[r] (its max) -> can't be there
                    r = mid - 1
                else:
                    # right half sorted, target <= nums[r] -> it's in there
                    l = mid + 1

            else:
                if nums[mid] < nums[r]:
                    # right half sorted, and target < nums[mid] (its min) -> can't be there
                    r = mid - 1
                elif nums[l] > target:
                    # left half sorted, target < nums[l] (its min) -> can't be there
                    l = mid + 1
                else:
                    # left half sorted, target >= nums[l] -> it's in there
                    r = mid - 1

        return -1