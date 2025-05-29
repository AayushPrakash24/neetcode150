class Solution:
    def hammingWeight(self, n: int) -> int: 
        # bit manipulation
        # TC: O(1) SC: O(1)
        
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        
        return count
        
            
        