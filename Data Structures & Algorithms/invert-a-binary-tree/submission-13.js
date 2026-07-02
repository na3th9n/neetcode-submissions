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
        // iterative DFS
            // need a data structure to implemenet
            // using a stack or just an array
            // use an explicit data structure
            // use if recursion depth be too large
            // process
                // swap the nodes
                // add each node to the stack
                // then, at each node, pop that

        if (!root) return null;
        const stack = [root];

        while (stack.length) {
            const node = stack.pop();
            [node.left, node.right] = [node.right, node.left];
            if (node.left) {
                stack.push(node.left);
            }

            if (node.right) {
                stack.push(node.right);
            }
        }

        return root;
    }
}
