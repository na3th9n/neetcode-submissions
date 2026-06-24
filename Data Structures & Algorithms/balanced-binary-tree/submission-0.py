# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # compare the left and right subtree and see if the difference in height. If it more than 1, we return false and end the code
        # if it is <= 1, we do nothing and we can return the max height of that tree + 1
        # dfs to find the height of each subtree

        def dfs(root):

            if not root:
                return [True, 0]

            # calculate heights
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


            