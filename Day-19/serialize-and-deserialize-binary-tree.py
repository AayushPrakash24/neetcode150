# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque()
        queue.append(root)
        build = []

        while queue:
            curr = queue.popleft()
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
                build.append(str(curr.val))
            else:
                build.append("n")

        print(build)
        return ','.join(build)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == 'n':
            return None
        
        build = data.split(',')
        n = len(build)
        queue = deque()
        root = TreeNode(int(build[0]))
        queue.append(root)
        i = 1
        while queue and i < n:
            node = queue.popleft()

            if build[i] != 'n':
                left_node = TreeNode(int(build[i]))
                node.left = left_node
                queue.append(left_node)
            
            i += 1

            if i >= n:
                break

            if build[i] != 'n':
                right_node = TreeNode(int(build[i]))
                node.right = right_node
                queue.append(right_node)

            i += 1
            
        return root




        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))