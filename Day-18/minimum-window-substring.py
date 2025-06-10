class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        freq = {}

        for c in t:
            freq[c] = freq.get(c,0)+1
        
        curr = {}
        have, need = 0, len(freq)
        ret = [-1,-1]
        best_len = float('inf')
        l = 0

        for r in range(n):
            if s[r] in freq:
                curr[s[r]] = curr.get(s[r],0)+1
                if curr[s[r]] == freq[s[r]]:
                    have += 1

            while have == need:
                if (r-l+1) < best_len:
                    ret = [l,r]
                    best_len = r-l+1
                if s[l] in curr:
                    curr[s[l]] -= 1
                    if curr[s[l]] < freq[s[l]]:
                        have -= 1
                l += 1
        if ret == [-1,-1]:
            return ""
        l,r = ret
        return s[l:r+1]


            

            






        