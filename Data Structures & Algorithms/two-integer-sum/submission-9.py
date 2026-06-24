class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if there is a num in hash map where target - curr inside
        seen = {}

        for i, n in enumerate(nums):
            x = target - n

            if x in seen:
                return [seen[x], i]

            seen[n] = i

        

