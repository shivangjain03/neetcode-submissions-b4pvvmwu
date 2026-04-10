class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Profit can never be neg in this case
        profit = 0
        if len(prices) == 0:
            return 0
        start = 0
        end = 1
        while start<end and end<len(prices):
            #Loss 
            if prices[start]>prices[end]:
                start = end
                end+=1
            else:
                profit = max(profit,prices[end]-prices[start])
                end+=1
        return profit


        