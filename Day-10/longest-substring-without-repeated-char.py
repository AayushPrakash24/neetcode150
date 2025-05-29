from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window -- can use default hashmap instead of counter
        # TC: O(n) SC: O(n)
        counter = Counter()
        maximum = 0
        
        l = 0
        for r in range(len(s)):
            while counter[s[r]] != 0:
                counter[s[l]] -= 1
                l += 1
            counter[s[r]] += 1
            maximum = max(r-l+1, maximum)
        
        return maximum


