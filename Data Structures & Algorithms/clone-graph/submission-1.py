"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = collections.deque([node])
        visited = {node}
        
        rootC = Node(node.val)
        qC = collections.deque([rootC])

        oriToC = {node:rootC}
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                nodeC = qC.popleft()
                for nei in node.neighbors:
                    if nei not in visited:
                        neiC = Node(nei.val)
                        nodeC.neighbors.append(neiC)
                        qC.append(neiC)
                        oriToC[nei] = neiC

                        visited.add(nei)
                        q.append(nei)
                    else:
                        nodeC.neighbors.append(oriToC[nei])
        return rootC

