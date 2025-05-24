from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap
        # TC: O(nlogk) SC: O(n+k)
        counter = Counter(nums)
        heap = []
        for key,value in counter.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (value, key))
            else:
                heapq.heappush(heap, (value, key))
        
        return [y for _,y in heap]