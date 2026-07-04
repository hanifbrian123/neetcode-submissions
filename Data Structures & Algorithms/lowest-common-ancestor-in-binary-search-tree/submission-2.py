# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def formatMpNode(self, mp):
        return mp
        return {key.val: mp[key] for key in mp}
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # print(f"{p}: {p.val} | {q}: {q.val}")
        # print(f"{p.left} | {q.left}")
        def dfs(node):
            if not node: return {p.val:0, q.val:0}
            # print("n val: ", node.val)
            mpLeft = dfs(node.left)
            mpRight = dfs(node.right)

            # print(f"n val: {node.val} | mpL: {self.formatMpNode(mpLeft)} | mpR: {self.formatMpNode(mpRight)}")
            if type(mpLeft) is list: return mpLeft
            elif type(mpRight) is list: return mpRight

            # mid
            mpMid = {p.val: 0, q.val: 0}
            # print(f"TEMP: {mpMid} | {node}")
            if node.val in mpMid:
                mpMid[node.val] += 1
            # print(f"mpMid: {self.formatMpNode(mpMid)}")

            # merge
            mpMerged = {p.val: 0, q.val: 0}
            mpMerged[p.val] = mpLeft[p.val] + mpRight[p.val] + mpMid[p.val]
            mpMerged[q.val] = mpLeft[q.val] + mpRight[q.val] + mpMid[q.val]
            # print(f"mpMerged: {self.formatMpNode(mpMerged)}")
            # print()

            if mpMerged[p.val] and mpMerged[q.val]:
                # print("kenaaa")
                return [node, True]
            
            return mpMerged
        # print(dfs(root))
        return dfs(root)[0]
