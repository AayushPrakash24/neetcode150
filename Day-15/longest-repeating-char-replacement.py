class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # binary search over solution space
        n = len(s)

        def bs(l,r):
            ret = 0
            while l <= r:
                m = l + (r-l)//2

                if valid(m):
                    l = m+1
                    ret = m
                else:
                    r = m-1
            
            return ret
        
        def valid(length):
            l = 0
            freq = Counter()
            maxFreq = 0

            for r in range(n):
                freq[s[r]] += 1

                if r-l+1 > length:
                    freq[s[l]] -= 1
                    l += 1
                
                maxFreq = max(maxFreq, freq[s[r]])

                if length - maxFreq <= k:
                    return True
                
            return False
        
        return bs(1,n)



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        freq = Counter()
        maxFreq = longest = 0

        for r in range(n):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])

            while r-l+1 > maxFreq + k:
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        
        return longest
 
