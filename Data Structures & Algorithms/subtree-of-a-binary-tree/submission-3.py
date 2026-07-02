# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfsIsSame(p, q):
            if not p and not q: return True
            if p and q and p.val == q.val:
                return dfsIsSame(p.left, q.left) and dfsIsSame(p.right, q.right)
                return True
            return False

        def dfs(node):
            if not node: return
            if node.val == subRoot.val and dfsIsSame(node, subRoot): return True
            return dfs(node.left) or dfs(node.right)
        if dfs(root): return True
        else: return False
