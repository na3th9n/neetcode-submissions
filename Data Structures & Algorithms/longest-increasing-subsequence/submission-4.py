class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom-up approach
        n = len(nums)
        memo = [1] * len(nums)

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
        return max(memo)



        