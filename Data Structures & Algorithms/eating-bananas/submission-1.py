class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Speed 
        low = 1
        high = max(piles)
        result = high
        while low <= high:
            mid = (low+high)//2
            time = 0
            for i in piles:
                time+=math.ceil(float(i)/mid)
            if time <=h:
                result = mid
                high = mid - 1
            else:
                low = mid+1
        return result
                
                
                
            
            
        
        