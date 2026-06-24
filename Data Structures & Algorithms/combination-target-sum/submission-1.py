class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # good base case: sum == target
        # bad base case:sum > target or the temp_inputs = []

        res = []

        # states: total_sum, curr_i, combo
        def dfs(total_sum, curr_i, combo):
            if total_sum == target:
                res.append(combo.copy())
                return

            if total_sum > target or curr_i > len(nums) - 1:
                return

            # case 1: we include the current indexed element
            combo.append(nums[curr_i])
            dfs(total_sum + nums[curr_i], curr_i, combo)
            # case 2: we don't include it in the future
            combo.pop()
            dfs(total_sum, curr_i + 1, combo)

        dfs(0, 0, [])
        
        return res

