class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0

        buy = 0
        res = 0

        for sell in range(1, len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
                continue

            profit = prices[sell] - prices[buy]
            res = max(res, profit)

        return res

            
        