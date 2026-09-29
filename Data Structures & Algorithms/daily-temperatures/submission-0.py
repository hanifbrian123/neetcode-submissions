class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (idx, t)
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idxStack, tStack = stack.pop()
                res[idxStack] = i - idxStack
            stack.append((i, t))
        return res