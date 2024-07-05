class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                day_profit = prices[r] - prices[l]
                max_profit = max(max_profit, day_profit)
            else:
                l = r

            r = r + 1
        return max_profit
