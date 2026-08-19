class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = INF
            for c in coins:
                if (amount - c) >= 0:
                    res = min(res, 1 + dfs(amount - c))
                
                memo[amount] = res
            return res
        minCoins = dfs(amount)

        return -1 if minCoins >= INF else minCoins
        