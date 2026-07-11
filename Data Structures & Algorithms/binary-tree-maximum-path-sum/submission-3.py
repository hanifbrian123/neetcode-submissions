# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def dfs(node):
            nonlocal maxSum
            if not node: return 0
            
            maxL = node.val + dfs(node.left)
            maxR = node.val + dfs(node.right)

            maxSum = max(maxSum, maxL+maxR-node.val, node.val, maxR, maxL)

            return max(maxL, maxR, node.val)
        dfs(root)
        return maxSum
            

