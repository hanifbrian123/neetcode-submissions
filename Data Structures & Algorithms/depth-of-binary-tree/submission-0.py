# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = [0]
        def dfs(node, depth):
            if not node: return None
            depth += 1
            maxDepth[0] = max(maxDepth[0], depth)
            dfs(node.left, depth)
            dfs(node.right, depth)
        dfs(root, 0)
        return maxDepth[0]