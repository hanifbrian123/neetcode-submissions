# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque() # may only append and popleft
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)

                node.left, node.right = node.right, node.left
        return root

        