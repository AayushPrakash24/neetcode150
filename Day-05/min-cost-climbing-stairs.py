class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top down dynamic programming (dp) -- recursion with memoization
        # TC: O(n) SC: O(n)
        memo = {}
        def dfs(i):
            # base case
            if i <= 1:
                return 0  

            # caching 
            if i in memo:
                return memo[i]

            # recursive relation
            memo[i] = min(dfs(i-1) + cost[i-1], dfs(i-2) + cost[i-2])
            return memo[i]

        return dfs(len(cost))
    


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up dynamic programming
        # TC: O(n) SC: O(n)
        n = len(cost)
        dp = [0] * (n+1)

        
        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[n]

        
