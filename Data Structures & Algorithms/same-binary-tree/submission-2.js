/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
        // bfs and two queues and go level by level to check
        // dfs and it checks if they match each time
            // empty, returns null, checks if left and right pointer have the same value, if so, return true
            // return [p.left, q.left] === [q.left. q.right];
            // pass [bool, p, q]
        return this.dfs(p, q);
    }

    dfs(p, q) {
        if (!p && !q) {
            return true;
        }

        if (!p || !q) {
            return false;
        }

        const left = this.dfs(p.left, q.left);
        const right = this.dfs(p.right, q.right);

        const same = left && right && (p.val === q.val)
        console.log(p, q, same);
        return same;
    }
}
