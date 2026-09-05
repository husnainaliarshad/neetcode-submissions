class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min = 0, 0 
        for i, n in enumerate(prices):
            if n < prices[min]:
                min = i
            newProfit = n - prices[min]
            if newProfit > profit:
                profit = newProfit
        return profit