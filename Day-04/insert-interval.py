import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # place newInterval in the right spot (according to start) then merge intervals
        # TC: O(n) SC: O(n)

        ret = []

        bisect.insort(intervals, newInterval)

        for start, end in intervals:
            if ret and start <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], end)
            else:
                ret.append([start,end])
        
        return ret