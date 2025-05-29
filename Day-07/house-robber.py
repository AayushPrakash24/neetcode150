class Solution:
    def rob(self, nums: List[int]) -> int:
        # recursion with memo
        # TC: O(n) SC: O(n)
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]

        return dfs(0)
        

class Solution:
    def rob(self, nums: List[int]) -> int:
        # iterative bottom up dp
        # TC: O(n) SC: O(n)

        n = len(nums)

        dp = [0] * (n)

        if len(nums) <= 2:
            return max(nums)
        
        for i in range(n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]

        