# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive solution (depth first search)
        # TC: O(n) SC: O(h) -> O(n)
        def dfs(node):
            if not node:
                return None
            
            node.left, node.right = dfs(node.right), dfs(node.left)

            return node
        
        return dfs(root)

        # Iterative solution (breadth first search)
        # TC: O(n) SC: O(n)
        if not root:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
        
