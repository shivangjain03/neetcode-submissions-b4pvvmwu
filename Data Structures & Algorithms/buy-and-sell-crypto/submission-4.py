class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # Brute force
        """for i in range(len(prices)):
            for j in range(i,len(prices)):
                max_profit =  max(max_profit, prices[j]-prices[i])
        
        return max_profit"""

        #Two pointer

        l = 0
        r = 1
        res = 0
        if len(prices)==0:
            return 0
        while l<r and r<len(prices):
            if prices[r]>prices[l]:
                res = max(res, prices[r]-prices[l])
                r+=1
            elif prices[r]<prices[l]:
                l = r
                r+=1
            else:
                r+=1
        return res