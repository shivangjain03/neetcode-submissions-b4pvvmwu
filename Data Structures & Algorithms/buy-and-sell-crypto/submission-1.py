class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1
        while l<r and r<len(prices):
            if prices[l]<prices[r]:
                temp_profit = prices[r]-prices[l]
                if temp_profit>profit:
                    profit = temp_profit
                r+=1
            else:
                l = r
                r+=1
        return profit
            

        