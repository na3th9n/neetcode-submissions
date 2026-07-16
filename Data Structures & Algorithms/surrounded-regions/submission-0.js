class Solution {
    /**
     * @param {character[][]} board
     * @return {void} Do not return anything, modify board in-place instead.
     */
    solve(board) {
        // apply some bfs/dfs when encountering a 'O'
        // if a 'O' is surrounded by 'X', turn it into a X
            // we need to check if the entire region is surrounded by 'X' before we turn them into 'X'
            // if a '0' is adjacent to an edge, can NOT be surrounded (case)

        // all cases for 'O'
            // surrounded by 'X', change all 'O' into 'X'
            // '0' on an edge, abort entire call stack
                // use a flag
            // memory to remember if we visited a cell already or not
        
        const ROWS = board.length;
        const COLS = board[0].length;
        const DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

        const dfs = (r, c, isSurrounded) => {
            if (r < 0 || c < 0 || r >= ROWS || c >= COLS || board[r][c] !== 'O') {
                return;
            }

            board[r][c] = 'T';

            for (const [dr, dc] of DIRS) {
                const nr = r + dr;
                const nc = c + dc;

                dfs(nr, nc);
            }
        }

        for (let r = 0; r < ROWS; r++) {
            if (board[r][0] === 'O') dfs(r, 0);
            if (board[r][COLS - 1] === 'O') dfs(r, COLS - 1); 
        }

        for (let c = 0; c < COLS; c++) {
            if (board[0][c] === 'O') dfs(0, c);
            if (board[ROWS - 1][c] === 'O') dfs(ROWS - 1, c);
        }

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (board[r][c] === 'O') board[r][c] = 'X';
            }
        }

        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (board[r][c] === 'T') board[r][c] = 'O';
            }
        }

        return board;
    }
}
