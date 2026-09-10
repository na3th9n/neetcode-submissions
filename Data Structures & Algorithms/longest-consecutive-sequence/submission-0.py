class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums into a set
        # find all the sequences
            # checking if the left neighbor exists or not
                # exists: start the count
                    # keep checking the right neigbor and storing the count in a result
                # does not exist: go next

        nums_set = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in nums_set:
                count = 1

                while n + 1 in nums_set:
                    count += 1
                    n += 1

                res = max(res, count)

        return res 

        