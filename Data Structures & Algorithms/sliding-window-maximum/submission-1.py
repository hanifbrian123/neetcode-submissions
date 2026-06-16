class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # print(nums)
        deq = deque([nums[0]])
        # print(deq)
        # print()
        res = []
        for i in range(1, k): 
            # print(f"nums[i]: {nums[i]}")
            while deq and nums[i] > deq[-1]:
                deq.pop()
            deq.append(nums[i])
            # print(deq)
        res.append(deq[0])
        # print(f"res: {res}")
        l = 0
        
        # print()
        for r in range(k, len(nums)):
            # print(f"nums[r]: {nums[r]}")
            if deq[0] == nums[l]: deq.popleft()
            while deq and nums[r] > deq[-1]: 
                deq.pop()
            deq.append(nums[r])
            # print(deq)
            res.append(deq[0])
            # print(f"res: {res}")
            # print()
            l+=1
        return res
