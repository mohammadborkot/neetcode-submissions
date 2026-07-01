class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 10 1 5 6 7 1
        # 10 -9 -5 -4 -3 -9 
        sell = prices[0]
        buy = prices[0]
        profit = 0
        # determine the smallest buy price
        for i in range(1, len(prices)):
            sell = prices[i]
            buy = min(prices[i - 1], buy)
            profit = max(sell - buy, profit)

        return profit
        