class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dynamic programming
        # TC: O(n^2) SC: O(n^2)
        n = len(s)
        
        dp = [[False for _ in range(n)] for _ in range(n)]

        longest = [0,0]

        # base case (single character)
        for i in range(n):
            dp[i][i] = True
        # base case (two adjacent characters)
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                longest = [i, i+1]
        # iterate through length wise -- (so we can check whether the previous window is a valid solution or not -- indicated by dp[i+1][j-1])
        for length in range(2,n):
            for i in range(n-length):
                j = i+length
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    longest = [i,j]

        return s[longest[0]: longest[1]+1]