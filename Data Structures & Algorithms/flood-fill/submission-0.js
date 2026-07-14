class Solution {
    /**
     * @param {number[][]} image
     * @param {number} sr
     * @param {number} sc
     * @param {number} color
     * @return {number[][]}
     */
    floodFill(image, sr, sc, color) {
        // Use DFS to transverse the graph
        // sr, sc is our starting cell
        // save starting color because we only want to color the adjancet cells that share that color

        // base case: if cell is not starting color, return;
        // color it,
        // for loop at each adjacent side

        if (image[sr][sc] === color) {
            return image;
        }

        const originalColor = image[sr][sc];
        const DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        const ROWS = image.length;
        const COLS = image[0].length;

        const dfs = (r, c) => {
            image[r][c] = color;

            for (const [dr, dc] of DIRS) {
                const nr = r + dr;
                const nc = c + dc;

                if (nr >= 0 && nc >= 0 && nr < ROWS && nc < COLS && image[nr][nc] === originalColor) {
                    dfs(nr, nc);
                } 
            }
        }

        dfs(sr, sc);

        return image; 
    }
}
