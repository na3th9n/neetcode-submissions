# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0

        # want to return the maximum depth so we need to compare the left and right subtree to each other
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))




        