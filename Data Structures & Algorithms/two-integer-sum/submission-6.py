class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for loop to go through each element of the array = O(n)
        # need a hash map to the value as the key and the index would be the value
        seen = {}

        for i in range(len(nums)):
            for i, n in enumerate(nums):
                diff = target - n
                if diff in seen: return [seen[diff], i]

                seen[n] = i