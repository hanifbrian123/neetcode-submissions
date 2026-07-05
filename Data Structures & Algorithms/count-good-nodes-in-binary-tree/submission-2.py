# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxV):
            nonlocal res
            if not node: return
            if node.val >= maxV: res += 1
            dfs(node.left, max(maxV, node.val))
            dfs(node.right, max(maxV, node.val))
        dfs(root, float('-inf'))
        return res
