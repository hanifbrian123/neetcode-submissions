# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sumVal = l1.val + l2.val
        simpan = 1 if sumVal>9 else 0
        res = ListNode(sumVal % 10)

        currRes = res
        
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            sumVal = l1.val + l2.val + simpan
            simpan = 1 if sumVal>9 else 0
            new = ListNode(sumVal % 10)
            currRes.next = new
            currRes = currRes.next
            l1 = l1.next
            l2 = l2.next
        
        toBeSpent = None
        if l1: toBeSpent = l1
        elif l2: toBeSpent = l2

        while toBeSpent:
            sumVal = toBeSpent.val + simpan
            simpan = 1 if sumVal>9 else 0
            new = ListNode(sumVal % 10)
            currRes.next = new
            currRes = currRes.next
            toBeSpent = toBeSpent.next
        if simpan: currRes.next = ListNode(1)
        return res
