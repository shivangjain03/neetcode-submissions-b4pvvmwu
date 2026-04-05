class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area = l*b
        # l = height of integer i in array heights
        # b = number of bars in between + 1
        num_bars = 0
        area = 0
        l = 0
        r = len(heights)-1
        while l<r:
            b = r-l
            h = min(heights[l],heights[r])
            print(b)
            print(h)
            temp_area = b*h
            if temp_area>area:
                area = temp_area
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1


        
        return area