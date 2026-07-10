class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        // approach #1: bfs
        // when encountering a 1, run bfs to find the total area, so everytime there is a 1 connected
        // horizontally or vertically, add to a temporary variable
        // once bfs is over, compare to a global variable using the Math.max() function
        // remember that we have to turn a cell to "0" to indicate that it has been visited 

        let maxArea = 0;
        const ROWS = grid.length;
        const COLS = grid[0].length;
        
        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (grid[r][c] === 1) {
                    maxArea = Math.max(this.bfs(grid, r, c), maxArea);
                }
            }
        }

        return maxArea;
    }

    bfs(grid, r, c) {
        const q = new Queue();
        const DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        let area = 0;
        const ROWS = grid.length;
        const COLS = grid[0].length;

        q.enqueue([r, c]);
        area++;
        grid[r][c] = 0;

        while (!q.isEmpty()) {
            const [cr, cc] = q.dequeue();

            for (const [dr, dc] of DIRS) {
                const nr = cr + dr;
                const nc = cc + dc;

                if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && grid[nr][nc] === 1) {
                    q.enqueue([nr, nc]);
                    grid[nr][nc] = 0;
                    area++;
                }
            }
        }

        return area;
    }
}
