class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque([])
        i = 0
        while i < k:
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            i += 1
        res = [q[0]]

        if q[0] == nums[0]:
            q.popleft()
        
        l = 1
        for r in range(k, len(nums)):
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])

            res.append(q[0])
            l += 1
        return res