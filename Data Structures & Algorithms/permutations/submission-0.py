class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # state
            # idx: pointer that indicates the first number of the permutation
                # uses current element
                    # reset i to 0, reduce the available_nums by removing available_nums[idx]
                # excludes curernt element
                    # icrement i
                    # do not change available_nums
                # current_combo: array
                    # have all the combos which are the removed elements
            # available_nums: array that does not include the previous idx call
        
        res = []

        def dfs(available_nums, perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(available_nums)):
                new_available_nums = available_nums.copy()
                perm.append(new_available_nums.pop(i))
                dfs(new_available_nums, perm)
                perm.pop()
                

        dfs(nums, [])

        return res

            

        