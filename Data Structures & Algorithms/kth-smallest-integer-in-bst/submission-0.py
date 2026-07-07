# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = 0
        def dfs(node):
            nonlocal idx
            if not node: return
            
            res = dfs(node.left)
            if res is not None: return res

            idx += 1
            if idx == k: return node.val
            
            res = dfs(node.right)
            if res is not None: return res

            return
        return dfs(root)