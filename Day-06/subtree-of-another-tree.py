# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # stacked dfs (basically like two for loops)
        # TC: O(m*n) SC: O(m+n) | m = |subRoot| & n = |root|

        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            left = check(node1.left, node2.left)
            right = check(node1.right, node2.right)

            return node1.val == node2.val and left and right


        def dfs(node):
            if not node:
                return False
            
            if check(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
                

        