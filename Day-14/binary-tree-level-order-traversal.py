# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # ret = []
        # def dfs(node,level):
        #     if not node:
        #         return 
            
        #     dfs(node.left,level+1)
        #     while len(ret) < level+1:
        #         ret.append([])
        #     ret[level].append(node.val)
            
        #     dfs(node.right,level+1)

        # dfs(root,0)
        # return ret

        queue = deque()
        queue.append(root)
        ret = []

        if not root:
            return []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                level.append(node.val)
            ret.append(level)
        return ret
        
                


