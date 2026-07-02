# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p is None and q is None: return True
            if p and q and p.val==q.val: 
                resLeft = dfs(p.left, q.left)
                resRight = dfs(p.right, q.right)
                if not resLeft or not resRight:
                    return False

                return True
            
            return False
        return dfs(p, q)