class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # conditions that will give you the max profit
        # looking for one day to buy and one day to sell
        # buy at the cheapest day and sell at the most expensive day

        buy = 0
        max_profit = 0

        for sell in range(1, len(prices)):
            max_profit = max(max_profit, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell


        return max_profit


        