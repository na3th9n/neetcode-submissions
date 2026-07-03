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
     * @return {boolean}
     */
    isBalanced(root) {
        // check if a node's left subtree and right subtree is balanced
        // pass the greatest height upwards
        // need a helper function and we can just have two states [height, isBalanced]
        const res = [true];
        this.dfs(root, res);
        return res[0];
    }

    // return the height of the tree
    dfs(root, res) {
        if (!root) return 0;

        const left = this.dfs(root.left, res);
        const right = this.dfs(root.right, res);

        if (Math.abs(left - right) > 1) {
            res[0] = false;
        }

        return 1 + Math.max(left, right);
    }
}
