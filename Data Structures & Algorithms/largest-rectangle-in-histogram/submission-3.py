class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ''' o(n^2)
        max_area = 0
        for i in range(len(heights)):
        
            right_width = 1
            while i + right_width < len(heights) and heights[i + right_width] >= heights[i]:
                right_width += 1

            left_width = 1
            while i - left_width >= 0 and heights[i - left_width] >= heights[i]:
                left_width += 1
            
            right_width -= 1
            left_width -= 1

            max_area = max(max_area,heights[i] * (left_width + right_width + 1))
        return max_area
    '''
        n = len(heights)
        
        stack = [] 
        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        maxArea = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
        return maxArea
        