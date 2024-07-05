class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        low_price = prices[0]
        for price in prices:
            if price > low_price:
                day_profit = price - low_price
                max_profit = max (max_profit, day_profit)
            else:
                low_price = price

        return max_profit
