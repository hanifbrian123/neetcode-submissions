# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = [0]
        def dfs(node):
            if not node: return 0

            maxL = dfs(node.left)
            maxR = dfs(node.right)
            maxD[0] = max(maxD[0], (maxL + maxR))

            return 1 + max(maxL, maxR)
        dfs(root)
        return maxD[0]