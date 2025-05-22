# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs solution
        # TC: O(n) SC: O(h) -> O(n)

        ret = [True]
        def dfs(node):
            if not node:
                return 0
            
            left, right = dfs(node.left), dfs(node.right)
            if abs(left-right) > 1:
                ret[0] = False
                return
            
            return 1 + max(left,right)
        
        dfs(root)
        return ret[0]