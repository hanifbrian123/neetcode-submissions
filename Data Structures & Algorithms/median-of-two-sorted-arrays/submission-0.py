class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a
        totalLen = len(a) + len(b)
        half = totalLen//2
        l, r = 0, len(a)-1
        while True:
            i = (l+r) // 2
            j = half - i - 2
            
            aLeft = a[i] if i>=0 else float('-inf')
            aRight = a[i+1] if i+1 <= len(a)-1 else float('inf')
            bLeft = b[j] if j>=0 else float('-inf')
            bRight = b[j+1] if j+1 <= len(b)-1 else float('inf')
            
            print(aLeft, aRight)
            print(bLeft, bRight)
            
            if (aLeft<=bRight and bLeft<=aRight):
                if (totalLen % 2):
                    return min(aRight, bRight)
                return ( ( max(aLeft, bLeft) + min(aRight, bRight) ) / 2 )
            elif aLeft>bRight:
                r = i - 1
            else:
                l = i + 1
        