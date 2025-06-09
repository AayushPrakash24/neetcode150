class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        line = []

        for start,end in intervals:
            line.append((start,1))
            line.append((end,-1))

        line.sort(key = lambda x:(x[0], x[1]))

        free = 0
        for time, attendance in line:
            free += attendance
            if free > 1:
                return False

        return True

            