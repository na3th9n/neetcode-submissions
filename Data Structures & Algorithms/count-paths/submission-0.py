class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # down or right
        # at each node, you can choose to either go down or right
        # cases
            # out-of-bounds: 0
            # (0, 0): 1
            # at each other node, you add the the up and left path paths    

        # use a m x n cache to store the number of paths to a certain cell
        # every cell adds the number of paths up and left
        # out of bounds have to be 0 so the edge nodes at row 0 and col 0 add 0
            # however, we can just say if it is out of bounds, we don't add anything, just for visualization

        grid = [[0 for _ in range (n)] for _ in range(m)]
        grid[0][0] = 1       


        for r in range(m):
            for c in range(n):
                if r - 1 >= 0:
                    top = grid[r - 1][c]
                else:
                    top = 0

                if c - 1 >= 0:
                    left = grid[r][c - 1] if c - 1 >= 0 else 0
                else:
                    left = 0

                grid[r][c] += (top + left)

        print(grid)
        return grid[m - 1][n - 1]