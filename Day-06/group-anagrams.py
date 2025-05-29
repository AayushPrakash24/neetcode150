from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # place in buckets based on letter frequency
        # TC: O(n*k) SC: O(n*k) | n = len(words) and k = max(len(word))

        groups = defaultdict(list)

        for word in strs:
            freq = [0] * 26

            for c in word:
                freq[ord(c)-ord('a')] += 1
            groups[tuple(freq)].append(word)
        
        ret = []

        for key, value in groups.items():
            ret.append(value)
        
        return ret
        
            

        