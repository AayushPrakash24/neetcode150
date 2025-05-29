import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:    
        # heap solution 
        # TC: O(nlog(n)) SC: O(n)

        # use negative numbers to make it a max heap (heapq is default minheap)
        heap = [-i for i in stones]
        # heapq.heapify turns an array into a heap in O(n) time
        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, x-y)
        
        if not heap:
            return 0
        return -heap[0]




        