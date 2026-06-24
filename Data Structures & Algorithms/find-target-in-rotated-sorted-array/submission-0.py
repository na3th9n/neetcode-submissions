class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init all variables
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target < nums[m]:
                if target >= nums[l]:
                    r = m - 1

                else:
                    l = m + 1

            elif target > nums[m]:
                if target <= nums[r]:
                    l = m + 1

                else:
                    r = m - 1
        
            else:
                return m
        
        return -1