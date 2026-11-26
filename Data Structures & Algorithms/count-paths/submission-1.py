class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range (n + 1)] for _ in range(m + 1)]
        grid[1][1] = 1       

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                grid[r][c] += grid[r - 1][c] + grid[r][c - 1]

        return grid[m][n]
