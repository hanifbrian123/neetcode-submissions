# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        prevNode = list1
        nextNode = list2
        head = list1
        if list2.val <= list1.val:
            prevNode = list2
            nextNode = list1
            head = list2

        temp = prevNode.next
        prevNode.next = nextNode
        currBottom = temp

        while nextNode and currBottom:
            if currBottom.val <= nextNode.val:
                prevNode.next = currBottom
                temp = currBottom.next
                currBottom.next = nextNode
                prevNode = currBottom
                currBottom = temp
            else:
                prevNode = nextNode
                nextNode = nextNode.next

        if not nextNode:
            prevNode.next = currBottom
            
        return head
