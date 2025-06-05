"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        clone = {head: Node(head.val)}

        curr = head
        
        while curr:

            if curr not in clone:
                clone[curr] = Node(curr.val)
            
            if curr.next:
                if curr.next not in clone:
                    clone[curr.next] = Node(curr.next.val)
                clone[curr].next = clone[curr.next]
                
            if curr.random:
                if curr.random not in clone:
                    clone[curr.random] = Node(curr.random.val)
            
                clone[curr].random = clone[curr.random]

            curr = curr.next
        
        return clone[head]

            
