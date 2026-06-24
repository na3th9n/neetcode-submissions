from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        islands = 0
        res = 0
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def bfs(r, c):

            q = deque([(r, c)])
            grid[r][c] = "0"

            while q:
                cr, cc = q.popleft()

                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc

                    if nr < 0 or nr >= n or nc < 0 or nc >= m or grid[nr][nc] == "0":
                        continue
                    
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1": 
                    bfs(i, j)
                    res += 1

        return res
