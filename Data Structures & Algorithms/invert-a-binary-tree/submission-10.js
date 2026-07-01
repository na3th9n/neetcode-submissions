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
     * @return {TreeNode}
     */
    invertTree(root) {
        // when dealing with trees, use DFS or BFS to transverse the tree
        // invert left and right
        // call the same functino on the children
        // base case: if this.val = null, return
        if (root === null) {
            return root;
        }
        const tempNode = root.left;
        root.left = root.right;
        root.right = tempNode;

        this.invertTree(root.left);
        this.invertTree(root.right);

        return root;
    }
}
