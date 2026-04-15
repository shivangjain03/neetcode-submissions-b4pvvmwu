"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        index = 1
        if len(intervals) == 0:
            return True
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i].start>=result[-1].end:
                result.append(intervals[i])
            elif intervals[i].start<result[-1].end:
                return False
        return True
