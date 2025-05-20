import heapq
class KthLargest:
    # heap solution (requires heapq import which is by default a min-heap)
    # the methods to know are heapq.heappush(heap,val) and heapq.heappop(heap)
    # TC: O(nlog(n)) SC: O(k)

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap,val)
        else:
            heapq.heappush(self.heap, val)

        return self.heap[0]
    
    
import bisect
class KthLargest:
    # insort solution (can be done manually with binary search but is quicker with bisect import)
    # TC: O(nlog(n)) amortized -- WC is O(n^2 + m*n) SC: O(m+n)

    def __init__(self, k: int, nums: List[int]):
        self.sorted = nums
        self.sorted.sort()
        self.k = k

    def add(self, val: int) -> int:
        # this method does insertion sort pretty much
        bisect.insort(self.sorted, val)
        return self.sorted[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)