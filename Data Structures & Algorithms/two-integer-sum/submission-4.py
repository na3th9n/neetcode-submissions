class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        meow = {}

        for i in range(len(nums)):
            if target - nums[i] in meow:
                return[meow[target - nums[i]], i]

            meow[nums[i]] = i
