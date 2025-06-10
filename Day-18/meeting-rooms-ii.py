class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        line = []

        for start, end in intervals:
            line.append((start,1))
            line.append((end,-1))

        line.sort(key = lambda x: (x[0],x[1]))
        curr,rooms = 0,0


        for time, div in line:
            curr += div
            rooms = max(rooms,curr)
        
        return rooms

            

