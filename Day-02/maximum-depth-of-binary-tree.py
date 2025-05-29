# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs solution
        # TC: O(n) SC: O(n) -- assuming unbalanced tree

        def dfs(node):
            if not node:
                return 0
            
            return 1 + max(dfs(node.left), dfs(node.right))
        
        return dfs(root)

        # bfs solution
        # TC: O(n) SC: O(n)
        if not root:
            return 0
            
        queue = deque()
        queue.append(root)
        level = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level
