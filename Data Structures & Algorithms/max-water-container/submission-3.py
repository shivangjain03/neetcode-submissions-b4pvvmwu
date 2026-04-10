class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area of water = min(heights[start],heights[end])*(end-start)
        # Can't sort
        start = 0
        area = 0
        end = len(heights)-1
        while start < end:
            a = min(heights[start], heights[end])*(end-start)
            area = max(a,area)

            if heights[start]>heights[end]:
                end-=1
            else:
                start+=1
        
        return area

        