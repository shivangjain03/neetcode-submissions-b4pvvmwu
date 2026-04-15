"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        count = 0
        for i in range(len(intervals)):
            start.append(intervals[i].start)
        for i in range(len(intervals)):
            end.append(intervals[i].end)
        start.sort()
        end.sort()
        print(start)
        print(end)
        start_ptr = 0
        end_ptr = 0

        res = 0 

        while start_ptr<len(intervals):
            if start[start_ptr]<end[end_ptr]:
                start_ptr+=1
                count+=1
            else:
                count-=1
                end_ptr+=1
            res = max(res,count)
        return res
                


        