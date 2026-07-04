class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        let numberOfIslands = 0;
        const ROWS = grid.length;
        const COLS = grid[0].length;
        const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        const dfs = (r, c) => {
            if (r < 0 || r >= ROWS || c < 0 || c >= COLS || grid[r][c] === '0') {
                return;
            }

            grid[r][c] = '0';

            for (const [dr, dc] of dirs) {
                dfs(r + dr, c + dc);
            }
        }

        for (let i = 0; i < ROWS; i++) {
            for (let j = 0; j < COLS; j++) {
                if (grid[i][j] === "1") {
                    dfs(i, j);
                    numberOfIslands++;
                }
            }
        }
        return numberOfIslands;
    }
}
