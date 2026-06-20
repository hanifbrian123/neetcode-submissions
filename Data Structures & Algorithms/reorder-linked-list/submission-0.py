# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        mid = (length + 1) // 2
        
        curr = head
        for i in range(1, mid):
            curr = curr.next
        temp = curr.next
        curr.next = None
        curr = temp
        
        # reverse
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print()
        # while prev:
        #     print(prev.val)
        #     prev = prev.next
        

        curr = head
        while curr and prev:
            temp1 = curr.next
            curr.next = prev
            curr = temp1

            temp2 = prev.next
            prev.next = curr
            prev = temp2


