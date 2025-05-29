class Solution:
    def countBits(self, n: int) -> List[int]:
        # count each bit
        # TC: O(nlogn) SC: O(n)

        ans = []
        for i in range(n+1):
            n = i
            count = 0
            while n:
                if n & 1:
                    count += 1
                n = n >> 1
            ans.append(count)

        return ans
    
class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp solution
        # TC: O(n) SC: O(n)
        
        dp = [0] * (n+1)

        for i in range(n+1):
            dp[i] = dp[i>>1] + (i&1)

        return dp 

        
