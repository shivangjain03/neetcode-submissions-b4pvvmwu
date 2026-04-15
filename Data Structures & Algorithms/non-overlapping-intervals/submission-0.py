class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=result[-1][-1]:
                result.append(intervals[i])
                print(intervals[i])
            elif intervals[i][0]<result[-1][-1]:
                print("Hitting here")
                result[-1][-1] = min(intervals[i][1], result[-1][-1])
                
        return len(intervals) - len(result)

        