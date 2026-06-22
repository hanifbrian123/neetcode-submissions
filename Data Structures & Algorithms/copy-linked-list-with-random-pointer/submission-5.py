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
        for i in range(len(MP_ori_new_idxRand)):
            ori_new_idxRand = MP_ori_new_idxRand[i]
            ori = ori_new_idxRand[0]
            new = ori_new_idxRand[1]
            idxRand = ori_new_idxRand[2]
            randForNew = MP_ori_new_idxRand[idxRand][1] if idxRand!=-1 else None

            new.next = MP_ori_new_idxRand[i+1][1] if i+1<len(MP_ori_new_idxRand) else None
            new.random = randForNew

        return MP_ori_new_idxRand[0][1]