class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const m = matrix.length;
        const n = matrix[0].length;
        // binary search for rows

        let row = -1;
        let rl = 0, rr = m;

        while (rl < rr) {
            const mid = Math.floor((rl + rr) / 2);

            if (matrix[mid][0] <= target) {
                rl = mid + 1;
            } else {
                rr = mid;
            }
        }

        row = rr - 1;

        if (row === -1) {
            return false;
        }

        let cl = 0, cr = n - 1;
        while (cl <= cr) {
            const mid = Math.floor((cl + cr) / 2);

            if (matrix[row][mid] === target) {
                return true;
            } else if (matrix[row][mid] < target) {
                cl = mid + 1;
            } else {
                cr = mid - 1;
            }
        }

        return false;
    }
}
