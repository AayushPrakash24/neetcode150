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
                        


class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, s):
        d = self.trie

        for c in s:
            if c not in d:
                d[c] = {}
            
            d = d[c]
        d['.'] = '.'
    
    def search(self,word):
        d = self.trie

        for c in word:
            if c not in d:
                return False
            d = d[c]
        
        return '.' in d
    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        root = Trie()
        max_len = 0
    
        for word in wordDict:
            root.insert(word)
            max_len = max(max_len, len(word))

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n):
            if dp[i]:
                curr = root
                
                for j in range(1, min(n-i,max_len)+1):
                    if curr.search(s[i:i+j]):
                        dp[i+j] = True
        return dp[n]