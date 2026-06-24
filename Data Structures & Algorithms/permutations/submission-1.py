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

        def dfs(first):
            if first == len(nums):
                res.append(nums[:])
                return

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                dfs(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        dfs(0)

        return res

            

        