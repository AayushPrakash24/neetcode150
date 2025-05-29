import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # max heap
        # TC: O(nlogn) SC: O(n)

        def compute_distance(x,y):
            return math.sqrt(x**2 + y**2)
        
        heap = []

        for x,y in points:
            dist = compute_distance(x,y)
            if heap and len(heap) >= k:
                if heap[0][0] < -dist:
                    heapq.heappushpop(heap, (-dist, [x,y]))
            else:
                heapq.heappush(heap, (-dist, [x,y]))

        ret = []
        
        for _, point in heap:
            ret.append(point)

        return ret
    

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # scuffed binary search solution
        # TC: O(n) amortized -- wc O(n^2) SC: O(n)
        
        def compute_dist(x,y):
            return x**2+y**2
        
        def split_dist(remaining, dist, m):
            l_segment, r_segment = [], []

            for i in remaining:
                if dist[i] > m:
                    r_segment.append(i)
                else:
                    l_segment.append(i)
            
            return [l_segment, r_segment]

        dist = [compute_dist(x,y) for x,y in points]

        l,r = 0, max(dist)
        remaining = [i for i in range(len(points))]

        closestPoints = []

        while k:
            m = l + (r-l)/2

            l_segment, r_segment = split_dist(remaining, dist, m)
                
            if len(l_segment) > k:
                remaining = l_segment
                r = m
            else:
                k -= len(l_segment)
                closestPoints.extend(l_segment)
                remaining = r_segment
                l = m
        
        return [points[i] for i in closestPoints]
        

        
            
            

                
        





        