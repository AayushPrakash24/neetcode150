class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n+1)]

        dp[0] = True

        for i in range(n):
            if dp[i]:
                for word in wordDict:
                    if len(word) < n-i+1 and s[i:i+len(word)] == word:
                        dp[i+len(word)] = True

        return dp[-1]
                        
        