import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap
        # TC: O(nlogn) SC: O(k)
        
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
            