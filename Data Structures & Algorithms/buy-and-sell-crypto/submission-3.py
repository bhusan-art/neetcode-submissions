class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10,1,5,6,7,1
        e = len(prices) - 1
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            minprice = min(price,minprice)   #10
            profit = price - minprice   # 10-10 = 0
            maxprofit = max(profit,maxprofit)
        return maxprofit



            



