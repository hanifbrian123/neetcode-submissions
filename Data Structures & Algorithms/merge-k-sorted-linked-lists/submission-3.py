# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while True:
            isThere = False
            minNode = ListNode(float('inf'))
            minNodeIdx = -1
            for i in range(len(lists)):
                l = lists[i]
                if l: 
                    isThere = True
                    if l.val < minNode.val:
                        minNode = l
                        minNodeIdx = i
            if not isThere:
                break
            lists[minNodeIdx] = minNode.next
            curr.next = minNode
            curr = minNode
        return dummy.next


