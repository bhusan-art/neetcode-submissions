class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10,1,5,6,7,1
        e = len(prices) - 1
        maxprofit = 0
        minprice = prices[0]
        for price in prices:
            minprice = min(price,minprice)
            profit = price - minprice
            maxprofit = max(maxprofit,profit)
        return maxprofit


            



