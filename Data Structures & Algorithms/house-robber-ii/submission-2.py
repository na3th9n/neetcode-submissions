class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            rob1, rob2 = 0, 0
            
            for i in range(len(arr)):
                temp = rob2
                rob2 = max(arr[i] + rob1, rob2)
                rob1 = temp

            return rob2
        
        return max(helper(nums[:-1]), helper(nums[1:]), nums[0])