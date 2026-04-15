class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        result = []
        #Left
        # [1,3], [5,6] ([5,6] is the new interval)
        while index < len(intervals) and intervals[index][1]<newInterval[0]:
            result.append(intervals[index])
            index+=1
        
        #Merge
        while index<len(intervals) and  intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index+=1
        result.append(newInterval)
        


        #Right
        # [1,3] is the new interval
        # [1,3], [5,6]
        while index<len(intervals) and intervals[index][0] > newInterval[1]:
            result.append(intervals[index])
            index+=1
        
        return result

        
        

        