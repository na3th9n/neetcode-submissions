# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # obvious solution is we check each node and check and the descedents of each node to make sure the conditions are right
        # can take O(n^2)
        # we use dfs to check each node if it sastifies a certain condition
        # this questions "trick" is about bounds and what bounds a BST can be in
        # the root can be any number so its bounds are -inf to +inf
        # when we go into the left subtree, everything in the left subtree have to be 
        # smaller than the parent node so the bounds become -inf to parent val
        # vise versa for right node

        def dfs(node, lowerBound, upperBound):
            if not node:
                return True

            if lowerBound < node.val < upperBound: 
                return dfs(node.left, lowerBound, node.val) and dfs(node.right, node.val, upperBound)

            else:
                return False

        return dfs(root, float("-inf"), float("inf"))