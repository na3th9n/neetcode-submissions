class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        minEnd = nums[0]
        maxEnd = nums[0]

        for i in range(1,n):
            temp = max(minEnd * nums[i], maxEnd * nums[i], nums[i])
            minEnd = min(minEnd * nums[i], maxEnd * nums[i], nums[i])
            maxEnd = temp
            res = max(res, maxEnd)

        return res