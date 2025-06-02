class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # first approach (failed by tle)
        # n = len(nums)

        # def backtrack(subset1, subset2, i):
        #     if i >= n:
        #         return subset1 == subset2
            
        #     memo[(subset1,subset2,i)] = backtrack(subset1+nums[i],subset2,i+1) or backtrack(subset1,subset2+nums[i],i+1)
        #     return memo[(subset1,subset2,i)]
        
        # return backtrack(0,0,0)
        
        # knapsack approach top down
        # n = len(nums)
        # s = sum(nums)
        # if s % 2 != 0:
        #     return False
        
        # target = s // 2
        # memo = {}
        # def dfs(i,curr):
        #     if (i,curr) in memo:
        #         return memo[(i,curr)]
        #     if i >= n:
        #         return curr == target
        #     elif curr > target:
        #         return False
            
        #     memo[(i,curr)] = dfs(i+1, curr+nums[i]) or dfs(i+1, curr)
        #     return memo[(i,curr)]
        
        # return dfs(0,0)

        #bottom up
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target = s // 2

        dp = [[False for _ in range(target+1)] for _ in range(n+1)]

        dp[0][0] = True

        for i in range(1,n+1):
            num = nums[i-1]
            for j in range(target+1):
                if j < num:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
        
        return dp[n][target]
            



            


            