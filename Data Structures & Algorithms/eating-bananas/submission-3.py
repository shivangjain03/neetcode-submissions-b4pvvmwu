class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force (O(m*n))
        """speed = 1 
        while True:
            totalTime = 0
            for pile in piles:
                totalTime+=math.ceil(pile/speed)
            
            if totalTime <= h:
                return speed
            
            speed+=1
        
        return speed"""


        low = 1
        high = max(piles)
        total_time_list = []


        while low<=high:
            total_time = 0
            mid = (low+high)//2
            for i in piles:
                total_time+=math.ceil(i/mid)

            if total_time > h:
                low = mid+1
            
            elif total_time <= h:
                total_time_list.append(mid)
                high = mid-1
            
        return min(total_time_list)
            
            

             




        