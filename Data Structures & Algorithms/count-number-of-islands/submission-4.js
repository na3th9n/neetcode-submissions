class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        // loop through the entire matrix
        // if we hit a 1:
            // we run bfs transversal
            // everytime we visit a node that is a "1", turn it into a "0" to indicate we visted it
        
        let numberOfIslands = 0;
        const rows = grid.length;
        const cols = grid[0].length;
        const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];

        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (grid[i][j] === "1") {
                    grid[i][j] = "0";
                    const q = new Queue([[i, j]]);

                    while (!q.isEmpty()) {
                        const [r, c] = q.dequeue();
                        for (const [nr, nc] of dirs) {
                            const cr = r + nr;
                            const cc = c + nc;

                            if (cr >= 0 && cr < rows && cc >= 0 && cc < cols && grid[cr][cc] === "1") {
                                grid[cr][cc] = "0";
                                q.enqueue([cr, cc]);
                            }
                        }
                    }
                    numberOfIslands++;
                }
            }
        }
        return numberOfIslands;
    }
}
