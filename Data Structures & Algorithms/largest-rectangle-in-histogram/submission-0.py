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
        for s in stack:
            i, h = s
            maxArea = max(maxArea, (n - i) * h)
        return maxArea


"""
7  1  1  2  2  4


(0, 1), (2, 1), (3, 2), (4, 2), (5, 4)


ma = 7


1, 2, 3, 4, 3, 1, 6, 5, 1

1, 1, 1
2, 3, 9, 3, 2

(0, 1), 5, 

"""