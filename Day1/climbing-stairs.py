class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursion with memoization (both approaches are worth learning here)
        # TC: O(n) SC: O(n)

        # handle base cases
        memo = {0:1, 1:1}

        # recursion with memoization (saves on redundant computations) -- memo hashmap acts like a "cache"
        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = dfs(i-1) + dfs(i-2)
            return memo[i]

        return dfs(n)

        # Iterative (dynamic programming)
        # TC: O(n) SC: O(n) -- can reduce SC to O(1) with this

        # dp array represents solutions for step i
        dp = [0] * (n+1)

        # base cases (step 0 and step 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            # recursive relationship, step i equals the sum of the previous two
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

