# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 1 -> None -> None => sum = root + max(left, right)
            # max(root, root + left, root + right
        # base case: None
            # return 0
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            currSum = max(root.val, root.val + left, root.val + right, root.val + left + right)

            res[0] = max(res[0], currSum)

            return max(root.val, root.val + left, root.val + right)

        dfs(root)

        return res[0] 
