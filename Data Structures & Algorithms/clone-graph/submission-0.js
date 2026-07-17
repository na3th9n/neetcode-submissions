/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node) {
        // use dfs to clone the graph
        // start at the node 
        // create the node 
        // dfs all its neighbors and add that to the cloned node
        // create the new node
        // how do you retrieve a node
        // need some sort of memory to know if a node is visited or not
        const oldToNew = new Map();

        const dfs = (node) => {
            if (oldToNew.has(node)) {
                return oldToNew.get(node);
            }

            const copy = new Node(node.val);
            oldToNew.set(node, copy);

            for (const n of node.neighbors) {
                copy.neighbors.push(dfs(n));
            }

            return copy;
        }

        return node ? dfs(node) : null;
    }
}
