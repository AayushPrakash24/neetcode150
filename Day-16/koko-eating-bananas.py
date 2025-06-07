from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # optimize function with binary search
        l,r = 1, max(piles)

        def valid(k):
            hrs = 0

            for pile in piles:
                hrs += ceil(pile / k)
            
            return hrs <= h
        
        ret = r

        while l<=r:
            m = l + (r-l)//2
            if valid(m):
                r = m - 1
                ret = m
            else:
                l = m + 1
        
        return ret
        
            




        