# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_a_to_idx = {inorder[i]: i for i in range(len(inorder))}
        def dfs(node, a, b):
            nonlocal idx
            
            if a>=b: return
            if idx>len(preorder)-1: return 

            mid = inorder_a_to_idx[node.val]
            if a < mid:
                idx += 1
                newNode = TreeNode(preorder[idx])
                node.left = newNode
                dfs(newNode, a, mid-1)
            if b > mid:
                idx += 1
                newNode = TreeNode(preorder[idx])
                node.right = newNode
                dfs(newNode, mid+1, b)

            
        idx = 0
        root = TreeNode(preorder[0])
        dfs(root, 0, len(preorder)-1)
        return root

        