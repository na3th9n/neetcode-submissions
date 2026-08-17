from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        DIRS = [(1,0), (-1,0), (0, -1), (0, 1)]

        q = deque()
        distance = 0
        seen = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r, c])
                    seen.add((r, c))

        while q:
            for _ in range(len(q)):
                cr, cc = q.popleft()

                grid[cr][cc] = distance
                
                for dr, dc in DIRS:
                    nr, nc = cr + dr, cc + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1 and (nr, nc) not in seen:
                        q.append([nr, nc])
                        seen.add((nr, nc))

            distance += 1