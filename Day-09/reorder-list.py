# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find midpoint, reverse rhs and merge
        # TC: O(n) SC: O(1)

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow
        prev = None

        while curr:
            # temp = curr.next
            # curr.next = prev
            # prev = curr
            # curr = temp
            curr.next, prev, curr = prev, curr, curr.next
        
        n1, n2 = head, prev

        while n2.next:
            # temp = n1.next
            # n1.next = n2
            # n1 = temp

            # temp = n2.next
            # n2.next = n1
            # n2 = temp

            n1.next, n1 = n2, n1.next
            n2.next, n2 = n1, n2.next
        
        
        
        

        
            

        
        