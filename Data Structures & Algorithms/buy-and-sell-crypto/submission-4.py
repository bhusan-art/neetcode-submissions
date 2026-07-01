class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10,1,5,6,7,1
        e = len(prices) - 1
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            minprice = min(price,minprice)   #10  , 1,10 = 1,  5,1 = 1 , 1,6 = 1, 1,7=1
            profit = price - minprice   # 10-10 = 0  , 1-1 = 0, 5-1 = 4, 6-1 = 5, 7-1= 6
            maxprofit = max(profit,maxprofit)  # 0,0 = 0 ,0,0 = 0, 4,0 = 4,  5,4 = 5,
        return maxprofit



            



