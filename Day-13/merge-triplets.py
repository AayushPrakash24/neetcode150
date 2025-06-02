class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        usefulTriplets = []
        a,b,c = target
        for x,y,z in triplets:
            if x > a or y > b or z > c:
                continue
            usefulTriplets.append([x,y,z])
        
        fa,fb,fc = 0,0,0
        for x,y,z in usefulTriplets:
            fa = max(fa,x)
            fb = max(fb,y)
            fc = max(fc,z)
        
        return fa == a and fb == b and fc == c

            
            