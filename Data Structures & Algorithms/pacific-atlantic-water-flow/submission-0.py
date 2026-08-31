class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # row 0 and row n - 1 
        # col 0 and col m - 1
        # updating a set that determines if it is connected to the pacific or the atlantic
        
        # graph transversal (bfs or dfs)
        # call of transversal 
        
        # dfs
            # coordinates (r, c)
            # visited 
            # prev_height 

            # base case
                # out of bounds return
                # curr_height < prev_height, return

        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid(r, c, prev_height, visited):
            if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and heights[r][c] >= prev_height:
                return True
            return False

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if is_valid(nr, nc, heights[r][c], visited):
                    dfs(nr, nc, visited)
        
            return
            
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])

        return res









