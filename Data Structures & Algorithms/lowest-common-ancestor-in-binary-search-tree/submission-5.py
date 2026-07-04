# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return {p.val:0, q.val:0}
            mpLeft = dfs(node.left)
            mpRight = dfs(node.right)

            if type(mpLeft) is list: return mpLeft
            elif type(mpRight) is list: return mpRight

            # mid
            mpMid = {p.val: 0, q.val: 0}
            if node.val in mpMid:
                mpMid[node.val] += 1

            # merge
            mpMerged = {p.val: 0, q.val: 0}
            mpMerged[p.val] = mpLeft[p.val] + mpRight[p.val] + mpMid[p.val]
            mpMerged[q.val] = mpLeft[q.val] + mpRight[q.val] + mpMid[q.val]

            if mpMerged[p.val] and mpMerged[q.val]:
                return [node, True]
            
            return mpMerged
        return dfs(root)[0]
