class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting 
        # TC: O(nlogn) # SC: O(n)
        intervals.sort(key=lambda x: x[0])

        ret = []

        for interval in intervals:
            if ret and ret[-1][1] >= interval[0]:
                ret[-1][1] = max(ret[-1][1],interval[1])
            else:
                ret.append(interval)
        
        return ret
            