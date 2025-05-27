# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs solution 
        # TC: O(n) SC: O(n)
        def dfs(node):
            val = node.val
            
            if p.val < val and q.val < val:
                return dfs(node.left)
            elif p.val > val and q.val > val:
                return dfs(node.right)
            return node
        
        return dfs(root)


        # iterative solution
        # TC: O(n) SC: O(1)
        curr = root

        while curr:
            val = curr.val

            if p.val > val and q.val > val:
                curr = curr.right
            elif p.val < val and q.val < val:
                curr = curr.left
            else:
                return curr
         
        

            
            
        