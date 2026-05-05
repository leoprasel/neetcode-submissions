class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum_area = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i == j:
                    continue
                min_value = min(heights[i],heights[j])
                area = min_value * abs(i-j)
                if area > maximum_area:
                    maximum_area = area
        return maximum_area