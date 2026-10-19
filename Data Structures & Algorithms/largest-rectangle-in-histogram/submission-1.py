class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair (index, height)
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                start = idx
                maxArea = max(maxArea, (i - idx) * height)
            stack.append((start, h))
        
        n = len(heights)
        for i, h in stack:
            maxArea = max(maxArea, (n - i) * h)
        return maxArea