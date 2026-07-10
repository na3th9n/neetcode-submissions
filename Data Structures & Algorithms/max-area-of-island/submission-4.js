class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        // dfs you would do the same thing
        // base case: if 0 or out of bounds: return 0
        // return 1 + dfs() to get the recursion
        // remember to set the current cell to "0"
        let maxArea = 0;
        const ROWS = grid.length;
        const COLS = grid[0].length;
        const DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

        const dfs = (r, c) => {
            if (r < 0 || c < 0 || r >= ROWS || c >= COLS || grid[r][c] === 0) {
                return 0
            }

            grid[r][c] = 0;
            let res = 1

            for (const [dr, dc] of DIRS) {
                res += dfs(r + dr, c + dc);
            }

            return res
        }
        
        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (grid[r][c] === 1) {
                    maxArea = Math.max(dfs(r, c), maxArea);
                }
            }
        }

        return maxArea;
    }
}
