class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set to hold value seen
        seen = set()
        # create a for loop to go through each value, worse case O(n)
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False
        # return true if there is a number in the set already, if condition

        
         