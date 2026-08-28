from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)];
        q = deque()

        def is_valid(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                return True
            
            return False


        # O(m * n)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            for i in range(len(q)):
                cr, cc = q.popleft() # (cr, cc)

                for dr, dc in DIRS:
                    nr, nc = cr + dr, cc + dc

                    if is_valid(nr, nc):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1

        