class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy algo
        # TC: O(n) SC: O(1)
        maxJump = 0

        for i in range(len(nums)):
            if maxJump < i:
                return False

            maxJump = max(maxJump, i+nums[i])
        
        return True
    

        

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dynamic programming
        # TC: O(n^2) SC: O(n)
        n = len(nums)

        dp = [False] * n
        dp[0] = True
        
        for i in range(n):
            if dp[i]:
                for j in range(i+1,min(i+nums[i]+1,n)):
                    dp[j] = True
        
        return dp[-1]


                

                
            

                