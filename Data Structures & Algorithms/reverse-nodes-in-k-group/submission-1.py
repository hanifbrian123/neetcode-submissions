# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        dummy = ListNode(0)
        prev = dummy
        curr = head
        idxCurr = 1
        endA = dummy
        while curr:
            print()
            print(f"idxc: {idxCurr} - currv: {curr.val} - prev: {prev.val}")
            if idxCurr % k == 1:
                ptrCek = curr
                cnt = 0
                startB = None
                while ptrCek and cnt < k:
                    cnt += 1
                    startB = ptrCek
                    ptrCek = ptrCek.next
                print(startB.val, cnt)
                if cnt == k:
                    print("IF cnt == k")
                    temp = curr.next
                    print(f"temp: {temp.val}")
                    curr.next = startB.next
                    print(f"startb.nxt: {startB.next}")
                    endA.next = startB
                    endA = curr
                    prev = curr
                    curr = temp
                    print("ENDIF cnt == k")
                else:
                    curr = None
            else:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            idxCurr += 1
        return dummy.next