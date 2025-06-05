import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ret = [float('inf')] * n
        adj = defaultdict(list)

        for src, dst, weight in times:
            adj[src].append([dst,weight])
        
        queue = []
        queue.append((0,k))
        
        while queue:
            time, node = heapq.heappop(queue)
            if ret[node-1] != float('inf'):
                continue
                
            ret[node-1] = time

            for neighbor, weight in adj[node]:
                if ret[neighbor-1] == float('inf'):
                    heapq.heappush(queue,(time+weight, neighbor))
        
        if float('inf') in ret:
            return -1
        return max(ret)
            

                
        

        

