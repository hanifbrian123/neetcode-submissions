# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def dfs(node):
            if not node: return 0
            maxL = dfs(node.left)
            maxR = dfs(node.right)
            print()
            print(node.val)
            print(abs(maxL - maxR))
            if abs(maxL - maxR) > 1: res[0] = False
            return 1 + max(maxL, maxR)
        dfs(root)
        return res[0]
