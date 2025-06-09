class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # memo = {}
        # def dfs(amount): 
        #     if amount in memo:
        #         return memo[amount]
        #     if amount == 0:
        #         return 0
        #     if amount < 0:
        #         return float('inf')
            
        #     ans = float('inf')
        #     for coin in coins:
        #         ans = min(ans, dfs(amount-coin)+1)
            
        #     memo[amount] = ans
        #     return memo[amount]
        
        # ans = dfs(amount)
        # if ans == float('inf'):
        #     return -1
        # return ans            
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]