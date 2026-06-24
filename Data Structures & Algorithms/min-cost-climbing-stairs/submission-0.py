class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # start at floor 0 or 1
        # cost array where each element is the cost for being on that position
        # can step either +1 step or +2 step
        # return minimum cost to pass the last index, > size of cost array

        # look at each uniqye path, and compare the minimum cost 

        # n: number of steps taken
        total_steps = len(cost)

        def dfs(n):
            if n >= total_steps:
                return 0

            return cost[n] + min(dfs(n+1), dfs(n+2))

        return min(dfs(0), dfs(1))
        