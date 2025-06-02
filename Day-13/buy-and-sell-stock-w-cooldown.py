class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # memo = {}
        # def dfs(i, holding):
        #     if (i,holding) in memo:
        #         return memo[(i,holding)]
        #     if i >= n:
        #         return 0

        #     if not holding:
        #         buy = -prices[i] + dfs(i+1, True)
        #         wait = dfs(i+1, False)
        #         memo[(i,holding)] = max(buy,wait)
        #     else:
        #         sell = prices[i] + dfs(i+2, False)
        #         wait = dfs(i+1, True)
        #         memo[(i,holding)] = max(sell,wait)
        #     return memo[(i,holding)]

        # return dfs(0,False)
        n = len(prices)
        dp = [[0 for _ in range(3)] for _ in range(n)] # states 0: holding 1: sell 2: rest

        dp[0][0] = -prices[0]

        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = prices[i] + dp[i-1][0]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        
        return max(dp[n-1][1], dp[n-1][2])




