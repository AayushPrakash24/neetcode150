"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # bfs approach
        # TC: O(n) SC: O(n)

        if not node:
            return None

        nodes = {node.val: Node(node.val)}

        queue = deque()
        visited = set()
        queue.append(node)
        visited.add(node)

        while queue:
            curr = queue.popleft()

            if curr.val not in nodes:
                nodes[curr.val] = Node(curr.val)

            for neighbor in curr.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)

                nodes[curr.val].neighbors.append(nodes[neighbor.val])

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return nodes[node.val]
            


        

