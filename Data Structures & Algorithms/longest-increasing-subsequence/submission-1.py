class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # base case
            # good
                # check if dp has that result already
                # if the current num at index i is > most recent entry to the subsequence
                # if it isn't prune and return the length
                # if i = len(nums), return the length
        # recursive case
            # take the max of all the possible branches and save that result

        n = len(nums)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            LIS = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[i] = LIS
            return LIS

        return max(dfs(i) for i in range(n))

            
