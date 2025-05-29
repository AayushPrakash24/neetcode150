from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap solution (no imports)
        # TC: O(n) SC: O(n)

        if len(s) != len(t):
            return False
        m1, m2 = {}, {}
        for c,v in zip(s,t):
            m1[c] = m1.get(c,0)+1
            m2[v] = m2.get(v,0)+1
        return m1 == m2
    
        # more elegant hashmap solution (needs the collections import)
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

        