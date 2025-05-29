# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs solution -- bfs solution not worth here (annoying)
        # TC: O(n) SC: O(h) -> O(n) 

        # this is one way of doing global variables in python -- another way is by using self.maximum = 0
        maximum = [0]

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            # we can store global variables like this *using a list rather than normal int
            maximum[0] = max(maximum[0], left + right)

            return 1 + max(left,right)
        
        dfs(root)

        return maximum[0]
