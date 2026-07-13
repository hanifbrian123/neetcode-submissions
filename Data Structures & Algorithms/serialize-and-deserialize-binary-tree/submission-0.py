# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        q = deque() # may only append and popleft
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res += str(node.val) + "#"
            else:
                res += "None#"
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split('#')
        data.pop()
        data = deque(data)
        print(data)

        q = deque() # a queue actually
        rootVal = data.popleft()
        if rootVal == 'None': return None
        
        root = TreeNode(int(rootVal))
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                leftVal = data.popleft()
                rightVal = data.popleft()
                leftNode = TreeNode(int(leftVal)) if leftVal != 'None' else None
                rightNode = TreeNode(int(rightVal)) if rightVal != 'None' else None

                node.left = leftNode
                node.right = rightNode

                q.append(leftNode)
                q.append(rightNode)
        return root