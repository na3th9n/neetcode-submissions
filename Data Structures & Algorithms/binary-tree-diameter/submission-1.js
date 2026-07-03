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
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root) {
            let res = 0;

            function dfs(root) {
                if (!root) return 0; 

                const leftDepth = dfs(root.left);
                const rightDepth = dfs(root.right);

                res = Math.max(res, leftDepth + rightDepth);

                return 1 + Math.max(leftDepth, rightDepth);
            }

            dfs(root);

            return res;
    }
}
