"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # data awal head
        # curr = head
        # while curr:
        #     print(f"{curr} ({curr.val}) ({curr.random.val if curr.random else None})")
        #     curr = curr.next
        # print()

        if not head:
            return None

        # mapping node -> idx
        curr = head
        idx = 0
        nodeToIdx = {None: -1}
        while curr:
            nodeToIdx[curr] = idx
            idx+=1
            curr = curr.next
        
        # mapping ori, new node, idx rand
        MP_ori_new_idxRand = []
        curr = head
        while curr:
            idxRand = nodeToIdx[curr.random] if curr.random else -1
            MP_ori_new_idxRand.append([curr, Node(curr.val), idxRand])
            curr = curr.next
        
        
        # create a copy
        for i in range(len(MP_ori_new_idxRand)-1):
            ori_new_idxRand = MP_ori_new_idxRand[i]
            ori = ori_new_idxRand[0]
            new = ori_new_idxRand[1]
            idxRand = ori_new_idxRand[2]
            randForNew = MP_ori_new_idxRand[idxRand][1] if idxRand!=-1 else None

            new.next = MP_ori_new_idxRand[i+1][1]
            new.random = randForNew
        new = MP_ori_new_idxRand[-1][1]
        new.next = None
        new.random = MP_ori_new_idxRand[MP_ori_new_idxRand[-1][2]][1] if MP_ori_new_idxRand[-1][2]!=-1 else None

        return MP_ori_new_idxRand[0][1]



        # headNew = MP_ori_new_idxRand[0][1]
        # curr = headNew
        # for i in range(len(MP_ori_new_idxRand)-1):
        #     ori_new_idxRand = MP_ori_new_idxRand[i]
        #     ori = ori_new_idxRand[0]
        #     new = ori_new_idxRand[1]
        #     idxRand = ori_new_idxRand[2]
        #     randForNew = MP_ori_new_idxRand[idxRand][1] if idxRand!=-1 else None

        #     curr.next = MP_ori_new_idxRand[i+1][1]
        #     curr.random = randForNew
        #     curr = curr.next
        # curr.next = None
        # curr.random = MP_ori_new_idxRand[MP_ori_new_idxRand[-1][2]][1]

        # return headNew